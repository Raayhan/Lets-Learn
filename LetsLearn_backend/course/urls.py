from django.urls import path,include
from course import views


urlpatterns = [
    
    path('latest-categories',views.LatestCategoriesList.as_view()),
]