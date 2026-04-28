from django.urls import path
from .views import BookGenericApiView

urlpatterns = [
    path('api/', BookGenericApiView.as_view()),
    path('api/<int:pk>/', BookGenericApiView.as_view()),
]