#pour modifier et supprimer les posts 
from django.contrib import admin
from .models import Post

admin.site.register(Post)