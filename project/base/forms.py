import json
from django import forms
from .models import Cadastro


class JsonFormMixin():

    def as_json(self):
        dct = {name: field.to_python(self[name].data) for name, field in self.fields.items()}
        return json.dumps(dct)


class CadastroForm(forms.ModelForm, JsonFormMixin):

    class Meta:
        model = Cadastro
        fields = ('nome', 'email', 'idade', 'sexo', 'hobbies')

    nome = forms.CharField(label='Nome', max_length=64, min_length=3, required=True)
    email = forms.EmailField(required=True)
    idade = forms.IntegerField()
    sexo = forms.ChoiceField(
        choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')])
    hobbies = forms.MultipleChoiceField(
        choices=[('futebol', 'Futebol'), ('game', 'Game'), ('leitura', 'Leitura')]
    )
