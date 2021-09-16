from django.shortcuts import render,redirect
from TODOLIST.models import todomodel
from TODOLIST.forms import todoform
# Create your views here.
def todolst(request): 
    todoall = todomodel.objects.all().order_by('-date')
    if request.method == 'POST':
        form = todoform(request.POST or None)
        #print(form.is_valid())
        print(form.errors.as_data())
        #print(form.as_p())
        if form.is_valid():
            form.save()
            #todoall = todomodel.objects.all()
    #form = todoForm()
            return redirect('todolst')
    context = {'todos':todoall}
    return render(request, 'todolist/home.html', context)

def delete(request, todo_id):
    todo = todomodel.objects.get(id=todo_id)
    todo.delete()
    #messages.success(request, ('Task has been Deleted!'))
    return redirect('todolst')

def status(request, todo_id):
    todo = todomodel.objects.get(id=todo_id)
    todo.status = True
    todo.save()
    #messages.success(request, ('Task has been Deleted!'))
    return redirect('todolst')


    