from django.shortcuts import render
from .models import GamesCategory,Games,FilmsCategory,Films
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

