from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    Name = request.GET.get("Name") or "World!"
    return render(
        request, "bookmodule/index.html", {"Name": Name}
    )  # render the template with the provided name


def index2(request, val1=0):
    return HttpResponse(f"Value 1: {str(val1)}")


def viewbook(request, bookId): 
# assume that we have the following books somewhere (e.g. database) 
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'} 
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    targetBook = None 
    if book1['id'] == bookId: targetBook = book1 
    if book2['id'] == bookId: targetBook = book2 
    context = {'book':targetBook} # book is the variable name accessible by the template 
    return render(request, 'bookmodule/show.html', context)