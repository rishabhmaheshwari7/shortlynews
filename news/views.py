import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
import bs4
import lxml

requests.packages.urllib3.disable_warnings()

def news_list(request):
	headlines = Headline.objects.all()[::-1]
	context = {
		'object_list': headlines,
	}
	#------------------------------------
	#the following code is necessary bcuz it deletes the temporary got news from database
	#otherwise it will just keep on adding in the database
	q=Headline()
	q=Headline.objects.all()
	q.delete()
	#------------------------------------
	return render(request, "news/home.html", context)

def scrape1(request):
	res1 = requests.get('https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en)-IN&gl=IN&ceid=IN%3Aen')
	soup1 = bs4.BeautifulSoup(res1.text)
	ind=soup1.select('h3')
	obe = soup1.find_all("img", class_="tvs3Id QwxBBf")
	ind.reverse() #since last news will be added first on page to counter that we revrese the list
	obe.reverse()
	l1=len(ind)
	for i in range(0,25): #its too many results right now
		#for artcile in News:
		main = "this is main"
		link = "this is link"
		image_src = obe[i].get('src') 
		title = "title"
		new_headline = Headline()
		new_headline.title = ind[i].getText()
		new_headline.url = link
		new_headline.image = image_src
		new_headline.save()
	return redirect("../")


def scrape2(request):
	res2=requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
	soup2 = bs4.BeautifulSoup(res2.text)
	
	world=soup2.select('h3')
	obe1 = soup2.find_all("img", class_="tvs3Id QwxBBf")
	world.reverse() #since last news will be added first on page to counter that we revrese the list
	obe1.reverse()
	l2=len(world)
	for i in range(0,25):
		main = "this is main"
		link = "this is link"
		image_src = obe1[i].get('src') 
		title = "title"
		new_headline = Headline()
		new_headline.title = world[i].getText()
		new_headline.url = link
		new_headline.image = image_src
		new_headline.save()
	return redirect("../")

