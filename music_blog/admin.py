from django.contrib import admin
from .models import Review, Category

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Review, ReviewAdmin)
admin.site.register(Category)
