from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404

#import rest_framework
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#import Models class
from apps.base.models.movie_ import Actor

#import Serializer class
from ..serializer.movieSerializer_ import (ActorSerializer)

class ActorAPI(APIView):
    def post(self, request, format=None):
        if isinstance(request.data, list):
            # If it's a list, handle bulk create
            serializer = ActorSerializer(data=request.data, many=True)
        else:
            # If it's not a list, handle single create
            serializer = ActorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'messages': {
                    'devcode': 'ACTOR_POST',
                    'text': 'ACTORS added successfully'
                }
            }, status=status.HTTP_201_CREATED)
        return Response({
            'errors': {
                'devcode': 'ERROR_0001',
                'text': 'Error while adding new Actors',
                'validations': serializer.errors
            }
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        queryset = Actor.objects.all()
        serializer = ActorSerializer(queryset, many=True)
        return Response({
        'data': {
        'results' : serializer.data
        }

        },status=status.HTTP_200_OK)