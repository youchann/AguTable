from django.urls import path
from . import views
from django.conf.urls import url
from table.views import SampleTemplate,TableList,TableUpdate,TableDelete 


app_name = 'table'

urlpatterns = [
    path('', SampleTemplate.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('tablelist/<int:week>/<int:time>/', TableList.as_view(), name='list'),
    path('update/<int:id>/<int:week>/<int:time>/<int:classid>/', TableUpdate.as_view(), name='update'),
    path('delete/<int:id>/<int:week>/<int:time>/', TableDelete.as_view(), name='delete'),
    # url(r'^update/$',TableUpdate.as_view(), name='update'),
    # path('create/<int:pk>/', views.TableCreate.as_view(), name='create'),
    # path('update/<int:pk>/', views.TableUpdate.as_view(), name='update'),
    # path('delete/<int:pk>/', views.TableDelete.as_view(), name='delete'),
]
