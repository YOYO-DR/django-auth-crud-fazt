from django import forms
from tasks.models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        #le paso el modelo
        model = Task
        #y le indico los campos a poner, las fechas se autoponen, y el usuario sera el que este autenticados
        fields = ['title','description','important']
        widgets={
            #le agrego atributos que quiera con esta forma
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe el titulo'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe una descripción'}),
            'important':forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }