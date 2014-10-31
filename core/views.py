from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404

from .forms import BoardForm, PinForm
from .models import Board, Pin

class ProfileView(TemplateView):
    template_name = "core/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        profile_user = get_object_or_404(User, username=kwargs["username"])
        context['profile_user'] = profile_user
        context['boards'] = profile_user.board_set.all()
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


class PinFormView(FormView):
    form_class = PinForm
    template_name = "core/new_pin.html"

    def get_context_data(self, **kwargs):
        context = super(PinFormView, self).get_context_data(**kwargs)
        kwargs['pin_form'] = kwargs['form']
        context['pin_form'] = context['form']
        del kwargs['form']
        return context

    def form_valid(self, form):
        self.m = form.save(self.request.user)
        messages.success(self.request, "Pin added successfully")
        return super(PinFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse("user-board", args=[
            self.request.user.username, self.m.board.slug])


class BoardView(TemplateView):
    template_name = "core/user_board.html"

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        profile_user = get_object_or_404(User, username=kwargs["username"])
        context['profile_user'] = profile_user
        context['board'] = get_object_or_404(Board, slug=kwargs['board_slug'])
        context['pin_form'] = PinForm()
        return context


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        pins = Pin.objects.all()
        context['pins'] = pins
        return context



