from django.contrib import admin
from .models import Profile, Category, Note

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['login', 'password', 'notes_count']

    def notes_count(self, obj):
        return obj.note_set.count()

    def notes_price_count(self, obj):
        return sum(obj.note_set.all().values_list('price', flat=True))


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'profile', 'category', 'price']
    list_filter = ['profile', 'category']
    search_fields = ('name', 'category__name')


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name', 'notes_count', 'notes_price_count']

    def notes_count(self, obj):
        return obj.note_set.count()

    def notes_price_count(self, obj):
        return sum(obj.note_set.all().values_list('price', flat=True))
        

