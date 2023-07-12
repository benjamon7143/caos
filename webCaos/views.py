from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_aut
import requests
from .carrito import *


# Create your views here.

def index(request):
    cate = Categoria.objects.all()
    contexto={'categoria':cate} 
    noticia=Noticia.objects.reverse()[:2]
    contexto["Noticias"]=noticia
    return render(request, 'index.html',contexto)

def contacto(request):
    return render(request, 'contacto.html')

def login(request): 
    contexto={'mensaje':''}
    if request.POST:
        usua = request.POST.get("txtusu")
        pas = request.POST.get("txtPass")
        us =  authenticate(request,username=usua,password=pas)
        if us is not None and us.is_active:
            login_aut(request,us)
            return render(request,"index.html")
        contexto={'mensaje':'usuario incorrecto'} 
    return render(request, 'login.html', contexto)

def cerrar_sesion(request):
    logout(request)
    return render(request,"index.html")

def registro(request):
    contexto={'mensaje':''}
    if request.POST:
        usua=request.POST.get("txtusuario")
        email=request.POST.get("txtEmail")
        password=request.POST.get("txtcontraseña")
        usu = User()
        usu.username=usua
        usu.email=email
        usu.set_password(password)
        try:
            usu.save()
            contexto['mensaje']='Usuario registrado'
        except:
         contexto['mensaje']='Usuario no registrado'
            
    return render(request,'login.html', contexto)
    
def sobre_nosotros(request):
    return render(request, 'sobre-nosotros.html')

def subir_noticia(request):
    cate=Categoria.objects.all()
    print(request.user.username)
    # nom_user=request.user.username
    # usu=User.objects.get(username=nom_user)
    # print(usu)
    noticia=Noticia.objects.all()
    periodistas=Periodista.objects.all()
    contexto={"Noticias":noticia,"Categoria":cate,"Periodistas":periodistas}
    if request.POST:
        titulo = request.POST.get("txtTitulo")
        descripcion = request.POST.get("txtDesc")
        fecha = request.POST.get("txtFecha")
        cat = request.POST.get("cboCategoria")
        objcat = Categoria.objects.get(IDCate = cat)
        perio = request.POST.get("cboPeriodista")
        objperio= Periodista.objects.get(IDPer = perio)
        imagen = request.FILES.get("txtIMG")
        noti = Noticia(
            Titulo=titulo,
            Descrip=descripcion,
            Fecha=fecha,
            categoria=objcat,
            periodista=objperio,
            Foto=imagen)
        noti.save()
        contexto["Mensaje"]="Enviado"
    return render(request, 'subir-noticia.html',contexto)

def admin_noticias(request):
    cate=Categoria.objects.all()
    noticia=Noticia.objects.all()
    print(request.user.username)
    # nom_user=request.user.username
    # # usu=User.objects.get(username=nom_user)
    # print(usu)
    contexto={"Noticias":noticia,"Categoria":cate}
    return render(request, 'admin-noticias.html', contexto)

def noticia_pandemia(request):
    return render(request, 'noticia-pandemia.html')

def noticia_Uchile(request):
    return render(request, 'noticia-Udechile.html')

def galeria(request):
    noticias = Noticia.objects.filter(Publicado=True)
    cantidad = Noticia.objects.filter(Publicado=True).count()
    contex = {"Noticias":noticias,'cantidad':cantidad}

    return render(request,'galeria.html',contex)
 
def Buscar_Palabra(request):
    palabra = request.POST.get('txtDesc')
    noticia = Noticia.objects.filter(Descrip__contains=palabra)
    cantidad = Noticia.objects.filter(Descrip__contains=palabra).count()
    contex={"Noticias":noticia,'cantidad':cantidad}

    return render(request,'galeria.html',contex)

def Buscar_Categoria(request,id):

    cat = request.POST.get(id)
    cate = Categoria.objects.get(NombreCate= cat)
    noticias = Noticia.objects.filter(categoria=cate)
    contex={"Noticias":noticias}

    return render(request,'galeria.html',contex)

def Buscar(request):
    palabra = request.GET.get('txtbuscar')
    resultado = Noticia.objects.filter(Descrip__contains=palabra)
    contex={"Noticias":resultado}

    return render(request,'buscador.html',contex)

def Buscador(request):

    return render(request,'buscador.html')

def rechazar(request,id):
    noticia = Noticia.objects.get(IDNot=id)
    noticia.delete()
    cate=Categoria.objects.all()
    # nom_user=request.user.username
    # usu=User.objects.get(username=nom_user)
    # print(usu)
    contexto={"Noticias":noticia,"Categoria":cate}
    contexto['mensaje']="rechazado"
    #return render(request,'admin-noticias.html',contexto)
    return redirect('/administrarnoticias/')
    
def modificar(request,id):
    noticia = Noticia.objects.get(IDNot=id)
    cate=Categoria.objects.all()
    periodistas=Periodista.objects.all()
    contexto={"Noticias":noticia,"Categoria":cate,"Periodistas":periodistas}
    return render(request,'modificar.html',contexto) 

def realizar_modificacion(request,id):
    cate=Categoria.objects.all()
    # nom_user=request.user.username
    # usu=User.objects.get(username=nom_user)

    noticia=Noticia.objects.all()
    periodistas=Periodista.objects.all()
    print(periodistas)
    contexto={"Noticias":noticia,"Categoria":cate,"Periodistas":periodistas}
    if request.POST:
        titulo = request.POST.get("txtTitulo")
        descripcion = request.POST.get("txtDesc")
        fecha = request.POST.get("txtFecha")
        cat = request.POST.get("cboCategoria")
        objcat = Categoria.objects.get(IDCate = cat)
        perio = request.POST.get("cboPeriodista")
        objperio= Periodista.objects.get(IDPer = perio)
        imagen = request.FILES.get("txtIMG")
        noti=Noticia.objects.get(IDNot=id)
        noti.Titulo=titulo
        noti.Descrip=descripcion
        noti.Fecha=fecha
        noti.categoria=objcat
        noti.periodista=objperio
        if imagen is not None:
            noti.Foto=imagen
        noti.save()
        contexto["Mensaje"]="Modifico"
    return render(request,'admin-noticias.html',contexto)

###############################

def mercancia(request):
    merca=Mercaderia.objects.all()
    contexto={"Mercaderia":merca}
    return render(request,'mercancia.html',contexto)

def agregar_producto(request,id_producto):
    carrito= Carrito(request)
    merca = Mercaderia.objects.get(IDMerca=id_producto)
    carrito.agregar(merca)
    return redirect('/carrito/')

def restar_producto(request,id_producto):
    carrito= Carrito(request)
    merca = Mercaderia.objects.get(IDMerca=id_producto)
    carrito.resta(merca)
    return redirect('/carrito/')

def carrito(request):
    #merca = Mercaderia.objects.all()
    response = requests.get("http://127.0.0.1:8000/api/mercaderia/")
    merca = response.json() 
    contexto={"Mercaderia":merca}
    return render(request,'carrito.html',contexto)


# alter session set "_oracle_script" = true
# create user caos_news IDENTIFIED BY caosnews account unlock;
# grant RESOURCE, CONNECT, dba to caos_news;

