from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
import time
from .models import FibonacciCalculator



def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': [1,2,3,4,5,],
    }
    return HttpResponse(template.render(context, request))

def calculate(request):
    start_time = time.time()
    n = request.POST.get('number')
    fib = FibonacciCalculator.get_fibonacci_seq(int(n))
    return render(request, 'index.html', {
            'fibonacci_sequence': fib[:-1],
            'nth_fib_num': fib[-1],
            'nth_number': n,
            'response_time': round((time.time() - start_time) * 1000, 3),
        })
