# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import *
from tester import *

def index(request):
    return render_to_response("one.html",RequestContext(request))
def two(request):
     data = request.POST.get('data', '')
     if(data):
        sites,measure = detect(data)
     else:
         return HttpResponse("No data was entered. Please enter data to continue.")
     #src = open('C:\Python\Scripts\tester\pools\two.html','r')
     list= zip(sites,measure)   
     t= Template("<div> Results: </div> <ol>{% for item in list %}    <li>{{ item.0 }} - {{ item.1 }}</li>{% endfor %}</ol>")
     c= Context({'list': list},{'text': data})
     res= t.render(c)
     return HttpResponse(res)
     
    
