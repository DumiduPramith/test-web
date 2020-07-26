from django.shortcuts import render, redirect
from .models import Question, Answers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewQuestion
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404  

# Create your views here.
@login_required
def home(request,page_num=1):
    qlist = []
    question_list = Question.objects.all()
    # print(question_list)
    for raw_question in question_list:
        try:
            ans = Answers.objects.get(question_id=raw_question.id)
            continue
            # print(ans)
        except:
            qlist.append(raw_question)
    try:
        p = Paginator(qlist, 3)
        page = p.page(page_num)
        is_paginated = True
    except:
        raise Http404

    context = {
        'page':page,
        'title': 'Answers Home',
        'is_paginated' : is_paginated,
    }
    return render(request, 'blog/index.html', context)


def save_reply(request, key):
    if request.method == 'POST':
        reply = request.POST['reply']
        # print(reply)
        if reply == 'Delete':
            reply = 'Null'
        logged_user = request.user.id
        q_query = Question.objects.get(id=key)
        user_query = User.objects.get(id=logged_user)
        query = Answers(answer=reply, question_id=q_query, acc_id=user_query)
        query.save()

    return redirect('blog-home')
@login_required
def create_question(request):
    if request.method == 'POST':
        form = NewQuestion(request.POST)
        if form.is_valid():
            raw_data = form.cleaned_data
            content = raw_data['content']
            image = request.FILES['question_image']
            print(image)
            logged_user = User.objects.get(id=request.user.id)
            query = Question(content= content,author= logged_user, question_image = image)
            query.save()
            messages.success(request, f'Your Question has been Submitted!')
            return redirect('index')
    form = NewQuestion()
    context ={
        'form' : form,
    }
    return render(request, 'blog/new_question.html', context)