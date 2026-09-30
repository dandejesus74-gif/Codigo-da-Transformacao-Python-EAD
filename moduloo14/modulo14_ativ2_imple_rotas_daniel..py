from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
        return redirect('listar_produtos')
    return render(request, 'produtos/cadastrar.html')

def atualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.quantidade = request.POST.get('quantidade')
        produto.save()
        return redirect('listar_produtos')
    return render(request, 'produtos/atualizar.html', {'produto': produto})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'produtos/excluir.html', {'produto': produto})