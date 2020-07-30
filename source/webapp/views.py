
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Todo, STATUS_CHOICES
from django.http import HttpResponseNotAllowed, Http404
from webapp.form import TodoForm


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
        form = TodoForm()
        return render(request, 'create_todo.html', context={
            'form': form,
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo = Todo.objects.create(
                title=form.cleaned_data['title'],
                data=form.cleaned_data['data'],
                descriptions=form.cleaned_data['descriptions'],
                status=form.cleaned_data['status'])
            return redirect('todo_view', pk=todo.pk)
        else:
            return render(request, 'create_todo.html', context={'form': form})

    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


# def todo_update_view(request, pk):
#     todo = get_object_or_404(Todo, pk=pk)
#     if request.method == 'GET':
#         return render(request, 'update.html', context={'todo': todo, 'status_choices': STATUS_CHOICES})
#     elif request.method == 'POST':
#         todo.title = request.POST.get('title')
#         todo.status = request.POST.get('status')
#         todo.descriptions = request.POST.get('descriptions')
#         todo.save()
#         return redirect('todo_view', pk=todo.pk)
def todo_update_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'GET':
        form = TodoForm(data={
            'title': todo.title,
            'status': todo.status,
            'description': todo.descriptions,
            'data': todo.data
        })
        return render(request, 'update.html', context={'form': form, 'status_choices': STATUS_CHOICES, 'todo':todo })
    elif request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo.title = form.cleaned_data['title']
            todo.data = form.cleaned_data['data']
            todo.descriptions = form.cleaned_data['descriptions']
            todo.status = form.cleaned_data['status']
            todo.save()
            return redirect('todo_view', pk=todo.pk)
        else:
            return render(request, 'update.html', context={'form': form})

def todo_delete_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'todo': todo})
    elif request.method == "POST":
        todo.delete()
        return redirect('index')

