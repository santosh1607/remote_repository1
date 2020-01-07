from django.shortcuts import render
from feedbackapp.models import FeedbackData
from feedbackapp.forms import FeedbackForm
from django.http.response import HttpResponse
import datetime as dt
date1=dt.datetime.now()
def Feedbackview(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name1=request.POST.get("name")
            ratting1=request.POST.get("ratting")
            feedback1=request.POST.get("feedback")
            data=FeedbackData(
                name=name1,
                ratting=ratting1,
                date=date1,
                feedback=feedback1

            )
            data.save()
            fform=FeedbackForm()
            feedbacks=FeedbackData.objects.all()
            return render(request,'feedback.html',{'abc':fform,'feedbacks':feedbacks})
        else:
            return HttpResponse("missing feedback data")

    else:
        fform=FeedbackForm()
        feedbacks=FeedbackData.objects.all()
        return render(request,'feedback.html',{'abc':fform,'feedbacks':'feedbacks'})



