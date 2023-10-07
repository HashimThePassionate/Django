from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
multiString ="""One
two
three
four"""
def home(request):
    name = "muhammad Hashim"
    age = 20
    list1 = [1,2,3]
    list2 = [4,5,6]
    django = "I'm using django"
    dj = "Django"
    nick = "MUHAMMAD"
    D = datetime.now()
    value = 123456789
    f = 34.23234
    messages = 1
    welcome = "&quotWelcome&quot to &#x27;&ltDjango&gt;&#x27; Programming"
    list3 = [  {"name": "Zahid", "age": 19},{"name": "Ahmed", "age": 22},{"name": "Jamshed", "age": 31},]
    list4 = ["Hashim","Juniad","Usman","Zahid"]
    cities = [
    {"name": "Mumbai", "population": "19,000,000", "country": "India"},
    {"name": "Calcutta", "population": "15,000,000", "country": "India"},
    {"name": "New York", "population": "20,000,000", "country": "USA"},
    {"name": "Chicago", "population": "7,000,000", "country": "USA"},
    {"name": "Tokyo", "population": "33,000,000", "country": "Japan"}]
    coach_list = [
        {
            'name': 'junaid',
            'athletes': [
                {'name': 'Hassan'},
                {'name': 'Hamza'},
                {'name': 'Zubair'},
            ]
        },
        {
            'name': 'Jamshed',
            'athletes': [
                {'name': 'Ehtisham'},
                {'name': 'Ahsan'},
                {'name': 'Zeeshan'},
            ]
        },
    ]
    d = {'name':name, 'age':age, 'list1':list1, 'list2':list2, 'django':django, 'dj':dj, 'D':D,'list3':list3,'value':value, 'f':f, "m":multiString, 'nick':nick, 'messages': messages , 'w':welcome, 'nl':list4, 'cities':cities,'c':coach_list}
    return render(request, 'SimpleApp/index.html', d)