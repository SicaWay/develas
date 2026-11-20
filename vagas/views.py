from django.http import Http404
from django.shortcuts import render
from vagas.dados import VAGAS


def home(request):
    return render(request, "vagas/home.html", {"total": len(VAGAS)})


def mural(request):
    modalidade = request.GET.get("modalidade", "")
    if modalidade:
        vagas = []
        for vaga in VAGAS:
            if vaga["modalidade"] == modalidade:
                vagas.append(vaga)
    else:
        vagas = VAGAS
    contexto = {
        "vagas": vagas,
        "total": len(vagas),
        "modalidade": modalidade,
    }
    return render(request, "vagas/mural.html", contexto)


def detalhe(request, vaga_id):
    for vaga in VAGAS:
        if vaga["id"] == vaga_id:
            return render(request, "vagas/detalhe.html", {"vaga": vaga})
    raise Http404("Vaga não encontrada")

def sobre(request):
    return render(request, "vagas/sobre.html")