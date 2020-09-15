from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('students', views.StudentView) 
router.register('scores', views.ScoreView)

urlpatterns = [
    path('', include(router.urls))

    # 클래스로 만드는거
    # path('students', views.StudentView.as_view()),
    # path('students/<pk>', views.StudentDetailView.as_view()),
    # path('scores', views.ScoreView.as_view()),
    # path('scores/<pk>', views.ScoreDetailView.as_view()),
    # path('students/', views.StudentView),
    # path('students/<id>', views.StudentDetailView),
    # path('scores/', views.ScoreView),
    # path('scores/', views.ScoreDetailView)
]

