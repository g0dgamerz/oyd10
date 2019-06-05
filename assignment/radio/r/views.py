from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.
#def data(request):
 #   if request.method=="POST":
  #      form=UserForm(request.POST)
   #     a=form.first
    #    b=form.second
     #   c=form.third
      #  return render(request,'templatea.html',{'a':a,'b':b,'c':c})
   # else:
    #    pass


def home(request):
    return render(request,"index.html")

def final(request):
    value1=request.GET['l1']
    value2=request.GET['l2']
    value3=request.GET['l3']
    if value1 == 'a':
        return render(request,'templatea.html',{'text':value1 + value2 + value3})
    elif value1 == 'b':
        return render(request,'templateb.html',{'text':value1 + value2 + value3})
    elif value1 == 'c':
        return render(request,'templatec.html',{'text':value1 + value2 + value3})


