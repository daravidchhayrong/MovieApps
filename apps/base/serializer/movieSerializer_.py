from rest_framework import serializers
from apps.base.models import Movie
from apps.base.models.movie_ import Actor, Genre, Director

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['firstName', 'lastName', 'profile_path']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['firstName', 'lastName', 'imageUrl']


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, required=False)
    genres = GenreSerializer(many=True, required=False)
    directors = DirectorSerializer(many=True, required=False)
    class Meta:
        model = Movie
        fields = ['movieId', 'title', 'releaseYear', 'genres', 'duration', 'trailerUrl', 'imgUrl', 'tagLine', 'overview', 'country', 'originalLanguage', 'actors', 'directors']

        def create(self, validated_data):
            actors_data = validated_data.pop('actors', [])
            genres_data = validated_data.pop('genres', [])
            directors_data = validated_data.pop('directors', [])

            movie_instance = Movie.objects.create(**validated_data)

            for actor_data in actors_data:
                Actor.objects.create(movie=movie_instance, **actor_data)

            for genre_data in genres_data:
                Genre.objects.create(movie=movie_instance, **genre_data)

            for director_data in directors_data:
                Director.objects.create(movie=movie_instance, **director_data)

            return movie_instance