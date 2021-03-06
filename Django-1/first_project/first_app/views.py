from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,WebPage,AccessRecord
from . import forms

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # my_dict = {'insert_me':"Hello I am from views.py"}
    return render(request,'first_app/index.html',context=date_dict)

def form_as_view(request):
    form = forms.FormName()
    if request.method == 'POST':
      form = forms.FormName(request.POST)

      if form.is_valid():
        print("VALIDATION IS COMPLETE")
        print("NAME: "+form.cleaned_data['name'])
        print("EMAIL: "+form.cleaned_data['email'])
        print("TEXT: "+form.cleaned_data['text'])

    return render(request,'first_app/formpage.html',{'form':form})
