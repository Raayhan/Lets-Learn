from django.urls import path,include
from course import views


urlpatterns = [
    
    path('latest-categories',views.LatestCategoriesList.as_view()),
    path('categories/<slug:category_slug>/',views.CategoryDetail.as_view()),

    path('all-courses',views.CourseList.as_view()),
]