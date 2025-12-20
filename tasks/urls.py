from django.urls import path

from tasks import views

urlpatterns = [
    path("", views.TasksView.as_view(), name="index"),
    path("toggle-completed/<int:pk>", views.ToggleCompletedView.as_view(), name="toggle_completed"),
    path("create/", views.TasksCreateView.as_view(), name="create"),
    path("update/<int:pk>", views.TasksUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.TasksDelete.as_view(), name="delete"),
    path("tags/", views.TagsView.as_view(), name="tags"),
    path("tags/create/", views.TagsCreateView.as_view(), name="tags_create"),
    path("tags/update/<int:pk>", views.TagsUpdate.as_view(), name="tags_update"),
    path("tags/delete/<int:pk>", views.TagsDelete.as_view(), name="tags_delete"),
]

app_name = "tasks"
