from django.shortcuts import render

# Create your views here.

def home(request):
    dados = {}
    campos_obrigatorios = {'nome', 'email'}
    erros = {}

    for chave in 'nome idade email sexo faixa_etaria hobby texto estado'.split():
        valor = request.POST.getlist(chave)
        if chave == 'hobby':
            dados[chave] = valor
        elif len(valor) == 1:
            valor_extraido = valor[0]
            dados[chave] = valor_extraido
            if chave in campos_obrigatorios and valor_extraido == '':
                erros[chave] = f'O campo {chave} é obrigatório'
        elif len(valor) == 0:
            dados[chave] = None
            if chave in campos_obrigatorios:
                erros[chave] = f'O campo {chave} é obrigatório'
        else:
            raise ValueError('Alguém mandou dados em formato impróprio')

    if erros:
        contexto = {'erros': erros, 'dados': dados}
        return render(request, 'base/home.html', contexto)
    
    return render(request, 'base/home.html')