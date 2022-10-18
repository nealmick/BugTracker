


from . import views

from django.urls import include, path
from .views import BugListView,BugCreateView,CompletedListView

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', BugListView.as_view() , name='home-bugs'),
    path('completed/', CompletedListView.as_view() , name='completed-bugs'),
    path('new/', BugCreateView.as_view(), name='new-bug'),
    path('edit/save/', views.saveBug, name='save-bug'),
    path('edit/<int:pk>', views.editBug, name='edit-bug'),
    path('del/<int:pk>', views.delBug, name='del-bug'),
    path('complete/<int:pk>', views.completeBug, name='complete-bug'),
    path('uncomplete/<int:pk>', views.uncompleteBug, name='uncomplete-bug'),
]
