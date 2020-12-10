from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from todo_list_app.models import lists_container

# create new task in to do list


def lists(request):
    # here temp is the var where we store our tasks name
    temp = lists_container.objects.all()
    if request.method == "POST":            # post means you want to add something in form
        # whatever task name we write in the add task name box will assign to the var temp1
        temp1 = request.POST['box']
        # now whatever task name we write in the add task name box will assign to store and after that assign in temp2
        temp2 = lists_container(store=temp1)
        temp2.save()                        # finally we save the task name to database
        # this is used to avoid double submission of same task when we reload the page
        return HttpResponseRedirect('/')
    return render(request, 'todo_list_app/index.html', {'temp': temp})


# edit a list item

def edit(request, id):
    edit = lists_container.objects.get(id=id)
    if request.method == "POST":
        # the item which is already saved in store variable we will edit that item
        edit.store = request.POST['box']
        edit.save()
        return HttpResponseRedirect('/')
    return render(request, 'todo_list_app/edit.html', {'edit': edit})

# delete a list item


def delete(request, id):
    del_list = lists_container.objects.get(id=id)
    del_list.delete()
    return redirect("/")
