from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('watches/', views.watches_index, name='index'),
    path('watches/<int:watch_id>/', views.watches_detail, name='detail'),
    path('watches/create/', views.WatchCreate.as_view(), name='watches_create'),
    path('watches/<int:pk>/update/', views.WatchUpdate.as_view(), name='watches_update'),
    path('watches/<int:pk>/delete/', views.WatchDelete.as_view(), name='watches_delete'),
    path('watches/<int:watch_id>/add_service/', views.add_service, name='add_service'),
    # path('watches/<int:watch_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
    # path('watches/<int:watch_id>/unassoc_accessory/<int:accessory_id>/', views.unassoc_accessory, name='unassoc_accessory'),
    path('accessorys/', views.AccessoryList.as_view(), name='accessorys_index'),
    path('accessorys/<int:pk>/', views.AccessoryDetail.as_view(), name='accessorys_detail'),
    path('accessorys/create/', views.AccessoryCreate.as_view(), name='accessorys_create'),
    path('accessorys/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessorys_update'),
    path('accessorys/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessorys_delete'),
]