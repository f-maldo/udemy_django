from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    # return HttpResponse("Hola Mundo Django")
    questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'questions': questions,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("Detail: %s" % question_id)


def results(request, question_id):
    response = "Results: %s"
    return response % question_id


def vote(request, question_id):
    return HttpResponse("Vote %s" % question_id)
