from django.contrib import admin
from .models import Profile, Address, Identification, Family
# Register your models here.
admin.site.register(Address)
admin.site.register(Identification)
admin.site.register(Family)
admin.site.register(Profile)
