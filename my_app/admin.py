from django.contrib import admin
from my_app.models import MonkeyBarMenuItem, MonkeyBarEmployee

# Register your models here.
admin.site.register(MonkeyBarMenuItem)
admin.site.register(MonkeyBarEmployee)
