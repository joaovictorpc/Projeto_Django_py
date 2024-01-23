from django.shortcuts import redirect, render
from django.http import HttpResponse
from teste.forms import AlunoForm,CursoForm
from teste.models import Aluno, Cursos
# Create your views here.
def index (request):
    return render(request,'inicio.html')

def listar_Aluno(request):
     alunos = Aluno.objects.all().order_by('id') 
     return render(request,'listar_aluno.html',
                  {'alunos': alunos}) 

def Listar_Cursos(request):
     cursos = Cursos.objects.all()
     return render(request,'listar_cursos.html',
                   {'cursos': cursos})
def incluirAluno(request):
    if request.method == 'POST':
       form = AlunoForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('listar_alunos')
    else:
        form = AlunoForm()   
    return render(request, 'incluir_aluno.html',
                  {'form': form})
def editarAluno(request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(instance=aluno)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
        
    return render(request,'incluir_aluno.html',
                  {'form':form})

def excluirAluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect ('listar_alunos')

def incluirCurso(request):
    if request.method == 'POST':
       form = CursoForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('listar_cursos')
    else:
        form = CursoForm()   
    return render(request, 'incluir_cursos.html',
                  {'form': form})

def editarCurso(request, id):
    cursos = Cursos.objects.get(id=id)
    form = CursoForm(instance=cursos)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=cursos)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
        
    return render(request,'incluir_cursos.html',
                  {'form':form})

def excluirCurso(request, id):
    cursos = Cursos.objects.get(id=id)
    cursos.delete()
    return redirect ('listar_cursos')