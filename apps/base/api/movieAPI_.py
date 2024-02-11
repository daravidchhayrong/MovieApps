from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404

#import rest_framework
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#import Models class
from apps.base.models import Movie

#import Serializer class
from ..serializer import (MovieSerializer)

class MovieAPI(APIView):
    def post(self, request, format=None):
        if isinstance(request.data, list):
            # If it's a list, handle bulk create
            serializer = MovieSerializer(data=request.data, many=True)
        else:
            # If it's not a list, handle single create
            serializer = MovieSerializer(data=request.data)

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
        try:
            queryset = Movie.objects.all()
            serializer = MovieSerializer(queryset, many=True)
            return Response({
                'data': {
                    'results': serializer.data
                }
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'errors': {
                    'devcode': 'ERROR_0002',
                    'text': f'Error while fetching Movies: {str(e)}'
                }
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)