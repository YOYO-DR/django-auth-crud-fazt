from django.shortcuts import render, redirect
#lib para crear formulario para la creacion de un usuario
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
#el login no crea un usuario, esto crea las cookies para el inicio de sesión
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError

def home(request):
  return render(request,'home.html')

def signup(request):
  if request.method == 'GET':
    #si el metodo es get, le paso el formulario
    return render(request,'signup.html',{
    'form': UserCreationForm
  })
  else:
    #comparo las contraseñas recibidas
    if request.POST['password1']==request.POST['password2']:
      # registrando usuario
      #esto crea un usuario, y tambien cifra la contraseña pero todavia no lo guarda en la base de datos
      try:
        user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
      #asi ya lo guarda
        user.save()
        #despues de guardar el usuario, al login (para que guarde las credenciales o cookies en el navegador, le paso a la funcion login, el request y el usuario/objeto que cree)
        login(request,user)
        #lo redirecciono a la url con ese 'name'
        return redirect('tasks')
      
      except IntegrityError:
        #asi más manejo errores más especificos, los de Integrity son errores con la base de datos
        return render(request,'signup.html',{
    'form': UserCreationForm,
    'error':'El usuario ya existe'
  })
    else:
      return render(request,'signup.html',{
    'form': UserCreationForm,
    'error':'La contraseña no coinciden'
  })

def tasks(request):
  return render(request,'tasks.html')

def signout(request):
  logout(request) #con esto cerro la sesión
  return redirect('home')

def signin(request):
  if request.method=='GET':
    return render(request,'signin.html',{
    #Para iniciar sesion
    'form': AuthenticationForm
  })
  else:
    user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
    #si no encontro nada (usuario no existe o contraseña incorrecta)
    if user == None:
      return render(request,'signin.html',{
    #Para iniciar sesion
    'form': AuthenticationForm,
    'error':'Usuario o contraseña incorrectos'
  })
    else:
      #antes de mandarlo a tasks porque el usuario si existe, creo la sesión
      login(request,user)
      return redirect('tasks')