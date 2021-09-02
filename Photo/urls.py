from django.urls import path
from . import views
from .views import PhotoList, ViewPic, AddPicture, AddComment, UpdatePicture, DeletePicture, EditComment

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('search_category', views.search_category, name='search-category'),
  #  path('', PhotoList.as_view(), name='gallery'),
    path('photo/<str:pk>/', ViewPic.as_view(), name='view-pic'),
    path('photo/<str:pk>/update', UpdatePicture.as_view(), name='update-pic'),
    path('photo/<str:pk>/delete', DeletePicture.as_view(), name='delete-pic'),
    path('photo-create/', AddPicture.as_view(), name='add-pic'),
     path('photo/<str:pk>/comment/', AddComment.as_view(), name='add_comment'),
     path('photo/<str:pk>/comment/edit', EditComment.as_view(), name='edit_comment'),
  #  path('photo/<str:pk>/add-comment', views.add_comment, name='add_comment'),
]