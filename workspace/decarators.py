from django.shortcuts import get_object_or_404, redirect

from pradact.models import Pradact


def is_owner(views):

    def inner_func(request, id, *args, **kwargs):
        pradact = get_object_or_404(Pradact, id=id)

        if pradact.author == request.user:
            return views(request, id, *args, **kwargs)
        
        return redirect('/workspace/')

    return inner_func