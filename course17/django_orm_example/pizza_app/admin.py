from django.contrib import admin

from pizza_app.models import Address

# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'full', )


admin.site.register(Address, AddressAdmin)
