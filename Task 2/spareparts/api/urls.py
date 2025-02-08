from django.urls import path
from . import views

urlpatterns = [
    path('spare-parts/', views.SparePartListCreateView.as_view()),
    path('spare-parts/<int:pk>', views.SparePartRetrieveUpdateDestroyView.as_view()),
]