from django.urls import path
from.import views 

urlpatterns = [
    path("",views.index),
    path("ragistration/",views.ragistration),
    path("table/",views.table),
    path("delete/<int:pk>/",views.userdelete,name="delete"),
    path("update/<int:uid>/",views.update_detials,name="update"),
    path("userupdate/",views.update_view)
    ]
