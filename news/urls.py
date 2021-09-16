from django.urls import path
from news.views import scrape1,scrape2, news_list

urlpatterns = [
	path('scrape1/', scrape1, name="scrape1"),
	path('scrape2/', scrape2, name="scrape2"),
	path('', news_list, name="home"),
]