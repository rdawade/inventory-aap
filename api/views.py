from django.http import JsonResponse
from rest_framework import serializers
from rest_framework import request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializer import ProductSerializer
from dashboard.models import Product,Order

# @api_view(['GET'])
# def getProducts(request):
#     routes = {
#         'GET':'/api-auth',
#         'GET':'api/dashboard/id',
#         'POST':'api/dashboard/id',

#         'POST':'api/users/token',
#         'POSt':'api/users/token/refresh',
#     }
#     return Response(routes,safe=False)

@api_view(['GET'])
def getProducts(request): 
    projects = Product.objects.all()
    print(projects)
    serializer = ProductSerializer(projects,many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteProduct(request,pk):
    print("ggggggggggggggggggggggggggggggg")
    print(request.data)
    # productId = request.data['product']
    project = Product.objects.get(id=pk)
    project.delete()
    return {'success':"deleted sucecssfully"}

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateProduct(request,pk):
    project = Product.objects.get(id=pk)
    user = request.Product
    data = request.data

    review,created = Product.objects.get_or_create(
        owner = Product,
        project = project,
        
    ) 

    review.value = data['value']
    review.save()
    project.getVoteCount 


    serializer = ProductSerializer(project,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']


    project = Product.objects.get(id=projectId)

    
    return Response('Tag was deleted!')

