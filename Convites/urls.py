from django.urls import path
from .views import CreateConvite, DeleteConvite, EditConvite

urlpatterns = [
    path("create/convite/", CreateConvite.as_view(), name="create-convite"),
    path("delete/convite/<int:id>/", DeleteConvite.as_view(), name="delete-convite"),
    path("edit/convite/<int:id>/", EditConvite.as_view(), name="edit-convite")
]