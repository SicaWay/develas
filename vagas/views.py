from django.shortcuts import render
from vagas.dados import VAGAS

def home(request):
    return render(request, "vagas/home.html")

def mural(request):
    contexto = {
        "vagas": VAGAS,
        "total": len(VAGAS),
    }
    return render(request, "vagas/mural.html", contexto)