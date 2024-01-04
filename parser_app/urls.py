from django.urls import path
from .views import create_table_from_excel_view

urlpatterns = [
    path('create_table_from_excel/', create_table_from_excel_view, name='create_table_from_excel'),

]
