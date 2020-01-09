from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('eaters/create/', views.EaterCreate.as_view(), name='eaters_create'),
    path('eaters/<int:pk>/update/',
         views.EaterUpdate.as_view(), name='eaters_update'),
    path('reviews/create/', views.ReviewCreate.as_view(), name='reviews_create'),
    path('reviews/<int:pk>/update/',
         views.ReviewUpdate.as_view(), name='reviews_update'),
    path('reviews/<int:pk>/delete/',
         views.ReviewDelete.as_view(), name='reviews_delete'),
]
