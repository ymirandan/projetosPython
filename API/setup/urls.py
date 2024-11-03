# criar a url (puxar a view)
#utilizar .\venv\Scripts\Activate.ps1 para ativar venv no terminal

from django.contrib import admin
from django.urls import path, include
#from escola.views import estudantes
from escola.views import EstudantesViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes',EstudantesViewSet,basename='Estudantes')
router.register('cursos',CursoViewSet,basename='Cursos')
router.register('matriculas',MatriculaViewSet,basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('estudantes/', estudantes),
    path('',include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()), #path especifico, por isso adiciona o path. alem disso, diz que é apenas para visualizacao 
    path('cursos/<int:pk>/matriculas/', ListaMatriculaCurso.as_view()), 
]


#objeto da classe routers vai conter todas as rotas (ao inves de usarmos path)