from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = 'blog'

urlpatterns = [
    #url(r'^$', views.list_post, name='list_post'),
    path('', views.PostListView.as_view(), name='list_post'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.PostDetailView.as_view(), name='post_detail'),
    path('categories/', views.CategoryListView.as_view(), name='list_category'),
    path('categories/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_details'),
    path('<int:post_id>/share/', views.PostShareView.as_view(), name='post_share'),
]