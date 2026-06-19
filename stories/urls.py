from django.urls import path
from . import views


urlpatterns = [

    # Home page
    path(
        "home/",
        views.home,
        name="home"
    ),


    # Story generation page
    path(
    "generate/",
    views.generate_story,
    name="generate"
),
    path(
    "library/",
    views.library,
    name="library"
),


path(
    "story/<int:id>/",
    views.story_detail,
    name="story_detail"
),
path(
"",
views.register,
name="register"
),

path(
"login/",
views.user_login,
name="login"
),

path( "logout/",
        views.user_logout,
        name="logout"
    ),
path(
    "profile/",
    views.profile,
    name="profile"
),
path(
    "story/edit/<int:id>/",
    views.edit_story,
    name="edit_story"
),


path(
    "story/delete/<int:id>/",
    views.delete_story,
    name="delete_story"
),

]