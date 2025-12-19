from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskForm
from tasks.models import Tag, Task


class TagsView(generic.ListView):
    model = Tag
    # template_name = "tag_list.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = ('name',)


class TagsUpdate(generic.UpdateView):
    model = Tag
    fields = ('name',)
    success_url = reverse_lazy("tasks:tags")


class TagsDelete(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tags")


class TasksView(generic.ListView):
    model = Task
    queryset = Task.objects.all().order_by("is_done", "date_created")
    template_name = "index.html"


class TasksCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TasksUpdate(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TasksDelete(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


def toggle_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)

    task.is_done = not task.is_done
    task.save()

    return redirect(
        "tasks:index",
    )
