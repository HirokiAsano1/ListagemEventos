from django.shortcuts import render
from datetime import date
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http.response import Http404, HttpResponseRedirect
from datetime import date
from django.urls import reverse

from agenda.models import Evento
# Create your views here.

def listar_eventos(request):
    eventos = Evento.objects.exclude(data__lt=date.today())
    return render(request, "agenda/listar_eventos.html", context={"eventos": eventos})

def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento = Evento.objects.get(id=id)
    return render(
        request,
         "agenda/exibir_evento.html", 
         context={"evento": evento})

def participar(request):
    evento_id = request.POST.get("evento_id")
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes +=1
    evento.save()
    return HttpResponseRedirect(reverse('exibir_evento',args=(evento_id,)))
        