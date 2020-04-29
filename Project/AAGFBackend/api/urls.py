from django.urls import path
from api import views

urlpatterns = [
    path('game_categories/', views.get_game_categories,name='game_categories'),
    path('game_categories/games', views.get_games,name='games'),
    path('game_categories/<int:category_id>',views.get_games_by_category,name='games_by_category'),
    path('game_categories/<str:gameName>', views.get_game_by_name,name='game_by_name'),
    path('film_categories/', views.get_film_categories,name='film_categories'),
    path('film_categories/films', views.get_films,name='films'),
    path('film_categories/<int:category_id>',views.get_films_by_category,name='films_by_category'),
    path('film_categories/<str:filmName>', views.get_film_by_name,name='film_by_name'),
    path('users', views.get_users,name='get_users'),
    path('users/<str:user_email>/<str:user_password>', views.get_user,name='get_user'),
]