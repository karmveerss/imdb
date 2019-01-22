from django.contrib import admin
from movies.models import Movie, Review, Rating, PageViews, Person, Genre

class RatingInline(admin.StackedInline):
    model = Rating
    verbose_name = 'Rating'
    verbose_name_plural = 'Ratings'
    fields = ('movie', 'user', 'rating')
    readonly_fields = ('movie',)
    extra = 0

class PageviewInline(admin.StackedInline):
    model = PageViews
    verbose_name = 'PageViews'
    verbose_name_plural = 'PageViews'
    fields = ('movie', 'views_date', 'views_count')
    readonly_fields = ('movie', 'views_date',)
    extra = 0

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', 'popularity','director', 'imdb_score', 'created_at')
    list_per_page = 30
    fields = ('name', 'popularity','director','genre', 'imdb_score')
    inlines = [RatingInline, PageviewInline]
    search_fields = ['name', 'director']
    ordering = ['name']
    readonly_fields = ('popularity', 'imdb_score', 'created_at', )

admin.site.register(Movie, MoviesAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_per_page = 30
    fields = ('name',)
    search_fields = ('name',)
    ordering = ['name']
    readonly_fields = ('created_at',)

admin.site.register(Person, PersonAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name','created_at')
    list_per_page = 30
    fields = ('name',)
    search_fields = ('name',)
    ordering = ['name']
    readonly_fields = ('created_at',)

admin.site.register(Genre, GenreAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie', 'user', 'created_at')
    list_per_page = 30
    fields = ('movie', 'user', 'title', 'description', 'rating', 'created_at')
    search_fields = ('title', 'movie',)
    ordering = ['created_at']
    readonly_fields = ('created_at',)

admin.site.register(Review, ReviewAdmin)
