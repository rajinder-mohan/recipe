from django.urls import path
from .views import SignUpView, RecipeListCreateView, RecipeDetailView, CategoryListCreateView, CategoryDetailView ,ReviewListCreateView, ReviewDetailView, RecipeSearchView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('recipes/', RecipeListCreateView.as_view(), name='recipe_list_create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review_list_create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('search/', RecipeSearchView.as_view(), name='recipe_search'),
]