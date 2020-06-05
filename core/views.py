from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import BookingForm
from .models import Soundcloud, UpcomingShow, PressKitImg, Bandcamp, NewsPost


def home_page(request, *args, **kwargs):
    soundclouds = Soundcloud.objects.all()
    upcoming_shows = reversed(UpcomingShow.objects.all())
    context = {
        "soundclouds": soundclouds,
        "upcoming_shows": upcoming_shows
    }
    return render(request, "home.html", context, status=200)


def press_kit(request, *args, **kwargs):
    pk_pics = PressKitImg.objects.all()
    context = {
        "pk_pics": pk_pics
    }
    return render(request, "press-kit.html", context, status=200)


def booking(request, *args, **kwargs):
    if request.method == 'GET':
        form = BookingForm()
    else:
        form = BookingForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['bhawk.page@gmail.com'])
                messages.success(request, "Your message has been sent!")
                return redirect("core:booking")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    context = {
        "form": form
    }
    return render(request, "booking.html", context, status=200)


def audio(request, *args, **kwargs):
    soundclouds = Soundcloud.objects.all()
    bandcamps = Bandcamp.objects.all()
    context = {
        "soundclouds": soundclouds,
        "bandcamps": bandcamps
    }
    return render(request, "audio.html", context, status=200)


def social(request, *args, **kwargs):
    return render(request, "social.html", status=200)


def upcoming(request, *args, **kwargs):
    shows = reversed(UpcomingShow.objects.all())
    news_posts = reversed(NewsPost.objects.all())
    context = {
        "shows": shows,
        "news_posts": news_posts
    }
    return render(request, 'news-and-events.html', context, status=200)
