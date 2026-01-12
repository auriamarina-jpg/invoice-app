from django.shortcuts import render, redirect
from .models import Fornecedor

def home(request):
    return render(request, "suppliers/home.html")

def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, "suppliers/fornecedor_list.html", {
        "fornecedores": fornecedores
    })

def fornecedor_create(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")

        Fornecedor.objects.create(
            nome=nome,
            email=email,
            telefone=telefone
        )
        return redirect("fornecedor_list")

    return render(request, "suppliers/fornecedor_form.html")


