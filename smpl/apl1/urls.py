
from django.urls import path
from .import views
urlpatterns = [
    path('',views.profile),
    path('h1',views.myfun8),
    path('reg',views.register1),
    path('diplay',views.diplay),
    path('reg1',views.reg1),
    path('reg2',views.reg2),
    path('upd',views.update),
    path('reg3',views.reg3),
    path('home',views.home),
    path('rl',views.reglo),
    path('lo',views.log),
    path('ch',views.rest),
    path('re', views.reset),
    path('lt',views.lt),
    path('au',views.rgstr),
    path('at',views.lgn),
    path('lt',views.profile)

    # path('mf1',views.myfun3),
    # path('mf2',views.myfun4),
    # path('x1',views.myfun5),
    # path('x2',views.myfun6),
]
