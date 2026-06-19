from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="stories",
    
)


    character = models.CharField(
        max_length=200
    )


    keyword = models.CharField(
        max_length=100
    )


    theme = models.CharField(
        max_length=100
    )


    length = models.CharField(
        max_length=50,
        default="medium"
    )


    age_group = models.CharField(
        max_length=50,
        default="children"
    )


    title = models.CharField(
        max_length=200
    )


    content = models.TextField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )



    def __str__(self):
        return self.title