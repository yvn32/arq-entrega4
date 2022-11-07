import http
from tkinter import N
from tkinter.messagebox import NO
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.http import HttpResponse
import requests

# PÁGINA DE INICIO
def inicio(request):
    cuentaLogueada = ""
    try:
        cuentaLogueada = request.session['cuentaLogueada']
        print(cuentaLogueada)
    except:
        print('No se ha logueado ninguna cuenta')
    contexto = {"cuentaLogueada":cuentaLogueada}
    return render(request, "inicio.html", contexto)

# LOGIN
def Login(request):
    if request.user.is_authenticated:
        return render(request, "mantenedor.html")
    else:
        messages.info(request, "Por favor inicia sesión para acceder")
        return HttpResponseRedirect('/')
    
# LOGIN USER
def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/mantenedor')
        else:
            messages.error(request, "Por favor ingresa datos correctos")
            return HttpResponseRedirect('/')

# LOGOUT
def Logout(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('/')
    
# VISUALIZAR PRODUCTOS
def productos(request):
    productos = []
    resp = requests.get('http://127.0.0.1:8000/api/productos/')
    print(resp.status_code)
    if resp.status_code == 200:
        productos = resp.json()
    else:
        print('Error en la busqueda')
    return render(request, 'productos.html', {'productos': productos})

# MANTENEDOR
@login_required(login_url="/login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def mantenedor(request):
    productos = []
    resp = requests.get('http://127.0.0.1:8000/api/productos/')
    print(resp.status_code)
    if resp.status_code == 200:
        productos = resp.json()
    else:
        print('Error en la busqueda')
    return render(request, "mantenedor.html", {'productos': productos})

# CREAR PRODUCTO
def crearProducto(request):
    print('Pendiente armar la función crearProducto')
    return redirect('/mantenedor')

# MODIFICAR PRODUCTO
def modificarProducto(request, id):
    print('Pendiente armar la función modificarProducto')
    return redirect('/mantenedor')

# ELIMINAR PRODUCTO
def eliminarProducto(request, id):
    print('Se eliminará el producto', id)
    requests.delete('http://127.0.0.1:8000/api/productos/{}'.format(id))
    return redirect('/mantenedor')




