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


# def index(request):
# return render(request, "bookmodule/index.html")


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {
        "id": 123,
        "title": "Continuous Delivery",
        "author": "J. Humble and D. Farley",
    }
    book2 = {"id": 456, "title": "Secrets of Reverse Engineering", "author": "E. Eilam"}
    targetBook = None
    if book1["id"] == bookId:
        targetBook = book1
    if book2["id"] == bookId:
        targetBook = book2
    context = {
        "book": targetBook
    }  # book is the variable name accessible by the template
    return render(request, "bookmodule/show.html", context)


def html5_links(request):
    links = [
        {"name": "HTML5 Specification", "url": "https://html.spec.whatwg.org/"},
        {
            "name": "MDN HTML5 Guide",
            "url": "https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5",
        },
        # Add more links here
    ]
    return render(request, "bookmodule/html5_links.html", {"links": links})


def search(request):
    if request.method == "POST":
            string = request.POST.get("keyword").lower()
            isTitle = request.POST.get("option1")
            isAuthor = request.POST.get("option2")
            # now filter
            books = __getBooksList()
            newBooks = []
            for item in books:
                contained = False
                if isTitle and string in item["title"].lower(): contained = True
                if not contained and isAuthor and string in item["author"].lower(): contained = True
                if contained: newBooks.append(item)
            return render(request, "bookmodule/bookList.html", {"books": newBooks})
    return render(request, "bookmodule/bookList.html")



def __getBooksList():
    book1 = {
        "id": 12344321,
        "title": "Continuous Delivery",
        "author": "J.Humble and D. Farley",
    }
    book2 = {
        "id": 56788765,
        "title": "Reversing: Secrets of Reverse Engineering",
        "author": "E. Eilam",
    }
    book3 = {
        "id": 43211234,
        "title": "The Hundred-Page Machine Learning Book",
        "author": "Andriy Burkov",
    }
    return [book1, book2, book3]
