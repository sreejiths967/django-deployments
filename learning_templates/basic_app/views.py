from django.shortcuts import render,HttpResponse,reverse,redirect
from basic_app.forms import UserForm,UserProfileForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
# Create your views here.


def index(request):
    filters={'text':"Hello World",'number':100}
    return render(request,'basic_app/index.html',filters)


def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url.html')


def register(request):

    registered=False
    
    if request.method =='POST':
        

        userform=UserForm(data=request.POST)
        userprofile=UserProfileForm(data=request.POST)
        print("heLooo daaa ithu",userform.is_valid(),"ithum noku",userprofile.is_valid())
        if userform.is_valid() and userprofile.is_valid():
           
            user=userform.save()
            user.set_password(user.password)
            user.save()

            profile=userprofile.save(commit=False)
            print("here")
            profile.user=user

            if 'profile_pic' in request.FILES:

                print("Found")
                profile.profile_pic=request.FILES['profile_pic']
            else:
                print("Not found")

            profile.save()
            registered=True
        else:
            print("errorrs daaa")
            print(userform.errors,userprofile.errors)

        


        
    else:
        userform=UserForm()
        userprofile=UserProfileForm()
        
    return render(request,'basic_app/registration.html',{'form1':userform,'form2':userprofile,'registered':registered})

def user_login(request):


    if request.method == 'POST':

        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("User Not active")


        else:
            print("Somone tried login and filed")
            print("Username={} \n Password={}".format(username,password))
            return HttpResponse("Inavlid Credentials")

    else:
        return render(request,'basic_app/login.html')

@login_required
def special(request):

    return HttpResponse("You are logged in")



@login_required
def user_logout(request):

    logout(request)
    return redirect('/')

    
