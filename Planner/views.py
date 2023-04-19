from django.shortcuts import render, redirect
from Planner.models import Planner, User_Interaction_Details
from django.http import JsonResponse
from .common_ import norm, clsmemory, norm_time, dist



memory = clsmemory()

def reinitiate_memory(current_user):
    # I don't have to call the headers everytime. might make this code
    # more efficient ngl.
    # getting the table headers.
    # KEYS.
    MODEL_HEADERS = [field.name for field in Planner._meta.get_fields() if
                     field.name not in ['Username', 'NextUpdate', 'Id']]

    # getting query results.
    # otherwise the entire table for the logged in user, in form of a list.
    query_results = [row for row in list(Planner.objects.filter(Username=current_user).defer("NextUpdate").values())]

    memory.list = []  # reset and update table.
    count = 1
    for row in query_results:  # each row is a dict.
        memory.list.append([])

        for key in MODEL_HEADERS:
            if key == "Priority":
                row[key] = count
                count += 1

            elif key == "Add_On" or key == "DeadLine":
                row[key] = norm_time(row[key])

            memory.list[-1].append(row[key])

    # merging model headers and query results.
    memory.list.insert(0, MODEL_HEADERS)


# Create your views here.
def Homepage(request):
    current_user = request.user.username

    if current_user == "":
        return redirect('/Login/')

    elif request.method== 'GET':
        return render(request, "Homepage.html")

    elif request.method == 'POST':
        if request.POST["remove_or_add"] == '0':
            item_to_be_deleted = request.POST["input"]
            print(memory.list, item_to_be_deleted)

            if memory.list == []: reinitiate_memory(current_user)

            row = Planner.objects.filter(Task=memory.list[int(item_to_be_deleted)][1], Username=current_user)
            row.delete()

            size = len(Planner.objects.filter(Username=current_user))
            Planner.change_auto_increment_value(size)


        elif request.POST["remove_or_add"] == '1':
            item1, item2 = norm(request.POST["input"])
            # adding new task to the table
            related_instance = User_Interaction_Details.objects.get(Username=current_user)
            row = Planner.objects.create(Task=item1, DeadLine=item2, NextUpdate=dist(item2), Username=related_instance)
            row.save()

        reinitiate_memory(current_user)
        data = {'Data': memory.list}

        return JsonResponse(data)