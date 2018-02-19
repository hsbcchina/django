from django.shortcuts import render
from django.template.context_processors import request
from future.backports.http.cookiejar import request_host
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    if request.method=='POST':
        u_name=request.POST.get('username','')
        p_word=request.POST.get('password','')
    elif request.method=='GET':
        return render(request, 'login.html',{'emsg':'用户名或密码错误'})






