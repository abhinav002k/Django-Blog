from django.shortcuts import render,redirect
from .models import Emp,Blog,Comment
# Create your views here.

def index(request):
    if request.session.get('is_login'):
        return redirect('/second')

    if request.POST:
        n=request.POST['name']
        e = request.POST['email']
        p = request.POST['password']
        num = request.POST['number']
        pin = request.POST['pCode']
        g = request.POST['gender']
        add = request.POST['address']
        hob = request.POST['hobbey']
        state = request.POST['state']
        uname = request.POST['uname']
        dob = request.POST['dob']
        obj=Emp(name=n, email=e, password=p, number=num, pCode=pin, gender=g, address=add, hobbey=hob, state=state, uname=uname, dob=dob)
        obj.save()
        request.session['regi'] = True
        request.session['name'] = n
        request.session['number'] = num
        request.session['pCode'] = pin
        request.session['address'] = add
        return redirect('/login')
    return render(request, "hello.html")
def second(request):
    data = Blog.objects.all
    return render(request, "second.html", {"data": data})

def update(request,id):
    data=Emp.objects.get(id=id)
    if request.POST:
        n=request.POST['name']
        e = request.POST['email']
        p = request.POST['password']
        num = request.POST['number']
        pin = request.POST['pCode']
        g = request.POST['gender']
        add = request.POST['address']
        hob = request.POST['hobbey']
        state = request.POST['state']
        obj=Emp(name=n, email=e, password=p, number=num, pCode=pin, gender=g, address=add, hobbey=hob,state=state,id=id)
        obj.save()
        return redirect('/second')
    return render(request, "update.html", {"data": data})

def delete(request,id):
    Emp.objects.get(id=id).delete()
    return redirect('/second')

def login(request):
    if request.POST:
        if request.session.get('is_login'):
            return redirect('/second')
        e = request.POST['email']
        p = request.POST['password']

        count=Emp.objects.filter( email=e, password=p).count()

        if count>0:
            request.session['is_login'] = True
            request.session['email'] = e

            return redirect('/second')

    return render(request, "login.html")

def createPost(request):
    if request.POST:
        postby = request.POST['postby']
        title = request.POST['title']
        desc = request.POST['desc']
        image = request.FILES['image']
        obj= Blog(postby=postby, desc=desc, title=title, image=image)
        obj.save()
        return redirect('/second')

    return render(request, "createPost.html")


def readMore(request,id):
    email=request.session.get('email')
    data = Blog.objects.get(id=id)
    if request.POST:
        msg = request.POST['msg']
        obj = Comment(msg=msg)
        obj.cid_id=id
        obj.save()
    data1 = Comment.objects.filter(cid=id)
    return render(request, "readMore.html", {"data": data, "data1": data1, "e": email})


def logout(request):
    del request.session['is_login']
    return redirect('/login')

def aboutUs(request):
    return render(request, "aboutUs.html")

def profile(request):
    if request.POST:
        n = request.POST['name']
        num = request.POST['number']
        pin = request.POST['pCode']
        add = request.POST['address']
        Emp.objects.filter(name=n, number=num, pCode=pin, address=add)
    return render(request, "profile.html")


