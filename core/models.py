from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary.uploader
from django.shortcuts import reverse


class Soundcloud(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=10000)

    def __str__(self):
        return self.title


class UpcomingShow(models.Model):
    title = models.CharField(max_length=200)
    day_of_week = models.CharField(max_length=9)
    date = models.DateField()
    time = models.CharField(max_length=15)
    guest = models.CharField(max_length=500, null=True, blank=True)
    venue = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    description = models.TextField()
    link_to_tickets = models.CharField(max_length=500)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

    """ Informative name for model """
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)


class PressKitImg(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

    """ Informative name for model """
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)


class Bandcamp(models.Model):
    title = models.CharField(max_length=200)
    iframe_src = models.CharField(max_length=10000)
    iframe_a_href = models.CharField(max_length=10000)
    iframe_a_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.title


class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = description = models.TextField()
    slug = models.SlugField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:news-post", kwargs={
            'slug': self.slug
        })

    """ Informative name for model """
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)


class Subscriber(models.Model):
    email = models.EmailField(max_length=300)
