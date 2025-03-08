
from django.urls import path
from .views import SkuIndex,dept_by_loc, cat_by_dept_loc,Scat_cat_dep_loc,sub_by_cat_dept_loc


urlpatterns = [
    path('', SkuIndex.as_view()),
    path('<int:loc_id>/Department/', dept_by_loc.as_view()),
    path('<int:loc_id>/Department/<int:dep_id>/category/', cat_by_dept_loc.as_view()),
    path('<int:loc_id>/department/<int:dep_id>/category/<int:cat_id>/subcategory/',Scat_cat_dep_loc.as_view()),
    path('<int:loc_id>/department/<int:dep_id>/category/<int:cat_id>/subcategory/<int:sub_cat_id>/',sub_by_cat_dept_loc.as_view()),
]
