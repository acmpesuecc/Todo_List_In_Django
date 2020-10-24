from django.shortcuts import render, redirect
from .models import Todo

# Todo create index view
def index(request):
    # Todo - Get all todos from DB
    todos = Todo.objects.all()

    context = {
        "todos": todos
    }

    # Todo - render index.html file with todos
    return render(request, 'index.html',context)

# Todo create add view
def add(request):

    # Todo - Accept request only if it is a post request
    # Todo - Extract information of todo from the request body
    # Todo - Create a todo object from the information
    # Todo - Add the object to the DB
    # Todo - Redirect to the '/todo' page

    return render(request, 'index.html')


# Todo Create the delete view
def delete(request):
    # Todo - Add id parameter to function
    # Todo - Accept request only if it is a post request
    # Todo - Delete todo Object from DB
    # Todo - Redirect to the '/todo' page
    if request.method=="POST":
            Todo.objects.filter(id=id).delete()
            return redirect('/todo')
    return render(request, 'index.html')
