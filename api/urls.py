from django.urls import path
from . import views

urlpatterns=[
    path('drinks/',views.drinks_list,name='drinks'),
    path('add-drink/',views.add_Drink,name='add drink'),
    path('drink/<int:id>/',views.drink_Detail,name='drink detail'),
    path('drink-update/<int:id>/',views.drink_Update,name='drink update'),
    path('drink-delete/<int:id>/',views.drink_Delete,name='drink delete')

]