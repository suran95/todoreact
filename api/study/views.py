from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import api_view, action
# 클래스
from rest_framework.views import APIView
from .models import Students, Scores
from .serializers import StudentSerializer, ScoreSerializer
from rest_framework.response import Response


# viewset으로 만들때
class StudentView(ModelViewSet):

    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name = name)
        return qs 

    @action(detail = False, methods = ['GET'])
    def Guri(self, request):
        qs = self.get_queryset().filter(address__contains = '구리')
        serializer = self.get_serializer(qs, many = True)
        return Response(serializer.data)

    @action(detail = True, methods = ['PUT'])
    def init(self, request, pk):
        instance = self.get_object()
        instance.address = ""
        instance.email = ""
        instance.save(update_fields= ['address', 'email'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ScoreView(ModelViewSet):
    queryset = Scores.objects.all()
    serializer_class = ScoreSerializer

# 클래스로 만들때
# class StudentView(APIView):

#     def get(self, request):
#         qs = Students.objects.all()
#         serializer = StudentSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentDetailView(APIView):
#     def get_object(self, pk):
#         try: student = Students.objects.get(pk=pk)
#         except: raise Http404()
#         return student

#     def get(self, request, pk):
#         student = self.get_object(pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         student = self.get_object(pk)
#         print(request.data)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def delete(self, request, pk):
#         student = self.get_object(pk)
#         student.delete()
#         return Response(status=204)


# class ScoreView(APIView):

#     def get(self, request):
#         qs = Scores.objects.all()
#         serializer = ScoreSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ScoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ScoreDetailView(APIView):
#     def get_object(self, pk):
#         try: score = Scores.objects.get(pk=pk)
#         except: raise Http404()
#         return score

#     def get(self, request, pk):
#         score = self.get_object(pk)
#         serializer = ScoreSerializer(score)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         score = self.get_object(pk)
#         print(request.data)
#         serializer = ScoreSerializer(score, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def delete(self, request, pk):
#         score = self.get_object(pk)
#         score.delete()
#         return Response(status=204)


        

'''
@api_view(['GET', 'POST'])
def StudentView(request):
    if request.method == 'GET':
        qs = Students.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def StudentDetailView(request, id):
    qs = get_object_or_404(Students, pk=id)
    #상세조회
    if request.method == 'GET':
        serializer = StudentSerializer(qs)
        return Response(serializer.data)
    #수정
    elif request.method == 'PUT':
        serializer = StudentSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    #삭제
    elif request.method == 'DELETE':
        qs.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def ScoreView(request):
    if request.method == 'GET':
        qs = Scores.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ScoreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ScoreDetailView(request):
    # qs = get_object_or_404(Scores, pk=id)
   
    if request.method == 'GET':
        serializer = ScoreSerializer(qs)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ScoreSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        qs.delete()
        return Response(status=204)

'''