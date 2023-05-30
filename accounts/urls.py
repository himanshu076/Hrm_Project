from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# from rest_framework.routers import DefaultRouter


from accounts import views

app_name = "accounts"


# user_list = views.UserModelApiView.as_view({
#     'get': 'list'
# })
# user_detail = views.UserModelApiView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'post': 'create',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })


# user_create = views.UserModelApiView.as_view({
#     'get': 'list'
# })

# user_update = views.UserModelApiView.as_view({
#     'get': 'retrieve'
# })

# user_partial_update = views.UserModelApiView.as_view({
#     'get': 'retrieve'
# })

# user_dele = views.UserModelApiView.as_view({
#     'get': 'retrieve'
# })

urlpatterns = [
    # path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('user/', views.UserModelApiView.as_view(), name='user'),
    path('user/<int:pk>', views.UserModelApiView.as_view(), name='user_details'),

]

# router = DefaultRouter()

# router.register('user', views.UserModelViewSet.as_view(), basename='user')