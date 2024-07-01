from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponse
from .models import Question, Choice, ChoiceRate, Books, UserDocuments
from .utils import get_questions_context
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import ListView
from django.contrib.auth import get_user_model

from .mixins import PaginationMixin, CacheMixixn
from .forms import UserDocumentForm
# from django.utils.decorators import method_decorator

User = get_user_model()

@login_required
def index(request):
    return render(request, 'index.html', get_questions_context())

class PollIndex(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'index.html'

    def get(self, request):

        return self.render_to_response(get_questions_context())


def detail(request, question_id):
    question = Question.objects.filter(id=question_id).first()
    if question:
        return HttpResponse(f'Here is a question #{question_id} text: {question.question_text}')
    return HttpResponse(f"You're looking for question #{question_id} which doesn`t exists")


@permission_required('polls.can_view_results')
def results(request):
    return render(request, 'results.html', get_questions_context())


def vote(request, choice_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    choice = Choice.objects.filter(id=choice_id).first()
    if choice:
        choice.vote()
    return redirect('index')

def get_popular_choices(request):
    if request.method == "POST":
        if search_string:=request.POST['search']:
            choice_rate = ChoiceRate.objects.first().choice_rate

            search_result = Choice.objects.filter(
                Q(choice_text__contains=search_string) &
                Q(votes__gte=choice_rate or 0)
            )
            return render(request, 'popular_choices.html', {'search_result': search_result})
    
    return render(request, 'popular_choices.html')


from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


@login_required
@permission_required('question.can_edit_question')
def assign_can_view_results_permission(request):
    message =''
    # try:
    #     user = User.objects.get(id=user_id)
    # except User.DoesNotExist:
    #     message = 'User with provided ID was not found'
    #     return render(request, 'assign_perm.html')
    if request.method == 'POST':
        selected_users = request.POST.getlist('users')

        content_type = ContentType.objects.get_for_model(Question)

        can_view_results_permission = Permission.objects.filter(
            codename='can_view_results',
            content_type=content_type
        ).first()
        for user_id in selected_users:
            allowed_user = User.objects.filter(id=user_id).first()
            if allowed_user:
                allowed_user.user_permissions.add(can_view_results_permission)
        
        restricted_users = User.objects.all().exclude(id__in=selected_users)

        for user in restricted_users:
            user.user_permissions.remove(can_view_results_permission)
            
        return redirect('assingn_permission')

    users = User.objects.all()

    return render(request, 'assign_perm.html', {'users': users, 'value': 'fooo'})


class BooksListView(CacheMixixn, PaginationMixin, ListView):
    model = Books
    template_name = 'books_list.html'
    cache_timeout = 60

class UploadUserDocuments(View):
    form = UserDocumentForm

    def get(self, request, *args, **kwargs):
        return render(request, 'upload_docs.html', {'form': self.form})
    
    def post(self, request, *args, **kwargs):
        # form = self.form(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        doc_title = request.POST.get('title')
        file = request.FILES.get('file')
        if all([doc_title, file]):
            UserDocuments.objects.create(title=doc_title, file=file)
        return redirect('books_list')
