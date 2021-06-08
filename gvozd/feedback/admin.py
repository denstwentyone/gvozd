from django.contrib import admin
from .models import Message, Favour


class FavourAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = ('id',)


class MessageAdmin(admin.ModelAdmin):
    def favour(obj):
        return obj.favour.name + ' ' + str(obj.favour.price)
    list_display = ('id', 'username', favour , 'text')


admin.site.register(Message, MessageAdmin)
admin.site.register(Favour, FavourAdmin)
