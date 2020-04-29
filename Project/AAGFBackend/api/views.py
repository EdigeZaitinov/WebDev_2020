from django.shortcuts import render
from .models import GamesCategory,Games,FilmsCategory,Films,AAGFUsers
from django.http import JsonResponse,HttpResponse
from django.core import serializers

def get_game_categories(request):
    game_categories=GamesCategory.objects.all()
    data=serializers.serialize('json',game_categories)
    return HttpResponse(data)

def get_games(request):
    games=Games.objects.all()
    data=serializers.serialize('json',games)
    return HttpResponse(data)

def get_games_by_category(request,category_id):
    games=Games.objects.filter(category__id=category_id)
    data=serializers.serialize('json',games)
    return HttpResponse(data)

def get_game_by_name(request,gameName):
    game=Games.objects.filter(name=gameName)[:1]
    data=serializers.serialize('json',game)
    return HttpResponse(data)

def get_film_categories(request):
    film_categories=FilmsCategory.objects.all()
    data=serializers.serialize('json',film_categories)
    return HttpResponse(data)

def get_films(request):
    films=Films.objects.all()
    data=serializers.serialize('json',films)
    return HttpResponse(data)

def get_films_by_category(request,category_id):
    films=Films.objects.filter(category__id=category_id)
    data=serializers.serialize('json',films)
    return HttpResponse(data)

def get_film_by_name(request,filmName):
    film=Films.objects.filter(name=filmName)[:1]
    data=serializers.serialize('json',film)
    return HttpResponse(data)

def create_user(request,user_email,user_password):
   if request.method == "POST":
        user = AAGFUsers()
        user.email = request.POST.get(user_email)
        user.password = request.POST.get(user_password)
        user.save()

def get_users(request):
    users=AAGFUsers.objects.all()
    data=serializers.serialize('json',users)
    return HttpResponse(data)

def get_user(request,user_email,user_password):
    user=AAGFUsers.objects.filter(email=user_email,password=user_password)[:1]
    data=serializers.serialize('json',user)
    return HttpResponse(data)



