from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Question, Choice
from .utils import get_questions_context


def index(request):
    return render(request, 'index.html', get_questions_context())


def detail(request, question_id):
    question = Question.objects.filter(id=question_id).first()
    if question:
        return HttpResponse(f'Here is a question #{question_id} text: {question.question_text}')
    return HttpResponse(f"You're looking for question #{question_id} which doesn`t exists")


def results(request):
    return render(request, 'results.html', get_questions_context())


def vote(request, choice_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    choice = Choice.objects.filter(id=choice_id).first()
    if choice:
        choice.vote()
    return redirect('index')