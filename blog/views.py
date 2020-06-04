from django.shortcuts import render, redirect
from .models import Question, Answers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from .forms import NewQuestion
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
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
    context = {
        'question_list': qlist,
        'title': 'Answers Home',
    }
    return render(request, 'blog/index.html', context)

class HomeListView(ListView):
    model = Question
    template_name = 'blog/index.html'
    context_object_name = 'question_list'

def save_reply(request, key):
    if request.method == 'POST':
        reply = request.POST['reply']
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
            title = raw_data['title']
            content = raw_data['content']
            logged_user = User.objects.get(id=request.user.id)
            query = Question(title= title, content= content, author= logged_user)
            query.save()
            messages.success(request, f'Your Question has been Submitted!')
            return redirect('index')
    form = NewQuestion()
    context ={
        'form' : form,
    }
    return render(request, 'blog/new_question.html', context)