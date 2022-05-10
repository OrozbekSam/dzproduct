from django.urls import path, include

from main import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    path('users/register/', views.UserRegistrationView.as_view()),
    path('users/logout/', views.CustomLogoutView.as_view()),
    path('users/rest_auth/', include('rest_auth.urls')),

    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('products/create/', views.ProductCreateView.as_view()),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('products/delete/<int:pk>', views.ProductDeleteView)
]