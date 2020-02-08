from django.urls import path
from .views import company_list, company_detail, CompanyAPIView, CompanyDetails

urlpatterns = [
    #path('company/', company_list),
    path('company/', CompanyAPIView.as_view()),
    #path('detail/<int:pk>/', company_detail),
    path('detail/<int:id>/', CompanyDetails.as_view()),
]