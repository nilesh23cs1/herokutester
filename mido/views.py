from django.shortcuts import render, redirect  # import redirect here
from mido.models import midomodel
from mido.forms import midoform
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    content = {'fruit': 'Homepage Content'}
    return render(request, 'index.html', content)



def didi(request):
    content = {'fruit': 'honey'}
    return render(request, 'hi.html', content)


def about(request):
    content = {'fruit': 'apple'}
    return render(request, 'about.html', content)


def contact(request):
    content = {'fruit': 'carrot'}
    return render(request, 'contact.html', content)


@login_required
def services(request):
    if request.method == 'POST':  # check if request is POST
        form = midoform(request.POST or None)
        if form.is_valid():  # if form data is valid
            fs = form.save(commit=False)
            fs.manage = request.user
            fs.save()
                                          #delaying form.save and change manage field of database
                                          #and requesting username
                                          # then save the form.also save data in model
            print("post success")
        messages.success(request, (
                'New Task Added'))  # message 'New Task Added') is displayed after adding task into database
        print(request.user)
        return (redirect('servin'))

    else:
        alltask = midomodel.objects.all  # otherwise we will print all our task.
        return render(request, 'services.html', {'alltask': alltask})

@login_required
def deletetask(request, taskid):
    task = midomodel.objects.get(pk=taskid)
    task.delete()
    return redirect('servin')

@login_required
def edittask(request, taskid):
    if request.method == 'POST':
        task = midomodel.objects.get(pk=taskid)
        form = midoform(request.POST or None, instance=task)  # since we did not create new form
        if form.is_valid():  # we are updating old object .thus instance is used
            form.save()

        messages.success(request, ('Task Edited'))
        return redirect('servin')
    else:
        taskobj = midomodel.objects.get(pk=taskid)
        return render(request, 'edit.html', {'taskobj': taskobj})

@login_required
def completetask(request, taskid):
    task = midomodel.objects.get(pk=taskid)
    task.done = True
    task.save()
    return redirect('servin')

@login_required
def pendingtask(request, taskid):
    task = midomodel.objects.get(pk=taskid)
    task.done = False
    task.save()
    return redirect('servin')




