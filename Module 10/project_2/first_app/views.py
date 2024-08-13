from django.shortcuts import render
import datetime
# Create your views here.
def about(request):
    d = {"author" : "Rahim", "age" : 20, "list" : ["Python","is","best"], "birthday" : datetime.datetime.now(), "Courses" : [
        {
            "id" : 1,
            "name" : "Python",
            "fees" : 5000
        },
        {
            "id" : 2,
            "name" : "Django",
            "fees" : 10000
        },
        {
            "id" : 3,
            "name" : "C",
            "fees" : 1000
        },
    ]}
    return render(request, 'first_app/about.html', d)

def contact(request):
    
    return render(request, 'first_app/contact.html')