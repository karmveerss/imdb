from django.db import models
from datetime import datetime
from django.db.models import Sum, Avg
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.name)[:50]

class Genre(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.name)[:50]

class Movie(models.Model):
    name = models.CharField(max_length=100)
    popularity = models.FloatField(default=0.0, null=True, blank=True)
    director = models.ForeignKey(Person)
    genre = models.ManyToManyField(Genre)
    imdb_score = models.FloatField(default=0.0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        current_date = datetime.now().date()
        avg_data = Rating.objects.filter(movie = self).aggregate(Avg('rating'))
        if avg_data.get('rating__avg', None):
            self.imdb_score = avg_data.get('rating__avg', None)
        sum_data = PageViews.objects.filter(views_date=current_date,
                                            movie = self,
                                            ).aggregate(Sum('views_count'))
        if sum_data.get('views_count__sum', None):
            self.popularity = sum_data.get('views_count__sum', None)
        super(Movie, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.name)[:50]

class PageViews(models.Model): # Used to calculate popularity
    movie = models.ForeignKey(Movie, null=True, blank=True)
    views_count = models.IntegerField(default=0)
    views_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        current_date = datetime.now().date()
        obj = PageViews.objects.filter(views_date=current_date,
                                    movie = self.movie).first()
        if obj:
            obj.views_count+=self.views_count
            self = obj
        super(PageViews, self).save(*args, **kwargs)
        (self.movie).save()

class Rating(models.Model): # Used to calculate imdb_score
    movie = models.ForeignKey(Movie, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Rating, self).save(*args, **kwargs)
        (self.movie).save()

class Review(models.Model):
    movie = models.ForeignKey(Movie, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.title)[:50]