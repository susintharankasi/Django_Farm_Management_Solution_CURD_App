from django.urls import path
from . import views

app_name = 'fmsapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index' ),
    path("dashboard/", views.Dashboard.as_view(), name="dashboard"),
    path('administrator/login/', views.Login.as_view(), name='login'),
    path('administrator/register/', views.Register.as_view(), name='register'),
    path("dashboard/logout/", views.Logout.as_view(), name="logout"),
    path("dashboard/administrator/edit/<int:pk>/", views.AccountUpdate.as_view(), name="account_update"),


   #Livestock Routes

   path("dashboard/livestock/new", views.LiveAdd.as_view(), name="create_livestock"),
   path("dashboard/livestock/", views.LiveList.as_view(), name="all_livestock"),
   path("dashboard/livestock/<int:pk>/edit/", views.LiveEdit.as_view(), name="live_edit"),
   path("dashboard/livestock/<int:pk>/delete/", views.LiveDestroy.as_view(), name="live_delete"),
   path("dashboard/livestock/<int:pk>/single/",views.livestockdata, name="livestock_single"),

   #DepStock Routes

   path("dashboard/depstock/new/",views.DepstockNew.as_view(), name="create_deptstock"),
   path("dashboard/depstock/<int:pk>/single/",views.DepstockDetail.as_view(), name="deptstock_single"),
   path("dashboard/depstock/<int:pk>/edit/",views.DepstockUpdate.as_view(), name="deptstock_edit"),
   path("dashboard/depstock/<int:pk>/delete/",views.DepstockDestroy.as_view(), name="deptstock_delete"),
   path("dashboard/depstock/", views.DepstockView.as_view(), name="all_stock"),


   #LiveFarmstock Routes

   path("dashboard/livefarmstock/new", views.LivefarmAdd.as_view(), name="create_livefarmstock"),
   path("dashboard/livefarmstock/", views.LivefarmList.as_view(), name="all_livefarmstock"),
   path("dashboard/livefarmstock/<int:pk>/edit/", views.LivefarmEdit.as_view(), name="livefarm_edit"),
   path("dashboard/livefarmstock/<int:pk>/delete/", views.LivefarmDestroy.as_view(), name="livefarm_delete"),
   path("dashboard/livefarmstock/<int:pk>/single/",views.livefarmdata, name="livefarmstock_single"),

   #FarmStock Routes

   path("dashboard/farmstock/new/",views.FarmstockNew.as_view(), name="create_farmstock"),
   path("dashboard/farmstock/<int:pk>/single/",views.FarmstockDetail.as_view(), name="farmstock_single"),
   path("dashboard/farmstock/<int:pk>/edit/",views.FarmstockUpdate.as_view(), name="farmstock_edit"),
   path("dashboard/farmstock/<int:pk>/delete/",views.FarmstockDestroy.as_view(), name="farmstock_delete"),
   path("dashboard/farmstock/", views.FarmstockView.as_view(), name="all_farmstock"),

]
