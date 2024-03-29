from django.shortcuts import redirect, render
from django.http import HttpResponse
from teste.forms import AlunoForm,CursoForm
from teste.models import Aluno, Cursos
# Create your views here.
def index (request):
    return render(request,'inicio.html')

def listar_Aluno(request):
     busca= request.GET.get('busca')
     ordem = request.GET.get ('ordem')

     if busca:
         if not ordem:
              alunos= Aluno.objects.filter(nome__icontains=busca).extra(select={'novo':'lower(nome)'}).order_by('novo')
         elif ordem == 'nome':
               alunos= Aluno.objects.filter(nome__icontains=busca).extra(select={'novo':'lower(nome)'}).order_by('novo')
         elif ordem == '-nome':
               alunos= Aluno.objects.filter(nome__icontains=busca).extra(select={'novo':'lower(nome)'}).order_by('-novo')
     else: 
         busca =''  
         if not ordem:  
              alunos = Aluno.objects.all().extra(select={'novo':'lower(nome)'}).order_by('novo') 
         elif ordem == 'nome':
               alunos = Aluno.objects.all().extra(select={'novo':'lower(nome)'}).order_by('novo')
         elif ordem == '-nome':
               alunos = Aluno.objects.all().extra(select={'novo':'lower(nome)'}).order_by('-novo')
     
     return render(request,'listar_aluno.html',
                  {'alunos': alunos, 'busca':busca}) 

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