from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','contact_date')
    list_display_links = ('id','name')

admin.site.register(Contact,ContactAdmin)