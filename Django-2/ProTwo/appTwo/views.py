from django.shortcuts import render
# from appTwo.models import User
from appTwo.forms import NewForm
# Create your views here.
def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    # users_list = User.objects.order_by('first_name')
    # user_dict = {'users':users_list}
    # return render(request,'appTwo/users.html',context=user_dict)
    form = NewForm()

    if request.method == 'POST':
        form = NewForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("ERROR")
    return render(request,'appTwo/users.html',{'form':form})