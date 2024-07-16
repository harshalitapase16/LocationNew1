from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

# Create your views here.
class CountryView(View):
 def get(self, request, id=None):
   if id:
      countryobj = CountryModel.objects.get(id=id)
      if countryobj.is_active:
       countryobj.is_active = False
       countryobj.save()
      else:
       countryobj.is_active = True
       countryobj.save()
      return redirect('/')
   else:
    countryobj = CountryModel.objects.all()
    return render(request,'country.html',{'country':countryobj})
  
 def post(self, request, id=None):
   if id:
     countryobj = CountryModel.objects.get(id=id)
     countryobj.delete()
   else:
    country_name = request.POST.get('country_name')
    country_slug = request.POST.get('country_slug')
    code = request.POST.get('code')
    flag = request.FILES.get('flag')
    state_available = request.POST.get('is_state_available')
    if  not state_available:
      state_available = False

    # agar code aur slug exist hai pehle hi to msg dikhaye
    if CountryModel.objects.filter(slug=country_slug).exists():
     messages.error(request, f"{country_slug} is already exists!!")
     return redirect('/')
			
    if CountryModel.objects.filter(code=code).exists():
     messages.error(request,f"{code} is already exists!!")
     return redirect('/')
       
    CountryModel.objects.create(name = country_name,
                                slug = country_slug,
                                code = code,
                                flag = flag,
                                is_state_available = state_available)
   return redirect('/')
  
class UpdateCountryView(View):
     def get(self, request, id=None):
        countryobj = CountryModel.objects.get(id=id)
        return render(request, 'countryupdate.html', {'country': countryobj})

     def post(self, request, id=None):
        country_name = request.POST.get('country_name')
        country_slug = request.POST.get('country_slug')
        code = request.POST.get('code')
        flag = request.FILES.get('flag')
        state_available = request.POST.get('is_state_available')
        
        countryobj = CountryModel.objects.get(id=id)
        
        if country_name:
            countryobj.name = country_name
        if country_slug:
            countryobj.slug = country_slug
        if code:
            countryobj.code = code
        if flag:
            countryobj.flag = flag
            
        if state_available:
           state_available = True               
           countryobj.is_state_available = state_available
        else:
           countryobj.is_state_available = False 

        if CountryModel.objects.filter(slug=country_slug).exists():
         messages.error(request, f"{country_slug} is already exists!!")
         return redirect('/')
       
        if CountryModel.objects.filter(code=code).exists():
         messages.error(request,f"{code} is already exists!!")
         return redirect('/')
        
        countryobj.save()
        return redirect('/')


class StateView(View):
  def get(self, request, id=None):
    countryobj = CountryModel.objects.get(id=id)
    stateobj = StateModel.objects.filter(country=countryobj)
  
    return render(request,'state.html',{'country':countryobj, 'state':stateobj})
  
  def post(self, request,id=None):
    state_name = request.POST.get('state_name')
    state_slug = request.POST.get('state_slug')
    language = request.POST.get('language')
    population = request.POST.get('population')
   
    countryobj = CountryModel.objects.get(id=id)
    StateModel.objects.create(country = countryobj, 
                              statename = state_name,
                              stateslug = state_slug,
                              language = language,
                              population = population)
    return redirect(f'/state/{id}')
  
  def delete_post(self, request, id=None):
    stateobj = StateModel.objects.get(id=id)
    stateobj.delete()
    return redirect('/state/')
  

class UpadtestateView(View):
  def get(self, request, id=None):
    stateobj = StateModel.objects.get(id=id)
    countryobj = stateobj.country
    return render(request, 'updatestate.html', {'state':stateobj,'country':countryobj})
  
  def post(self, request, id=None):
    state_name = request.POST.get('state_name')
    state_slug = request.POST.get('state_slug')
    language = request.POST.get('language')
    population = request.POST.get('population')
    
    stateobj = StateModel.objects.get(id=id)
    stateobj.statename = state_name
    stateobj.stateslug = state_slug
    stateobj.language = language
    stateobj.population = population
    stateobj.save()
    return redirect(f'/static/')

class CityView(View):
  def get(self,request, id=None):
    return render(request, 'city.html')