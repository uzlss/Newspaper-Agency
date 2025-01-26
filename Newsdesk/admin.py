from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from Newsdesk.models import Topic, Redactor, Newspaper


admin.site.unregister(Group)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    ordering = ("name",)


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "years_of_experience",
                )
            },
        ),
    )


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_select_related = ("topic",)
    list_display = ("title", "topic")
    list_filter = ("topic",)
    ordering = ("topic__name", "title")
    search_fields = ("title",)
