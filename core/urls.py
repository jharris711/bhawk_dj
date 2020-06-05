from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    home_page,
    press_kit,
    booking,
    audio,
    social,
    upcoming,
    PostDetailView
)

app_name = 'core'

urlpatterns = [
    path('', home_page, name='home'),
    path('press-kit/', press_kit, name='press-kit'),
    path('booking/', booking, name='booking'),
    path('audio/', audio, name='audio'),
    path('social/', social, name='social'),
    path('news-and-events/', upcoming, name='upcoming'),
    path('news-and-events/<slug>/', PostDetailView.as_view(), name='news-post'),
]
