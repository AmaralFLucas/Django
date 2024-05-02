from django.shortcuts import render, redirect
from .models import Produtos, Categoria
from datetime import datetime

def index(request):
    produtos = Produtos.objects.all()
    return render(request, 'pages/index.html', {"produtos":produtos})

def adicionar_produto(request):

    if request.method == "POST":
        nome = request.POST['nome']
        preco = request.POST['preco']
        descricao = request.POST['descricao']
        quantidade = request.POST['quantidade']
        codigo = request.POST['codigo']
        em_estoque = False
        if int(quantidade) > 0:
            em_estoque = True
        data_criacao = datetime.now()

        Produtos.objects.create(
            nome=nome,
            preço=preco,
            descricao=descricao,
            quantidade=quantidade,
            codigo=codigo,
            em_estoque=em_estoque,
            data_criacao=data_criacao
        )

        return redirect('index')
    
    else:
        return render(request, 'pages/adicionar_produto.html')
    
def produto(request, id):
    detalhes = Produtos.objects.get(id=id)
    return render(request, 'pages/produto.html', {'detalhe': detalhes})

def excluir(request, id):
    produto = Produtos.objects.get(id=id).delete()
    # produto.delete()
    return redirect('index')