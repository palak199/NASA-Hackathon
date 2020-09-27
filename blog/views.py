from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def blog_view(request):
    context   = Blog.objects.all()
    paginator = Paginator(context,4)
    page = request.GET.get('page')
    try:
        context = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        context = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        context = paginator.page(paginator.num_pages)
    return render(request,'blog.html',{'context':context})
