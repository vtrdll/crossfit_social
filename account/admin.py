from django.contrib import admin
from .models import Profile
# Register your models here.



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_coach', 'box', 'category')
    list_filter = ('is_coach', 'box', 'category')
    search_fields = ('user__username',)



admin.site.register(Profile, ProfileAdmin)