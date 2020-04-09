from django.shortcuts import render
from .models import Company,Vacancy

def home(request):
    name='Edige'
    surname='Zaitinov'
    data={"name":name,"surname":surname}
    return render(request,'api.html',context=data)

def companies(request):
    companies=Company.objects.all()
    data={"companies":companies}
    return render(request,'api_companies.html',context=data)

def one_company(request,company_id):
    company=Company.objects.get(id=company_id)
    data={"c":company}
    return render(request,'one_company.html',context=data)

def vacancies_by_company(request,company_id):
    vacancies=Vacancy.objects.filter(company__id=company_id)
    company=Company.objects.get(id=company_id)
    data={'vacancies':vacancies,'c':company}
    return render(request,'vacancies_by_company.html',context=data)                                       
    # получение id связанной с товаром компании
    # Product.objects.get(id=1).company.id
    
    #  получение названия связанной с товаром компании
    # Product.objects.get(id=1).company.name
    
    #  получение товаров, которые принадлежат к компании "Apple"
    # Product.objects.filter(company__name="Apple")

def vacancies(request):
    vacancies=Vacancy.objects.all()
    companies=Company.objects.all()
    data={'vacancies':vacancies,'companies':companies}
    return render(request,'vacancies.html',context=data)

def one_vacancy(request,vacancy_id):
    vacancy=Vacancy.objects.get(id=vacancy_id)
    company=Company.objects.get(id=vacancy.company_id)
    data={"v":vacancy,"c":company}
    return render(request,'one_vacancy.html',context=data)

def top_ten(request):
    vacancies=Vacancy.objects.order_by('-salary')[0:9]
    companies=Company.objects.all()
    data={'vacancies':vacancies,'companies':companies}
    return render(request,'top_ten.html',context=data)

