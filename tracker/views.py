from django.shortcuts import render
import COVID19Py,requests,time

covid19 = COVID19Py.COVID19()

def world(request):
	locations = covid19.getLocations(rank_by='confirmed')
	latest=covid19.getLatest()
	params={
		'world':locations,
		'latest':latest,
	}
	return render(request,'world.html',params)


def india(request):
	url="https://api.covid19india.org/data.json"
	r = requests.get(url)
	k=r.json()
	listt=[]
	for i in k['statewise']:
		list1=[]
		list1.append(i['state'])
		list1.append(i['confirmed'])
		list1.append(i['active'])
		list1.append(i["recovered"])
		list1.append(i['deaths'])
		listt.append(list1)
	indian_confirmed=listt[0][1]
	indian_active=listt[0][2]
	indian_recovered=listt[0][3]
	indian_deaths=listt[0][4]
	params={
		'states':listt,
		'indian_confirmed':indian_confirmed,
		'indian_active':indian_active,
		'indian_recovered':indian_recovered,
		'indian_deaths':indian_deaths,
	}
	return render(request,'india.html',params)

def helpline(request):
	return render(request,'helpline.html')

def home(request):
	return render(request,'home.html')

def donate(request):
	return render(request,'donate.html')