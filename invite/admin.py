from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Photo, Music, Time, Guest
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ('title',)
@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ('title',)
@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
	list_display = ('day',)
	search_fields = ('day',)
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
	list_display = ('fullname',)
	search_fields = ('fullname',)


admin.site.site_header = _("Wedding")
admin.site.site_title = _("Wedding")
