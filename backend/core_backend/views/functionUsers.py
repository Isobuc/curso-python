from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core_backend.models import Usuario
from voluptuous.schema_builder import Required
from backend.utils import validateData


@api_view(['GET'])
@permission_classes([AllowAny])
def get_users(request):
    users = Usuario.objects.all()
    response = []
    for user in users:
        response.append({
            'id': user.identificador,
            'nombre': user.nombre,
            'apellido': user.apellido
        })
    return Response(response)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    data = validateData({
        Required('nombre'):str,
        Required('apellido'):str,
        ('identificador'):int,
    }, request.data)
    if 'identificador' not in data:
        data['identificador'] = data['id'] + 1000
    if Usuario.objects.filter(identificador=data['identificador']).exists():
        data['identificador'] = data['identificador'] + 1000
    if data['identificador'] > 9999:
        data['identificador'] = data['identificador'] - 1500
    user = Usuario.objects.create(nombre=data['nombre'], apellido=data['apellido'], identificador=data['identificador'])
    user.save()
    return Response('Usuario creado exitosamente')

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_user(request):
    data = validateData({
        Required('identificador'):int,
        ('nombre'):str,
        ('apellido'):str,
        ('nuevo_identificador'):int,
    }, request.data)
    try:
        user = Usuario.objects.get(identificador=data['identificador'])
        if 'nombre' in data:
            user.nombre = data['nombre']
        if 'apellido' in data:
            user.apellido = data['apellido']
        if 'nuevo_identificador' in data:
            user.identificador = data['nuevo_identificador']
        user.save()
        return Response('Usuario actualizado exitosamente')
    except:
        return Response('Usuario no encontrado')
    
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_user(request):
    data = validateData({
        Required('identificador'):int,
    }, request.data)
    try:
        user = Usuario.objects.get(identificador=data['identificador'])
        user.delete()
        return Response('Usuario eliminado exitosamente')
    except:
        return Response('Usuario no encontrado')
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_user(request):
    data = validateData({
        Required('identificador'):int,
    }, request.data)
    try:
        user = Usuario.objects.get(identificador=data['identificador'])
        return Response({
            'id': user.identificador,
            'nombre': user.nombre,
            'apellido': user.apellido
        })
    except:
        return Response('Usuario no encontrado')