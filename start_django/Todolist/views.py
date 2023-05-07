from django.shortcuts import render
from .models import Todo
# Create your views here.
def index(request):
    _todos=Todo.objects.all()
    return render(request,'index.html',{'todos':_todos})

from django.shortcuts import HttpResponseRedirect
from Todolist.models import Todo
from django.urls import reverse

# url = /create_todo
def createTodo(request):
    content = request.POST['todoContent']
    new_todo = Todo(title=content)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
    _id = request.GET['todoNum']
    todo = Todo.objects.get(id=_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))