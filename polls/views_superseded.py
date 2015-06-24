#superseded from this point down
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_R.html', context)

    """ #version with more writing :)
    from django.template import loader,RequestContext

    template = loader.get_template('polls/index_R.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))
    """
    """ #hardcoded response (no template)
    from django.http import HttpResponse
    output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output)
    """

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    """ #version with model-coupled writing
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    return render(request, 'polls/detail.html', {'question': question})
    """ #mockup hardcoded response
    return HttpResponse("You're looking at question %s." % question_id)
    """

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
     #mockup hardcoded response
    return HttpResponse("You're looking at the results of question %s." % question_id)