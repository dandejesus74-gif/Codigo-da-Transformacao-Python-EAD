from django.core.paginator import Paginator

def listar_produtos(request):
    query = request.GET.get('q', '')
    if query:
        produtos_list = produtos.objects.filter(nome__icontains=query)
    else:
        produtos_list = produtos.objects.all()

    # Paginação: exibe 5 produtos por página
    paginator = Paginator(produtos_list, 5)
    page_number = request.GET.get('page')
    produtos = paginator.get_page(page_number)

    return (request, 'produtos/listar.html', {'produtos': produtos, 'query': query})