from django.urls import path

# https://docs.djangoproject.com/en/3.2/intro/tutorial01/#write-your-first-view
from . import views

# https://docs.djangoproject.com/en/3.2/intro/tutorial03/#namespacing-url-names
app_name = 'deposits'
urlpatterns = [
    path('', views.DepositListView.as_view(), name='index'),
    path('deposit/<int:pk>/', views.DepositDetailView.as_view(), name='get-deposit'),
    path('deposit/new/', views.AddDepositView.as_view()),
]


