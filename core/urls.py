from django.http import request
from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('home/', views.HomeListView.as_view()), 
    path('service/', views.ServiceListView.as_view()),
    path('upcomingevent/', views.UpcomingEventListView.as_view()),
    path('structure/', views.StructureListView.as_view()),
    path('po/', views.POListView.as_view()),
    path('ac/', views.ACListView.as_view()),
    path('pmy/', views.PMYListView.as_view()),
    #path('dl/', views.DLListView.as_view()),
    path('nlm/', views.NLMListView.as_view()),
    #path('sbm/', views.SBMListView.as_view()),
    path('uba/', views.UBAListView.as_view()),
    path('awards/', views.AwardsListView.as_view()),
    path('report/', views.ReportListView.as_view()),
    path('activity/', views.ActivityCalendarListView.as_view()),
    path('assets/', views.AssetListView.as_view()),
    path('vt/', views.VTListView.as_view()),
    path('sapling/', views.SaplingListView.as_view()),
    path('bdc/', views.BDCListView.as_view()),
    path('camps/', views.CampListView.as_view()),
    path('seminar/', views.SeminarListView.as_view()),
    path('others/', views.OtherListView.as_view()),
    path('othereventyears/', views.EventYears),
    path('hu/', views.HU.as_view()),
]