from django.urls import path

# https://docs.djangoproject.com/en/3.2/intro/tutorial01/#write-your-first-view
from . import views

# https://docs.djangoproject.com/en/3.2/intro/tutorial03/#namespacing-url-names
app_name = 'deposits'
urlpatterns = [
    path('', views.DepositListView.as_view(), name='index'),
    #path('get_user/<int:pk>', views.UserDetailView.as_view()),
    path('deposit/new', views.AddDepositView.as_view()),
    #path('edit_user/<int:pk>/', views.EditUserView.as_view()),
    #path('delete_user/<int:pk>/', views.DeleteUserView.as_view()),
]


