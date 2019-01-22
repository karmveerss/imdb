from movies.models import Movie
from rest_framework import generics
from django_filters import FilterSet
from movies.serializers import MovieSerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

class MovieFilter(FilterSet):

    name = filters.CharFilter(method="filter_by_name")

    class Meta:
        model = Movie
        fields = ('name',)

    def filter_by_name(self, queryset, name, value):
        queryset = queryset.filter(name__icontains=value)
        return queryset

class MovieList(generics.ListAPIView):

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = MovieFilter

    ordering_fields = ('name', 'popularity', 'imdb_score')
    ordering = ('name',)

    search_fields = ('name', 'director__name', 'genre__name')
