from django.http import Http404
from django.shortcuts import render
from pradact.models import Pradact
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


    
def main(request):
    pradact = Pradact.objects.filter(is_published=True).order_by("price")

    search = request.GET.get('search')
    
    if search:
        pradact = pradact.filter(name__icontains=search)

    category_id = int(request.GET.get('category', 0))

    if category_id:
        pradact = pradact.filter(category__id=category_id)

    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 4))
 
    pagin = Paginator(pradact, page_size)
    pradact = pagin.get_page(page) 

    return render(request, 'index.html', {'pradact': pradact})


# Create your views here.
def detail_pradact(request, id):
    # try:
    #     pradact = Pradact.objects.get(id=id, is_published=True)
    # except Pradact.DoesNotExist as e:
    #     raise Http404
    pradact = get_object_or_404(Pradact, id=id,is_published=True)

    if request.user.is_authenticated:
        user = request.user
        if user != pradact.author:
            pradact.views += 1
    
    else:
        pradact.views += 1

    pradact.save()


    return render(request, 'detail_pradact.html', {'pradact': pradact})