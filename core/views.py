from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404

from .forms import BoardForm

class ProfileView(TemplateView):
    template_name = "core/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        profile_user = get_object_or_404(User, username=kwargs["username"])
        context['board_form'] = BoardForm()
        return context


class BoardFormView(FormView):
    form_class = BoardForm
    template_name = "core/new_board.html"

    def get_context_data(self, **kwargs):
        context = super(BoardFormView, self).get_context_data(**kwargs)
        kwargs['board_form'] = kwargs['form']
        context['board_form'] = context['form']
        del kwargs['form']
        return context

    def form_valid(self, form):
        m = form.save(self.request.user)
        messages.success(self.request, "Board '%s' created successfully" % m.name)
        return super(BoardFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse("user-profile", args=[self.request.user.username])
