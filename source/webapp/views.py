
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Todo, STATUS_CHOICES
from django.http import HttpResponseNotAllowed, Http404


def index_view(request):
    data = Todo.objects.all()
    return render(request, 'index.html', context={
            'todo_list': data})


def todo_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {'todo': todo}
    return render(request, 'todo_view.html', context)


def create_view(request):
    if request.method == "GET":
        return render(request, 'create_todo.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        descriptions = request.POST.get('descriptions')
        status = request.POST.get('status')
        if date == '':
            Todo.objects.create(title=title, descriptions=descriptions, status=status)
        else:
            Todo.objects.create(title=title, descriptions=descriptions, data=date, status=status)

        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def todo_update_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', context={'todo': todo})
    elif request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.status = request.POST.get('status')
        todo.descriptions = request.POST.get('descriptions')
        todo.save()
        return redirect('todo_view', pk=todo.pk)