from django.urls import path
from .views import UpdateProfilePicture

urlpatterns = [
   # path('profile_pic/', AddProfilePicture.as_view(), name='profile-pic'),
    path('profile/<str:pk>/update/', UpdateProfilePicture.as_view(), name='profile-update')
]
