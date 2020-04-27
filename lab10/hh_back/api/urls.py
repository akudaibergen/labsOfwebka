from django.urls import path
from api.views.views import companies_list, company_detail, company_vacancies, vacancy_list, vacancy_detail
from api.views.viewsCBF import CompanyList


urlpatterns = [
    path('companies/', companies_list),
    # path('companies/', CompanyList.as_view()),

    # path('api/companies/<int:pk>/', CompanyDetails.as_view()),
    # path('api/companies/<int:company_id>/vacancies/', CompanyVacancies.as_view()),
    # path('api/vacancies/', VacancyList.as_view()),
    # path('api/vacancies/<int:pk>/', VacancyDetails.as_view()),

    path('companies/<int:company_id>/', company_detail),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('companies/<int:company_id>/vacancies/', company_vacancies)
]