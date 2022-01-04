from django.contrib import admin
from url_shortening.models import URL


class URLAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'user')


admin.site.register(URL, URLAdmin)
