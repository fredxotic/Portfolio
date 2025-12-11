from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<slug:slug>/', views.portfolio_details, name='portfolio-details'),
]