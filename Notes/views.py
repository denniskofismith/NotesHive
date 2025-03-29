from.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Notes

@api_view(["GET","POST"])
def notes(request):
    if request.method == "GET":
        notes = Notes.objects.all()
        serializer = NoteSerializer(notes,many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == "POST":
        print(request.data)
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    
@api_view(['GET','PUT','DELETE'])
def note_details(request,slug):
    
  
    note = get_object_or_404(Notes,slug=slug)
        
    
    if request.method == 'GET':
        
        serializer = NoteSerializer(note)
        
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        
        serializer = NoteSerializer(note,data=request.data)
        
        serializer.is_valid(raise_exception=True)
            
        serializer.save()
            
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
    
    elif request.method == 'DELETE':
        
        note.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        