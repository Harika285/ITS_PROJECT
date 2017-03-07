from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
<<<<<<< HEAD
from django.http import HttpResponseRedirect
from .models import Question
from django.shortcuts import render_to_response
#import account.views
=======
from .models import Question
from django.shortcuts import render_to_response

>>>>>>> 06383a7ea820e0cbefd0cb199e365aa1ead6f5b9

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

<<<<<<< HEAD
    template = loader.get_template('polls/show.html')
=======
    template = loader.get_template('polls/index.html')
>>>>>>> 06383a7ea820e0cbefd0cb199e365aa1ead6f5b9
    context = {
         'latest_question_list': latest_question_list,
        }

    return HttpRespnse(template.render(context,request))
<<<<<<< HEAD
def show1(request):
    template = loader.get_template('polls/chart-chartjs.html')

    # ... your python code/script
   
    return HttpResponse(template.render(request))  
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

#    return HttpRespnse(template.render(context,request))
=======
>>>>>>> 06383a7ea820e0cbefd0cb199e365aa1ead6f5b9


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

<<<<<<< HEAD
#class SignupView(account.views.SignupView):

 #   def after_signup(self, form):
  #      self.update_profile(form)
   #     super(SignupView, self).after_signup(form)

    #def update_profile(self, form):
     #   profile = self.created_user.profile  # replace with your reverse one-to-one profile attribute
      #  profile.some_attr = "some value"
       # profile.save()
=======
>>>>>>> 06383a7ea820e0cbefd0cb199e365aa1ead6f5b9


      
  
