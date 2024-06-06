from django.urls import path,include,re_path
from .views import *
urlpatterns = [
	 path('photo/', PhotoViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='photo_list'),
	 path('photo/<int:pk>/', PhotoViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='photo_detail'),
	 path('music/', MusicViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='music_list'),
	 path('music/<int:pk>/', MusicViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='music_detail'),
	 path('time/', TimeViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='time_list'),
	 path('time/<int:pk>/', TimeViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='time_detail'),
	 path('guest/', GuestViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='guest_list'),
	 path('guest/<int:pk>/', GuestViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='guest_detail'),
]