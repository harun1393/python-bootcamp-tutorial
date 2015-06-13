from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    name = request.GET.get("name", "Python Bootcamp")
    time = request.GET.get("time", "Morning")
    season = request.GET.get("season", "Raining")

    output = """
    Hello {0}, Good {1}! It is {2} now! Good {1} again {0}!!!
    """.format(name, time, season)

    return HttpResponse(output)


def good_bye(request):
    return HttpResponse("<b>Good-Bye!!!</b>")


def request_dump(req):
    if req.method == "GET":
        return HttpResponse("I RECEIVED A GET")
    else:
        return HttpResponse("I DIDN'T RECEIVE A GET")


def reverser(request):
    if request.method == 'POST':
        name = request.POST.get("input1")
        return HttpResponse("{} -> {}".format(name, name[::-1]))

    return render(request, "blog/reverse.html")


def tpl_hello(request):
    return render(request, "blog/index.html", {"name": "Bootcamp",
                                               "teachers": ["Mafinar Khan",
                                                            "Mozammel Hoque",
                                                            "Tahmid Rafi"],
                                               "show_teachers": not False})
































