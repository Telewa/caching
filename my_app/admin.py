from django.contrib import admin

# Register your models here.
from my_app.models import Flag


class FlagAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "enabled", "created_at", "updated_at",)
    list_filter = ("enabled",)
    list_display_links = ('id', "name",)
    search_fields = ("name",)
    list_per_page = 10
    ordering = ("id",)


admin.site.register(Flag, FlagAdmin)