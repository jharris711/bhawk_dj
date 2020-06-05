from django.contrib import admin
from .models import Soundcloud, UpcomingShow, PressKitImg, Bandcamp, NewsPost

# Register your models here.
admin.site.register(Soundcloud)
admin.site.register(UpcomingShow)
admin.site.register(PressKitImg)
admin.site.register(Bandcamp)
admin.site.register(NewsPost)
