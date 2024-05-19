from django.urls import path
from .views import SponsorCreatreAPIView, SponsorListAPIView,SponsorUpdateAPIView,StudentDetailAPIView
from .views import StudentSponsorCreatreAPIView, StudentListAPIView, StudentUpdateAPIView,StudentSponsorListAPIView,StatisticAPIView,GraphicAPIView
urlpatterns = [
    path('sponsor-list/', SponsorListAPIView.as_view()),
    path('sponsor-create/', SponsorCreatreAPIView.as_view()),
    path('sponsor-update/', SponsorUpdateAPIView.as_view()),

    path('student-list/', StudentListAPIView.as_view()),
    path('student-list/<int:pk>', StudentDetailAPIView.as_view()),
    path('student-sponsor-create/', StudentSponsorCreatreAPIView.as_view()),
    path('student-update/<int:pk>', StudentUpdateAPIView.as_view()),
    path('student-sponsors/',StudentSponsorListAPIView.as_view()),
    path('statistic-amount/',StatisticAPIView.as_view()),
    path('graphic/',GraphicAPIView.as_view())
]