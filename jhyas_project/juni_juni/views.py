from django.shortcuts import render, redirect
from .models import Poet
#from django.db import IntegrityError
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCanAddmoreField, UpdateForm
from django.contrib.auth.decorators import login_required


# class PostListView(ListView):
#     model = Poet
#     template_name = 'jhyas_project/home.html'
#     context_object_name = 'poets'



class PoetCreateView(LoginRequiredMixin,CreateView):
    model = Poet
    fields = ['headline', 'Description']
    

    
    def form_valid(self, form):
        form.instance.lekhak = self.request.user
        return super().form_valid(form)
    
def home(request):
    poets = Poet.objects.all()
    context = {
        'poets':poets
    }
    return render(request, 'juni_juni/home.html', context)

def poet_detail(request, pk):
    poet= Poet.objects.get(id=pk)
    context ={
        'poet':poet
    }
    return render(request, 'juni_juni/detail.html', context)



# def create(request):
#     if request.method == 'POST':
#         headline = request.POST['headline']
#         Description = request.POST['description']
#         poet=Poet.objects.create(headline=headline, Description=Description)
#         poet.save()
#         return redirect('home')
    
#     else:
#         headline=request.POST
#         Description=request.POST
#         return render(request, 'juni_juni/poet_create.html',{'headline':headline, 'Description':Description})
    
def register(request):
    if request.method == 'POST':
        form = UserCanAddmoreField(request.POST)
    
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Your Account Created Sucessfullys')
            return redirect('poet-home')
    else:
        form = UserCanAddmoreField()    
    return render(request, 'juni_juni/register.html',{'form':form})




def delete(request, pk):
    
        
    tasks = Poet.objects.get(id=pk)
    if request.method == 'POST':
        tasks.delete()
        messages.success(request, f'{tasks} is Deleted successfully!')
        return redirect('poet-home')
        
    else:
        context = {
            'tasks':tasks
        }
    return render(request, 'juni_juni/delete.html',context)

@login_required
def update(request):
    if request.method == 'POST':
        u_form = UpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('poet-home')
    else:
        u_form = UpdateForm()
        return render(request, 'juni_juni/update.html', {'u_form':u_form})