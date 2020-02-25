from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.

def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_item = List.objects.all
            messages.success(request, ('Item has been added to the list!'))
            return render(request, 'home.html', {'all_items':all_item})
    else:   
        all_item = List.objects.all
        return render(request, 'home.html', {'all_items':all_item})




def about(request):
    return render(request, 'about.html', {})

def remove(request, item_id):
    item = List.objects.get(pk=item_id)
    print(item_id)
    item.delete()
    messages.info(request, ('Item has been delete from the list!'))
    return redirect('home')
