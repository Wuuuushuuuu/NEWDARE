from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from  Client.models import client, Records, Bookings
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'name','contact_no','date_joined',"last_login", 'is_admin','is_staff')
    search_fields = ('email', 'contact_no', 'name')
    readonly_fields = ('id', 'date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(client, AccountAdmin)
admin.site.register(Records)
admin.site.register(Bookings)