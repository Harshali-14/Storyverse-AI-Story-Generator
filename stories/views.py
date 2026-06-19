from .models import Story
from django.shortcuts import render, get_object_or_404, redirect
import os
from google import genai
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")


        if password1 != password2:

            messages.error(
                request,
                "Passwords do not match"
            )

            return redirect("register")


        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect("register")


        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )


        login(request, user)


        messages.success(
            request,
            "Account created successfully"
        )


        return redirect("login")


    return render(
        request,
        "register.html"
    )



def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(
                request,
                user
            )


            messages.success(
                request,
                "Welcome back!"
            )


            return redirect("home")


        else:

            messages.error(
                request,
                "Invalid username or password"
            )


    return render(
        request,
        "login.html"
    )


@login_required
def user_logout(request):

    logout(request)


    messages.success(
        request,
        "Logged out successfully"
    )


    return redirect("login")

@login_required
def profile(request):

    return render(
        request,
        "profile.html"
    )
    
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@login_required
def generate_story(request):

    if request.method == "POST":

        character = request.POST.get("character")
        keyword = request.POST.get("keyword")
        theme = request.POST.get("theme")
        length = request.POST.get("length")
        age = request.POST.get("age")


        prompt = f"""
Write a creative story.

Character:
{character}

Keyword:
{keyword}

Theme:
{theme}

Story Length:
{length}

Age Group:
{age}


Follow these rules:

If age group is Children (5-10 years):
- Use very simple words.
- Use short sentences.
- Avoid difficult vocabulary.
- Make it fun and easy to understand.
- Add a small moral lesson.

If age group is Young Readers (11-17 years):
- Use simple but interesting language.
- Add emotions, adventure and imagination.
- Use moderate vocabulary.

If age group is Adults:
- Use mature language.
- Add deeper emotions and complex characters.
- Make the story meaningful.


Create:
- Beginning
- Middle
- Ending

Make the story engaging and match the selected age group.
"""

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )


            story_text = response.text


            story = Story.objects.create(
            user=request.user,

            title=f"{character} Story",

            character=character,

            keyword=keyword,

            theme=theme,

            length=length,

            age_group=age,

            content=story_text

        )
            return redirect(
                "story_detail",
                id=story.id
            )


        except Exception as e:

            print(e)

            return render(
                request,
                "generate.html",
                {
                    "error":
                    "AI generation failed. Try again."
                }
            )


    return render(request,"generate.html")


@login_required
def home(request):
    return render(request, "home.html")
@login_required
def library(request):

    stories = Story.objects.filter(
        user=request.user
    ).order_by('-created_at')


    return render(
        request,
        "library.html",
        {
            "stories": stories
        }
    )

@login_required
def story_detail(request,id):

    story = get_object_or_404(
    Story,
    id=id,
    user=request.user
)

    return render(
        request,
        "result.html",
        {
            "story":story
        }
    )

@login_required
def edit_story(request,id):

    story = get_object_or_404(
    Story,
    id=id,
    user=request.user
)


    if request.method=="POST":

        story.title = request.POST.get("title")
        story.content = request.POST.get("content")

        story.save()


        messages.success(
            request,
            "Story updated successfully ✨"
        )

        return redirect(
            "library"
        )


    return render(
        request,
        "edit_story.html",
        {
            "story":story
        }
    )




@login_required
def delete_story(request,id):

    story = get_object_or_404(
    Story,
    id=id,
    user=request.user
)


    if request.method=="POST":

        story.delete()

        messages.success(
            request,
            "Story deleted 🗑️"
        )

        return redirect(
            "library"
        )


    return render(
        request,
        "delete_story.html",
        {
            "story":story
        }
    )