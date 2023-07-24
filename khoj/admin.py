from django.contrib import admin
from .models import *

admin.site.site_header = "Ami Coding Pari Na Admin"
admin.site.site_title = "Ami Coding Pari Na"
admin.site.index_title = "Welcome to Ami Coding Pari Na Admin Panel"


class InputAdmin(admin.ModelAdmin):
    list_display = ('user', 'input_values', 'timestamp', 'user_id')


admin.site.register(Input, InputAdmin)
