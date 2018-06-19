from django.shortcuts import render

from django.http.response import HttpResponse

from django.contrib.auth import get_user_model




from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView
from .models import table,user,teacher,classes,time,week
from django.views import generic
from .forms import LoginForm, UserCreateForm

from django.urls import reverse_lazy





User = get_user_model()



class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    #条件文↓
    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのユーザー情報ページのpkが同じか、又はスーパーユーザーなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserCreate(generic.CreateView):
    """ユーザー登録"""
    template_name = 'user-create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy("table:user_create_complete")



class UserCreateComplete(generic.TemplateView):
    """メール内URLアクセス後のユーザー本登録"""
    template_name = 'user_create_complete.html'



class SampleTemplate(TemplateView):
    """時間割ページ"""
    template_name = "table_template.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        data = {
                'tables': table.objects.all(),
                'times': time.objects.all(),
                'weeks': week.objects.all(),
             }

        return data

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'table_template.html'


class TableList(ListView):
    """時間割リスト表示ページ"""
    template_name = 'table-list.html'

    model = classes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

    def get_queryset(self):
        return classes.objects.filter(weekNum=self.kwargs['week'],
                                      timeNum=self.kwargs['time'])


    paginate_by = 5
    context_object_name = "classes"


class TableUpdate(TemplateView):
    """更新ページ"""
    template_name = "table-update.html"

    model = table



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        data = {
                'tables': table.objects.all(),
                'times': time.objects.all(),
                'weeks': week.objects.all(),
             }

        return data





    def get(self, request, **kwargs):
        super().get(request, **kwargs)
        userid = kwargs['id']
        time = kwargs['time']
        week = kwargs['week']
        classid = kwargs['classid']

        table.objects.filter(userId__id=userid,
                             classId__weekNum=week,
                             classId__timeNum=time).delete()


        table.objects.update_or_create(userId=user(id=userid),
                                       classId=classes(id=classid))


        return super().get(request, **kwargs)



class TableDelete(TemplateView):
    """削除ページ"""
    template_name = "table-delete.html"

    model = table


    def get(self, request, **kwargs):
        super().get(request, **kwargs)
        userid = kwargs['id']
        time = kwargs['time']
        week = kwargs['week']

        table.objects.filter(userId__id=userid,
                             classId__weekNum=week,
                             classId__timeNum=time).delete()




        return super().get(request, **kwargs)
