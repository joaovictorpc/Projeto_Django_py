from django.forms import ModelForm
 
from teste.models import Aluno,Cursos
 
 
class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class CursoForm(ModelForm):
    class Meta:
        model = Cursos
        fields = '__all__'

