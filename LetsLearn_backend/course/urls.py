from django.urls import path,include
from course import views


urlpatterns = [
    
    path('latest-categories',views.LatestCategoriesList.as_view()),
    path('categories/<slug:category_slug>/',views.CategoryDetail.as_view()),


    path('all-courses',views.CourseList.as_view()),
    path('courses/<slug:category_slug>/<slug:course_slug>',views.CourseDetail.as_view()),
    path('courses/<slug:category_slug>/<slug:course_slug>/enrollment',views.GetEnrollment.as_view()),
]