#criar um get (no momento que a pessoa entrar, pedir informação pra ela)
#from django.http import JsonResponse

#def estudantes(request):
 #   if request.method == 'GET':
  #      estudante = {
   #         'id': '1',
    #        'nome': 'lais',
     #   }
      #  return JsonResponse(estudante)

#transformar esse requeste no Json

from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser #adicionar autentificacao nas classes, para pessoas especificas alterarem o BD

class EstudantesViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class =  CursoSerializer

#temos viewsets (antes eram models) com info de modelos e serializers. vamos visualizar tudo o que é imputado na API

class MatriculaViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Matricula.objects.all()
    serializer_class =  MatriculaSerializer

class ListaMatriculaEstudante(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']) #puxar o id do estudante
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk']) #puxar o id do curso
        return queryset
    serializer_class = ListaMatriculasCursoSerializer    