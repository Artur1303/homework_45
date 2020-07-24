
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Todo, STATUS_CHOICES
from django.http import HttpResponseNotAllowed, Http404


def index_view(request):
    data = Todo.objects.all()
    return render(request, 'index.html', context={
            'todo_list': data})



# def article_view(request, pk):
    # try:
    #     article = Article.objects.get(pk=pk)
    # except Article.DoesNotExist:
    #     raise Http404

    # article = get_object_or_404(Todo, pk=pk)
    #
    # context = {'article': article}
    # return render(request, 'article_view.html', context)


def create_view(request):
    if request.method == "GET":
        return render(request, 'create_todo.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        status = request.POST.get('status')
        if date == '':
            Todo.objects.create(title=title, status=status)
        else:
            Todo.objects.create(title=title, data=date, status=status)

        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


