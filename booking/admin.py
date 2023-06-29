from django.contrib import admin
from booking.models import Listing, Host, Amenity, Calendar, Review, User
# Register your models here.

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Amenity)
admin.site.register(Calendar)
admin.site.register(Review)
admin.site.register(Host)
