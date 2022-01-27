from django.shortcuts import render
from django.http import Http404, HttpResponse


books =[
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'},
]

def not_found_404(request, exception):
    data = { 'err': exception }
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html')

def home(req):
    data = { "books": books }
    return render(req, 'home.html', data)

def show(req, id):
    try:
        book = [ book for book in books if book["id"] == id ][0]
    except:
        raise Http404
    data = { "book": book }
    return render(req, 'show.html', data)

# def show(request, dog_id):
#     dog = get_object_or_404(Dog, pk=dog_id)
#     if request.method == 'POST':
#         form = AdoptDogForm(request.POST)
#         if form.is_valid():
#             dog.owner = request.user
#             dog.save()
#             return redirect("dog-show", dog_id=dog_id)
#     else:
#         form = AdoptDogForm(initial={'owner': request.user})
#     data = {
#         'dog': dog,
#         'form': form
#     }
#     return render(request, 'dogs/show.html', data)

# def not_found_404(req, exception):
#     data = { 'err': exception }
#     return render(req, '404.html', data)