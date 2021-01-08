from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    # index,
    # get_category,
    # view_news,
    # add_news,
    HomeNews,
    NewsByCategory,
    ViewNews,
    CreateNews,
    register,
    user_login,
    user_logout,
    # sending_by_email,
)


urlpatterns = [
    # Таким образом кэшируется страница сайта,
    # в представлениях основанные на классах
    # path('', cache_page(60)(HomeNews.as_view()), name='home'),

    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>', NewsByCategory.as_view(),
         name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('sending_by_email/', sending_by_email, name='sending_by_email'),


    # path('', index, name='home'),
    # path('category/<int:category_id>', get_category, name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    # path('news/add-news/', add_news, name='add_news')
]
