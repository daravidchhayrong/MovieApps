from django.db import models

# class Director(models.Model):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female')
#     )
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     imageUrl = models.CharField(max_length=100)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

#     # def full_name(self) -> str :
#     #     return "%s %s"%(self.first_name, self.last_name)

#     def __str__(self):
#         return (self.first_name + " " + self.last_name)

# class Actor(models.Model):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female')
#     )
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     imageUrl = models.CharField(max_length=100)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

#     # def full_name(self) -> str:
#     #     return "%s %s"%(self.first_name, self.last_name)

#     def __str__(self):
#         return (self.first_name)

class Director(models.Model):
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    profile_path = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return (self.firstName + " " + self.lastName)

class Actor(models.Model):
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    profile_path = models.CharField(max_length=100)

    def __str__(self):
        return (self.firstName + " " + self.lastName)

class Genre(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Movie(models.Model):
    movieId = models.CharField(max_length=20)
    title = models.CharField(max_length=500)
    releaseYear = models.CharField(max_length=5, blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    trailerUrl = models.CharField(max_length=100, blank=True, null=True)
    imgUrl = models.CharField(max_length=100)
    tagLine = models.CharField(max_length=500, blank=True, null=True)
    overview = models.CharField(max_length=1000, blank=True, null=True)
    country = models.CharField(max_length=50)
    originalLanguage = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, blank=True, null=True)
    directors = models.ManyToManyField(Director, blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'movie'
    

