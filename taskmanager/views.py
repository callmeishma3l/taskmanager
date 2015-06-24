from django.shortcuts import get_object_or_404, render, render_to_response

from django.views import generic

from .models import Task
from .forms import TaskForm

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


# this is the official way to do it from the docs, but still :)
# class LoginRequiredMixin(object):
#    @classmethod
#    def as_view(cls, **initkwargs):
#        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
#        return login_required(view)


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class AdminRequiredMixin(object):
    @method_decorator(user_passes_test(lambda u: u.is_admin))
    def dispatch(self, *args, **kwargs):
        return super(AdminRequiredMixin, self).dispatch(*args, **kwargs)


class IndexView(LoginRequiredMixin,generic.ListView):
    def get_queryset(self):
        return Task.objects.all()
    context_object_name = 'task_list'
    template_name = 'taskmanager/index.html'


@user_passes_test(lambda u: u.is_admin)
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return HttpResponseRedirect(reverse('taskmanager:index'))
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskmanager/edit.html', {'form': form})


class CreateView(AdminRequiredMixin,generic.CreateView):
    model = Task
    template_name = 'taskmanager/create.html'
    form_class = TaskForm


@user_passes_test(lambda u: u.is_admin)
def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('taskmanager:index'))


@user_passes_test(lambda u: u.is_admin)
def editinplace(request, pk):
    task = get_object_or_404(Task, id=pk)
    field_name = request.POST.get("name", None)
    field_value = request.POST.get("value")
    data = {field_name: field_value}
    form = TaskForm(data, instance=task)
    if field_name not in form.errors:
        setattr(task, field_name, field_value)
        task.save()
        return HttpResponse()