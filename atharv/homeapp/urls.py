from django.urls import path
from .views import *
from .products_apis.urls import *

urlpatterns = [
    path('', homepage, name="homepage"),
    path('page1/', page1, name="page1"),
    path('page2/', page2, name="page2"),
    path('page3/', page3, name="page3"),
    path('page4/', page4, name="page4"),
    path('getProducts/', getProducts, name="getProducts"),
    path('addUser/', addUser, name="addUser"),
    path('getAllUsers/', getAllUsers, name="getAllUsers"),
    path('getUser/<int:user_id>/', getUser, name="addUser"),
    path('deleteUser/<int:user_id>/', deleteUser, name="deleteUser"),
]
