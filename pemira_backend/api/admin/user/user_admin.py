from django.contrib.admin import ModelAdmin

class UserAdmin(ModelAdmin):
    list_display = ["name", "email", "last_login"]
