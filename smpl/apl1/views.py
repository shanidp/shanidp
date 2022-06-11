from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import student,register,login
from django.contrib.auth.models import User,auth
# Create your views here.
def myfun(request):
    return render(request,'aut.html')

def myfun2(request):
    if request.method == 'POST':
        x = int(request.POST['n1'])
        y = 1
        for i in range(1,x+1):
            y = y * i
        return render(request,'myfun.html', {'x1' : x , 'x2' : y })
def myfun3(request):
    if request.method == 'POST':
        a = request.POST['r1']
        b = ""
        count = len(a)
        while count>0:
            b += a[count - 1]
            count=count-1
        return render(request,'myfun.html',{'y1':a,'y2':b})
def myfun4(request):
    return redirect(myfun)
def myfun5(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        if(a>=b)and(a>=c):
            large=a;
        elif (b>=a)and(b>=c):
            large=b;
        else:
            large=c;
            return render(request,'myfun.html',{'a1':a,'a2':b,'a3':c,'a4':large})
def myfun6(request):
    if request.method == 'POST':
        a= int(request.POST['n1'])
        if a %2==0:
            a='even'
        else:
            a='odd'
    return render(request,'myfun.html',{'a1':a})
def myfun8(request):
    if request.method == 'POST':
        a= request.POST['v1']
        b = request.POST['v2']
        c = request.POST['v3']
        d = request.POST['v4']
        l=[]
        l.append(a)
        l.append(b)
        l.append(c)
        l.append(d)
        return render(request,'mf4.html',{'x':l})
def register1(request):
    if request.method=='POST':
        a= request.POST['y1']
        b = request.POST['y2']
        c = request.POST['y3']
        d=request.FILES['y4']
        data=student(roll=a,name=b,age=c,image=d)
        data.save()
        return HttpResponse("created")
def diplay(request):
    if request.method=='GET':
        data = student.objects.all()
        return render(request,'diplay.html',{'r':data})
def reg1(request):
    if request.method=='GET':
        data = student.objects.all()
        return render(request,'reg.html',{'r':data})
def reg2(request):
    if request.method=='POST':
        a=request.POST['v1']
        b=student.objects.filter(roll=a)
        return render(request,'update.html',{'r':b})
def update(request):
    if request.method=='POST':
        a=request.POST['x1']
        b=request.POST['x2']
        c=request.POST['x3']
        student.objects.filter(roll=a).update(name=b,age=c)
        return HttpResponse("updated")
def reg3(request):
    if request.method=='POST':
        a=request.POST['h1']
        b=student.objects.filter(roll=a)
        b.dalete()
        return HttpResponse("deleted")
def reglo(request):
    if request.method=='POST':
        w = request.POST['a1']
        x = request.POST['a2']
        y = request.POST['a3']
        z = request.POST['a4']
        u = request.POST['a5']
        p = request.POST['a6']
        data=register(rol=w,name=x,age=y,salary=z)
        data.save()
        data1=login(use=u,pswd=p)
        data1.save()
        return HttpResponse("Done")
def home(request):
    if request.method=='GET':
        re = register.objects.all()
        lo=login.objects.all()
        return render(request,'home.html',{'d':re,'e':lo})
def log(request):
    if request.method=='POST':
        u = request.POST['c1']
        p = request.POST['c2']
        data = login.objects.get(use=u)
        if data.pswd == p:
            request.session['id']=u
            return redirect(profile)
        else:
            return HttpResponse("u/p incurrect")
    else:return render(request,'reglo.html')

def reset(request):
    if request.method=='POST':
        a = request.POST['z1']
        b = login.objects.filter(use=a)
        if b.use == a :
            return render(request,'chps.html',{'g':b})
        else:
            HttpResponse("invalid user name")

def rest(request):
    if request.method=='POST':
        m = request.POST['j1']
        o = request.POST['j2']
        k = request.POST['j3']
        login.objects.filter(use=m).update(use=k,pswd=o)
        return HttpResponse("updated")
def profile(request):
    if 'id' in request.session:
        return render(request,'profile.html')
    else:
        return redirect(lgn)
def regi(request):
    return render(request,'reglo.html')


def lt(request):
    if 'id' in request.session:
        request.session.flush()
    return redirect(lgn)
def rgstr(request):
    if request.method=='POST':
        w = request.POST['m1']
        x = request.POST['m2']
        y = request.POST['m3']
        u = request.POST['m4']
        p = request.POST['m6']
        data = User.objects.create_user(first_name=w,last_name=x,email=y,username=u,password=p)
        data.save()
        return HttpResponse("created")
def lgn(request):
    if request.method=='POST':
        u=request.POST['k1']
        p = request.POST['k2']
        user=auth.authenticate(username=u,password=p)
        if user is not None:
            auth.login(request,user)
            request.session['id'] = u
            return redirect(profile)
        else:
            return  HttpResponse("Invalid")
    else:
        return render(request,'aut.html')
