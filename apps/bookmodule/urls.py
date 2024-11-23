from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="books.index"),
    path("list_books/", views.list_books, name="books.list_books"),
    path("<int:bookId>/", views.viewbook, name="books.view_one_book"),
    path("aboutus/", views.aboutus, name="books.aboutus"),
    path("html5/links/", views.html5_links, name="books.html5_links"),
    path("search/", views.search, name="books.search"),
    path("simple/query", views.simple_query, name="books.simple_query"),
    path("complex/query", views.complex_query, name="books.complex_query"),
    path("lab8/task1", views.Lab8Task1, name="books.Lab8Task1"),
    path("lab8/task2", views.Lab8Task2, name="books.Lab8Task2"),
    path("lab8/task3", views.Lab8Task3, name="books.Lab8Task3"),
    path("lab8/task4", views.Lab8Task4, name="books.Lab8Task4"),
    path("lab8/task5", views.Lab8Task5, name="books.Lab8Task5"),
    path("lab8/task6", views.Lab8Task6, name="books.Lab8Task6"),
    path("lab9_part1/addBook", views.addBook, name="books.addBook"),
    path("lab9_part1/editbook/<int:id>", views.editBook, name="books.editBook"),
    path("lab9_part1/deleteBook/<int:id>", views.deleteBook, name="books.deleteBook"),
    path("lab9_part2/addBook", views.addBookWithForm, name="books.addBookWF"),
    path("lab9_part2/editBook/<int:id>", views.editBookWithForm, name="books.editBookWF"),
    path("lab9_part2/deleteBook/<int:id>", views.deleteBookWithForm, name="books.deleteBookWF"),
    path("lab9_part2/listBooks", views.listBooksWithForm, name="books.listBooksWF"),
]
