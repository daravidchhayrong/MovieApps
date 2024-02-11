from django.contrib import admin
from .models import Movie
from .models.movie_ import Genre, Actor, Director

class ActorAdmin(admin.ModelAdmin):
    search_fields = ['firstName', 'lastName']
    def save_model(self, request, obj, form, change):
        existing_actor = Actor.objects.filter(first_name=obj.first_name, last_name=obj.last_name)
        if existing_actor.exists() and not change:
            error_message = "An actor with the same first name and last name already exists."
            self.message_user(request, error_message, level=admin.ERROR)
            return
        super().save_model(request, obj, form, change)



# Register your models here.
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor, ActorAdmin)

