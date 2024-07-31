from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from pprint import pprint
from workspace.forms import PradactForm, PradactModelForm
from pradact.models import Category, Pradact, Tag

# 3)
# def workspace(request):
#     pradact = Pradact.objects.all()
#     page = int(request.GET.get('page', 1))
#     page_size = int(request.GET.get('page_size', 4))
 
#     pagin = Paginator(pradact, page_size)
#     pradact = pagin.get_page(page) 

#     return render(request, 'workspace/index.html', {'pradact': pradact})


# def create_pradact(request):
#     form = PradactModelForm()

#     if request.method == 'POST':
#         form = PradactModelForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             pradact = form.save()
#             return redirect('/workspace/')
         
#     return render(request, 'workspace/create_pradact.html', {'form': form})

# def delete_pradact(request, id):
#     pradact = get_object_or_404(Pradact, id=id)
#     pradact.delete()
#     return redirect('/workspace/')

# def ubdate_pradact(request, id):
#     pradact = get_object_or_404(Pradact, id=id)
#     form = PradactModelForm(instance=pradact)

#     if request.method == 'POST':
#         form = PradactModelForm(data=request.POST, files=request.FILES, instance=pradact)

#         if form.is_valid():
#             form.save()
#             return redirect('/workspace/')

#     return render(request, 'workspace/ubdate_pradact.html', {
#         'pradact': pradact,
#         'form': form,
#     })

# 2)
def workspace(request):
    pradact = Pradact.objects.all().order_by('-date', 'name')
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 4))
 
    pagin = Paginator(pradact, page_size)
    pradact = pagin.get_page(page) 

    return render(request, 'workspace/index.html', {'pradact': pradact})


def create_news(request):
    form = PradactForm()

    if request.method == 'POST':
        form = PradactForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            pradact = form.save()
            return redirect('/workspace/')
         
    return render(request, 'workspace/create_pradact.html', {'form': form})


def delete_pradact(request, id):
    pradact = get_object_or_404(Pradact, id=id)
    pradact.delete()
    return redirect('/workspace/')


def ubdate_pradact(request, id):
    pradact = get_object_or_404(Pradact, id=id)

    if request.method == 'POST':
        pradact.name = request.POST.get('name')
        pradact.description = request.POST.get('description')
        pradact.content = request.POST.get('content')
        pradact.author = request.POST.get('author')
        pradact.is_published = request.POST.get('is_published') == 'on'
       

        category_id = int(request.POST.get('category'))
        pradact.category = Category.objects.get(id=category_id)

        tag_ids = list(map(int, request.POST.getlist('tags')))
        tags = Tag.objects.filter(id__in=tag_ids)

        pradact.tags.clear()
        pradact.tags.add(*tags)

        image = request.FILES.get('image')

        if image:
            pradact.image.save(image.name, image)

        pradact.save()
       
        
        return redirect('/workspace/')

    
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    return render(request, 'workspace/ubdate_pradact.html', {
        'categories': categories, 
        'tags': tags,
        'pradact': pradact,
    })



# 1)

# def workspace(request):
#     pradact = Pradact.objects.all()
#     page = int(request.GET.get('page', 1))
#     page_size = int(request.GET.get('page_size', 4))
 
#     pagin = Paginator(pradact, page_size)
#     pradact = pagin.get_page(page) 

#     return render(request, 'workspace/index.html', {'pradact': pradact})


# def create_pradact(request):

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description',)
#         price = request.POST.get('price')
#         is_published = request.POST.get('is_published') == 'on'
#         image = request.FILES.get('image')

#         category_id = int(request.POST.get('category'))
#         category = Category.objects.get(id=category_id)
        

#         tag_ids = list(map(int, request.POST.getlist('tags')))
#         tags = Tag.objects.filter(id__in=tag_ids)

#         pradact = Pradact.objects.create(
#             name=name,
#             price=price, 
#             description=description,
#             is_published=is_published,
#             category=category,
#         )

#         pradact.tags.add(*tags)

#         pradact.image.save(image.name, image)

#         pradact.save()
        
#         return redirect('/workspace/')

    
    
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
    
#     return render(request, 'workspace/create_pradact.html', {'categories': categories, 'tags': tags})


# def delete_pradact(request, id):
#     pradact = get_object_or_404(Pradact, id=id)
#     pradact.delete()
#     return redirect('/workspace/')

# def ubdate_pradact(request,id):
#     pradact = get_object_or_404(Pradact, id=id)
#     if request.method == 'POST':
#         pradact.name = request.POST.get('name')
#         pradact.description = request.POST.get('description',)
#         pradact.price = request.POST.get('price')
#         pradact.is_published = request.POST.get('is_published') == 'on'
#         category_id = int(request.POST.get('category'))
#         pradact.category = Category.objects.get(id=category_id)
#         tag_ids = list(map(int, request.POST.getlist('tags')))
#         tags = Tag.objects.filter(id__in=tag_ids)

        
#         pradact.tags.clear()
#         pradact.tags.add(*tags)
#         image = request.FILES.get('image')
#         if image:
#             pradact.image.save(image.name, image)
#         pradact.save()
        
#         return redirect('/workspace/')

    
    
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     return render(request, 'workspace/ubdate_pradact.html', {'categories': categories, 'tags': tags,'pradact':pradact})
# # Create your views here.
