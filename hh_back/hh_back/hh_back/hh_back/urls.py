"""hh_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views import companies_list, company_detail, company_vacancies, vacancies_list, vacancy_detail, vacancy_top

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies/', companies_list),
    path('api/companies/<int:company_id>/', company_detail),
    path('api/companies/<int:company_id>/vacancies/', company_vacancies),
    path('api/vacancies/', vacancies_list),
    path('api/vacancies/<int:vacancy_id>/', vacancy_detail),
    path('api/vacancies/top_ten/', vacancy_top)
]
