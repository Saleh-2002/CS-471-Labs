from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import BookForm
from django.db.models import Q
from .models import Address, Book
from django.db.models import Sum, Avg, Max, Min, Count


def index(request):
    Name = request.GET.get("Name") or "World!"
    return render(
        request, "bookmodule/index.html", {"Name": Name}
    )  # render the template with the provided name


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains="")  # <- multiple objects
    return render(request, "bookmodule/bookList.html", {"books": mybooks})


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
            if isTitle and string in item["title"].lower():
                contained = True
            if not contained and isAuthor and string in item["author"].lower():
                contained = True
            if contained:
                newBooks.append(item)
        return render(request, "bookmodule/bookList.html", {"books": newBooks})
    return render(request, "bookmodule/search.html")


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


def complex_query(request):
    mybooks = books = (
        Book.objects.filter(author__isnull=False)
        .filter(title__icontains="and")
        .filter(edition__gte=2)
        .exclude(price__lte=100)[:10]
    )
    if len(mybooks) >= 1:
        return render(request, "bookmodule/bookList.html", {"books": mybooks})
    else:
        return render(request, "bookmodule/index.html")


def Lab8Task1(request):
    books = Book.objects.filter(Q(price__lte=100))
    return render(request, "bookmodule/Lab8Task1.html", {"books": books})


def Lab8Task2(request):
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains="qu") | Q(author__icontains="qu"))
    )
    return render(request, "bookmodule/Lab8Task2.html", {"books": books})


def Lab8Task3(request):
    books = Book.objects.filter(
        Q(edition__lte=2) & ~(Q(title__icontains="qu") | Q(author__icontains="qu"))
    )
    return render(request, "bookmodule/Lab8Task3.html", {"books": books})


def Lab8Task4(request):
    books = Book.objects.all().order_by("title")
    return render(request, "bookmodule/Lab8Task4.html", {"books": books})


def Lab8Task5(request):
    stats = Book.objects.aggregate(
        total_books=Count("id"),
        total_price=Sum("price"),
        avg_price=Avg("price"),
        max_price=Max("price"),
        min_price=Min("price"),
    )
    return render(request, "bookmodule/Lab8Task5.html", {"stats": stats})


def Lab8Task6(request):
    cities = Address.objects.annotate(student_count=Count("student"))
    return render(request, "bookmodule/Lab8Task6.html", {"cities": cities})


def addBook(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        price = request.POST.get("price")
        edition = request.POST.get("edition")
        newBook = Book(title=title, author=author, price=price, edition=edition)
        newBook.save()
        return redirect("books.addBook")  # Redirect to the same form or another page
    return render(request, "bookmodule/addBook.html")


def editBook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.price = request.POST.get("price")
        book.edition = request.POST.get("edition")
        book.save()
        return redirect("books.bookList")  # Redirect to a relevant page
    return render(request, "bookmodule/editBook.html", {"book": book})


def deleteBook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect("books.bookList")  # Redirect to a relevant page


def addBookWithForm(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.bookListWF')
    else:
        form = BookForm()
    return render(request, 'bookmodule/addBookWF.html', {'form': form})

def editBookWithForm(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.bookListWF')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookmodule/editBookWF.html', {'form': form, 'book': book})


def deleteBookWithForm(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('books.bookListWF')
    return render(request, 'bookmodule/deleteBookWF.html', {'book': book})

def listBooksWithForm(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/bookListWF.html', {'books': books})