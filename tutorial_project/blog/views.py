from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


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


def author_list(request):
    authors = Author.objects.all()
    template_name = "blog/author_list.html"

    return render(request, template_name, {"object_list": authors})


@login_required
def author_create(request):
    form = AuthorForm()
    template_name = "blog/author_form.html"

    if request.method == 'POST':
        try:
            form = AuthorForm(request.POST)

            if form.is_valid():
                form.save()

                messages.add_message(request, messages.INFO, "Author instance saved")
                return redirect("author-list")
        except:
            return render(request, template_name, {"form": form})

    return render(request, template_name, {"form": form})


@login_required
def author_update(request, pk):
    author = Author.objects.get(id=pk)
    form = AuthorForm(instance=author)

    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)

        if form.is_valid():
            try:
                form.save()
                author = form.instance

                author.created_by = request.user
                author.updated_by = request.user
                author.save()

                messages.add_message(request, messages.INFO, "Author Updated Successfully")
                return redirect('author-list')
            except:
                messages.add_message(request, messages.INFO, "An error occured")
                return render(request, "blog/author_form.html", {"form": AuthorForm(instance=author)})

    return render(request, "blog/author_form.html", {"form": form})

def author_detail(request, pk):
    author_object = Author.objects.get(pk=pk)

    return render(request, "blog/author_detail.html", {"object": author_object})


def author_delete(request, pk):
    author_object = Author.objects.get(pk=pk)
    author_object.delete()
    messages.add_message(request, messages.INFO, "Author was successfully deleted")
    return redirect("author-list")


