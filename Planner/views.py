from django.shortcuts import render, redirect
from Planner.models import Planner
from django.http import JsonResponse
from .common_ import norm, filter_, clsmemory, norm_time

memory = clsmemory()

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
            row = Planner.objects.filter(Task=memory.list[int(item_to_be_deleted)][1], Username=current_user)

            row.delete()

            size = len(Planner.objects.filter(Username=current_user))
            Planner.change_auto_increment_value(size)


        elif request.POST["remove_or_add"] == '1':
            item1, item2 = norm(request.POST["input"])
            # adding new task to the table
            row = Planner.objects.create(Task=item1, Deadline=item2, Username=current_user)
            row.save()

        # I don't have to call the headers everytime. might make this code
        # more efficient ngl.
        # getting the table headers.
        # KEYS.
        MODEL_HEADERS = [field.name for field in Planner._meta.get_fields() if field.name != 'Username']

        # getting query results.
        # otherwise the entire table for the logged in user, in form of a list.
        query_results = [row for row in list(Planner.objects.filter(Username=current_user).values())]

        memory.list = [] # reset and update table.
        count = 1
        for row in query_results: # each row is a dict.
            memory.list.append([])

            for key in MODEL_HEADERS:
                if key == "Priority":
                    row[key] = count
                    count += 1

                elif key == "Add_On" or key == "Deadline":
                    row[key] = norm_time(row[key])

                memory.list[-1].append(row[key])

        # merging model headers and query results.
        memory.list.insert(0, MODEL_HEADERS)
        data = {'Data': memory.list}

        return JsonResponse(data)