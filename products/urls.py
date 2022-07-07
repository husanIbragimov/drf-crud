from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('list/', views.ProductListAPIView.as_view()),
    path('create/', views.ProductCreateAPIView.as_view()),
    path('list-create/', views.ProductListCreateAPIView.as_view()),
    path('retrieve/<int:pk>/', views.ProductRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>/', views.ProductUpdateAPIView.as_view()),
    path('retrieve-update/<int:pk>/', views.ProductRetrieveUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', views.ProductDestroyAPIView.as_view()),
    path('retrieve-destroy/<int:pk>/', views.ProductRetrieveDestroyAPIView.as_view()),
    path('rud/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='rud-view'),
    # other project
    path('daily-products/', views.DailyProduct.as_view()),
    # mixins
    path('my-mixin-list/', views.MyListMixin.as_view()),
    # Token
    path('auth/token/', obtain_auth_token),
    # view-sets
    path('vs/', include('products.routers'))

]
