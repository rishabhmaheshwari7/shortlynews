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
	# session = requests.Session()
	# session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
	# url = "https://www.theonion.com/"

	# content = session.get(url, verify=False).content
	# soup = BSoup(content, "html.parser")
	# News = soup.find_all('div', {"class":"curation-module__item"})
	res1 = requests.get('https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en)-IN&gl=IN&ceid=IN%3Aen')
	soup1 = bs4.BeautifulSoup(res1.text)
	ind=soup1.select('h3')
	ind.reverse() #since last news will be added first on page to counter that we revrese the list
	l1=len(ind)
	for i in range(0,int(60)): #its too many results right now
		#for artcile in News:
		main = "this is main"
		link = "this is link"
		image_src = "https://www.google.com/search?q=dog+image&rlz=1C1CHBF_enIN748IN749&tbm=isch&source=iu&ictx=1&fir=wzRcY9R2ANhK-M%252C2r6Arj4-hBjhNM%252C_&vet=1&usg=AI4_-kQbPIKZLBKrUZUUeg-qSC-u-gUmkg&sa=X&ved=2ahUKEwiywYKV0IHzAhUFheYKHXp4CAoQ9QF6BAgQEAE#imgrc=wzRcY9R2ANhK-M"
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
	world.reverse() #since last news will be added first on page to counter that we revrese the list
	l2=len(world)
	for i in range(0,(60)):
		main = "this is main"
		link = "this is link"
		image_src = "https://www.google.com/search?q=dog+image&rlz=1C1CHBF_enIN748IN749&tbm=isch&source=iu&ictx=1&fir=wzRcY9R2ANhK-M%252C2r6Arj4-hBjhNM%252C_&vet=1&usg=AI4_-kQbPIKZLBKrUZUUeg-qSC-u-gUmkg&sa=X&ved=2ahUKEwiywYKV0IHzAhUFheYKHXp4CAoQ9QF6BAgQEAE#imgrc=wzRcY9R2ANhK-M"
		title = "title"
		new_headline = Headline()
		new_headline.title = world[i].getText()
		new_headline.url = link
		new_headline.image = image_src
		new_headline.save()
	return redirect("../")

