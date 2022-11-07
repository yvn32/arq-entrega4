from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
import json, traceback
from api_compare.persistencia.models import Producto
from rest_framework.response import Response

TEXT_PLAIN = "text/plain"
NOT_FOUND = 'Registro no encontrado'
APPLICATION_JSON = 'application/json'

@api_view(['GET', 'POST', 'PUT'])
def load(request):
    if request.method == 'GET':
        return find_all()      
    elif request.method == 'POST':
        return create(request)
    elif request.method == 'PUT':
        return update(request)

def find_all():
    print('find_all')        
    productos = []
    try:        
        resultado = Producto.objects.all()
        for p in resultado:
            productos.append(p.to_json())
        return create_response(productos, status.HTTP_200_OK, APPLICATION_JSON)
    except Exception:
        traceback.print_exc()
        return productos

def create(request):
    try: 
        print('Estoy en create')
        # Transformar texto json a objeto json en Python
        payload = json.loads(request.body)
        print(payload)
        # Leer atributos de objeto json y dejarlos en variables
        nombre = payload['nombre']
        descripcion = payload['descripcion'] 
        precio = payload['precio']
        preciodcto = payload['preciodcto']
        stock = payload['stock']
        idempresa = payload['idempresa']
        rutaimg = payload['rutaimg']
        # Crear objeto producto de tipo models        
        producto = Producto()
        # Asignar valores de variables a objeto producto
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.preciodcto = preciodcto
        producto.stock = stock
        producto.idempresa = idempresa
        producto.rutaimg = rutaimg
        # Grabar en BD
        producto.save()
        return create_response(producto.to_json(), status.HTTP_201_CREATED, APPLICATION_JSON)     
    except Exception:
        traceback.print_exc()
        return create_response(None, status.HTTP_500_INTERNAL_SERVER_ERROR, TEXT_PLAIN)

def update(request):
    try: 
        print('Estoy en update')
        # Transformar texto json a objeto json en Python
        payload = json.loads(request.body)
        print(payload)
        # Leer atributos de objeto json y dejarlos en variables
        id = payload['id']
        nombre = payload['nombre']
        descripcion = payload['descripcion'] 
        precio = payload['precio']
        preciodcto = payload['preciodcto']
        stock = payload['stock']
        idempresa = payload['idempresa']
        rutaimg = payload['rutaimg'] 
        # Crear objeto producto de tipo models      
        producto = Producto.objects.get(pk=id)
        # Asignar valores de variables a objeto producto
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.preciodcto = preciodcto
        producto.stock = stock
        producto.idempresa = idempresa
        producto.rutaimg = rutaimg
        # Grabar en BD
        producto.save(force_update=True)
        return create_response(producto.to_json(), status.HTTP_200_OK, APPLICATION_JSON)
    except Producto.DoesNotExist:
        return create_response(NOT_FOUND, status.HTTP_404_NOT_FOUND, TEXT_PLAIN)  
    except Exception:
        traceback.print_exc()
        return create_response(None, status.HTTP_500_INTERNAL_SERVER_ERROR, TEXT_PLAIN)

@api_view(['GET', 'DELETE'])
def load_id(request, id):
    print('Estoy en load_id')
    if request.method == 'GET':
        return find_by_id(id)
    if request.method == 'DELETE':
        return delete_by_id(id)

def find_by_id(id):
    print('Estoy en find_by_id: ', id)
    try:
        producto = Producto.objects.get(pk=id)
        print('Producto: ', producto)
        return create_response(producto.to_json(), status.HTTP_200_OK, APPLICATION_JSON)
    except Producto.DoesNotExist:
        return create_response(NOT_FOUND, status.HTTP_404_NOT_FOUND, TEXT_PLAIN)
    except Exception:
        traceback.print_exc()
        return create_response(None, status.HTTP_500_INTERNAL_SERVER_ERROR, TEXT_PLAIN)

def delete_by_id(id):
    print('Estoy en delete_by_id: ', id)
    try:
        producto = Producto.objects.get(pk=id)
        producto.delete()
        return create_response('Registro {} eliminado'.format(id), status.HTTP_200_OK, TEXT_PLAIN)
    except Producto.DoesNotExist:
        return create_response(NOT_FOUND, status.HTTP_404_NOT_FOUND, TEXT_PLAIN) 
    except Exception:
        traceback.print_exc()
        return create_response(None, status.HTTP_500_INTERNAL_SERVER_ERROR, TEXT_PLAIN)  

def create_response(payload, status_code, content_type):
    # Respuesta sin body y solo estatus
    if payload is None:
        return Response(status=status_code)
    # Respuesta con body (payload), status y tipo de dato a responder
    elif content_type is not None:
        return Response(payload, status=status_code, content_type=content_type)
    # Respuesta con body y status
    else:
        return Response(payload, status=status_code)
