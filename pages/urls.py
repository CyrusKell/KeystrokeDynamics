from django.urls import path

from . import views

urlpatterns = [
    path('', views.instructions, name='instructions'),
    path('test1', views.test1, name='test1'),
    path('test1error', views.test1error, name='test1error'),
    path('test2', views.test2, name='test2'),
    path('test3', views.test3, name='test3'),
    path('test4', views.test4, name='test4'),
    path('test5', views.test5, name='test5'),
    path('test6', views.test6, name='test6'),
    path('register', views.register, name='register'),
    path('selftest1', views.selftest1, name='selftest1'),
    path('selftest2', views.selftest2, name='selftest2'),
    path('selftest3', views.selftest3, name='selftest3'),
    path('selftest4', views.selftest4, name='selftest4'),
    path('selftest5', views.selftest5, name='selftest5'),
    path('selftest6', views.selftest6, name='selftest6'),
    path('completed', views.completed, name='completed')
]
