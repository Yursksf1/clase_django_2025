from django.contrib import admin
from myapp.models import Park

class ParkAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    list_filter = ('city',)
    search_fields = ('name',)

admin.site.register(Park, ParkAdmin)