from django.contrib import admin
from .models import Movie, Review, Comment

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Comment)
class MovieAdmin(admin.ModelAdmin):
    list_display = '__all__'

class ReviewAdmin(admin.ModelAdmin):
    list_display = '__all__'

class CommentAdmin(admin.ModelAdmin):
    list_display = '__all__'