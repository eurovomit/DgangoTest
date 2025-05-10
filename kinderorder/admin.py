from django.contrib import admin

from kinderorder.models import Typephoto


@admin.register(Typephoto)
class TypephotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'size')
    list_display_links = ('id', 'price', 'size')

