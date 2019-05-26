from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponseRedirect,reverse,get_object_or_404
from django.views.generic.base import View
from .form import crudForm
from .models import Crud
from django.contrib.auth.models import User
class CrudView(View):
    """ This view will get the from and return on all the object list from the databace """
    template_name = 'index.html'
    form_name = crudForm
    def get_context_data(self, **kwargs):
        data = Crud.objects.all()
        context = {'form':self.form_name,'data':data}
        return context
    def get(self, request, *args, **kwargs):
        # form = self.form_name
        context = self.get_context_data()
        # print(context)
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form = self.form_name(request.POST)
        if form.is_valid():
            form.save()
        else:
            
            print('form is not valid',form.errors)
        context = self.get_context_data()
        return render(request,self.template_name,context)

def delete(request,id):
    """This function will delete the exisiting object"""
    iteam = get_object_or_404(Crud,id=id)
    iteam.delete()
    return HttpResponseRedirect(reverse('home'))

def update(request,id):
    """ This function will update the selcted object"""
    iteam2 = get_object_or_404(Crud,id=id)
    if request.method == 'GET':
        form = crudForm(instance=iteam2)
        data = Crud.objects.all()
        context = {'form':form,'data':data}
        return render(request,'index.html',context)
    else:
        form = crudForm(request.POST,instance=iteam2)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('home'))