from django.urls import path
from .views import LoginView, CadasterView

urlpatterns = [
    path('cadaster/', CadasterView.as_view(), name="CadasterView"),
    path('login/', LoginView.as_view(), name="LoginView")
]