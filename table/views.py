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
from .forms import LoginForm



# def index(request):
#     tables = {
#         'classes': table.objects.all(),
#     }
#     return render(request, 'table_template.html', table)

User = get_user_model()



class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    #条件文↓
    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのユーザー情報ページのpkが同じか、又はスーパーユーザーなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


# @login_required
class SampleTemplate(TemplateView):
    """時間割ページ"""
    template_name = "table_template.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        tables = {
                'tables': table.objects.all(),
                'times': time.objects.all(),
                'weeks': week.objects.all(),
             }
        # times = {
        #         'times': time.objects.all(),
        #      }
        # weeks = {
        #         'weeks': week.objects.all(),
        #      }
        return tables

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'table_template.html'


class TableList(ListView):
    """時間割リスト表示ページ"""
    model = table

    template_name = "table_list.html"


    paginate_by = 10
    context_object_name = "tables"

class TableCreate(CreateView):
    """追加ページ"""
    model = table
    fields = ("id", "userId", "classId")

    template_name = "table_create.html"

class TableUpdate(UpdateView):
    """更新ページ"""
    model = table
    fields = ("id", "userId", "classId")

    template_name = "table_update.html"


class TableDelete(DeleteView):
    """削除ページ"""
    model = table

    template_name = "table_delete.html"

# @login_required
# def help(request):
#     return HttpResponse("Member Only Help Page")
