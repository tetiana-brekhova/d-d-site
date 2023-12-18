from django.shortcuts import render, redirect
from django.contrib import messages
from models import Post


def information_about_all_posts(request):
    posts = Post.get_all()
    return render(request, 'posts/list.html', {'content': posts})

def show_post(request, post_id):
    correct_post = Post.get_by_id(post_id)
    return render(request, 'posts/post.html', {"context": correct_post})


# def add_book(request):
#     if request.method == 'GET':
#         authors_all = Author.get_all()
#         context = {'authors': authors_all}
#         return render(request, 'book/form_book.html', context)
#     else:
#         data = request.POST
#         authors_id = request.POST.getlist('authors[]')
#         authors = []
#         if authors_id:
#             for author_id in authors_id:
#                 authors.append(Author.get_by_id(author_id))
#
#         Book.create(data['book_name'], data['book_description'], data['book_count'], authors)
#         return redirect('/book/list/')