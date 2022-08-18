#from django.conf.urls import url
from django.urls import path
from tutorials import views

urlpatterns = [
    path('api/tutorials', views.tutorial_list),
    path('api/tutorials/<int:tutorial_id>/', views.tutorial_detail),
    path('api/tutorials/published', views.tutorial_list_published),
    path('api/books', views.get_books),
    path('api/book/add', views.add_book),
    path('api/book/update/<int:book_id>', views.update_book),
    path('api/book/delete/<int:book_id>', views.delete_book),
]
