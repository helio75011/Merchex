from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def band_detail(request, id):  # notez le paramètre id supplémentaire
   return render(request,
          'listings/band_detail.html',
         {'id': id}) # nous passons l'id au modèle

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')