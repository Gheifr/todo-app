from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from tasks.forms import TaskForm
from tasks.models import Tag, Task


class TagsView(generic.ListView):
    model = Tag


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


class ToggleCompletedView(View):
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save(update_fields=["is_done"])
        return redirect("tasks:index")
