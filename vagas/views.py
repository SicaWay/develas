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

def detalhe_vaga(request, vaga_id):
    # Procura na lista VAGAS aquela cujo id corresponde ao parâmetro da URL
    vaga_encontrada = None
    for vaga in VAGAS:
        if vaga["id"] == vaga_id:
            vaga_encontrada = vaga
            break
            
    contexto = {
        "vaga": vaga_encontrada
    }
    return render(request, "vagas/detalhe.html", contexto)