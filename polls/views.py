from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Question
from django.shortcuts import render_to_response
from .models import Question
from django.shortcuts import render_to_response
from polls.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/polls/home')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response('polls/home', )
 
def logout_page(request):
    logout(request)
    template = loader.get_template('polls/index.html')

    # ... your python code/script
   
    return HttpResponse(template.render(request)) 
    #return HttpResponseRedirect('{% url 'polls.views.index'  %}')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    #output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
         'latest_question_list': latest_question_list,
	}
    return HttpResponse(template.render(context,request))


def show(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/show.html')

    template = loader.get_template('polls/index.html')
    context = {
         'latest_question_list': latest_question_list,
        }

    return HttpRespnse(template.render(context,request))

@login_required(login_url='django.contrib.auth.views.login')
def show1(request):
    template = loader.get_template('polls/chart-chartjs.html')

    # ... your python code/script
   
    return HttpResponse(template.render(request)) 
def page(request):
    template = loader.get_template('polls/home.html')

    # ... your python code/script
   
    return HttpResponse(template.render(request)) 


@login_required(login_url='django.contrib.auth.views.login') 
def show2(request):
    template = loader.get_template('polls/basic_table.html')

    # ... your python code/script

    #return HttpResponse(template.render(request))
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]

    #template = loader.get_template('polls/show.html')
    #context = {
      #   'latest_question_list': latest_question_list,
      #  }
    return HttpResponse(template.render(request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)







      
  
