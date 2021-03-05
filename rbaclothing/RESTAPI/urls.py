from django.urls import path
from . import views

urlpatterns = [
    path('update/<int:id>/', views.update_api_data, name="update_Order"),
    path('display/', views.Display_API, name="Display_product"),
    path('delete/<int:id>/', views.Deleta_api_data, name="delete_Order"),
    path('create/', views.postAPI, name="postOrderAPI"),
    path('page/<int:PageNo>/<int:Size>/', views.pagination, name="delete_Order"),




    
]