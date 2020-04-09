from django.urls import path
from api import views

urlpatterns = [
    path('',views.home,name='home'),
    path('companies/',views.companies,name='companies'),
    path('companies/<int:company_id>/',views.one_company,name='one_company'),
    path('companies/<int:company_id>/vacancies/',views.vacancies_by_company,name='vacancies_by_company'),
    path('vacancies/',views.vacancies,name='vacancies'),
    path('vacancies/<int:vacancy_id>/',views.one_vacancy,name='one_vacancy'),
    path('vacancies/top_ten/',views.top_ten,name='top_ten')
    ]
