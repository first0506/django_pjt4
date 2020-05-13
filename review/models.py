from django.db import models
from django.conf import settings

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_url = models.URLField(max_length=150)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    rank = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                            related_name='like_reviews')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    recommend = models.BooleanField(default=True)