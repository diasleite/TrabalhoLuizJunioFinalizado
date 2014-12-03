# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from models import *
from Cadastro.views import *
from Cadastro.forms import ContatoForm, ProdutoForm


def homepage(request):


       return render(request,'homepage.html', locals())


def excluir_contato(request, contato_id=None):
    if contato_id:
        contato.objects.get(pk=contato_id).delete()

    return redirect('/contato/search/')


def edita_contato(request, contato_id=None):
        if contato_id:
            v_contato = contato.objects.get(pk=contato_id)
        else:
            v_contato = None

        if request.method == 'POST' :
            form =  ContatoForm(request.POST, instance = v_contato)

            if form.is_valid():
                resultado = form.save()
                if resultado:
                    return redirect('/contato/search/')
        else:
            form = ContatoForm(instance=v_contato)

        return render(request,'CadastroContatoNovo.html', locals())


def Contatos(request):
    v_contatos = contato.objects.all()

    return render(request, 'MostrarContatos.html', locals())

def search_contato(request):
   # pesquisa COnTem v_contatos = contato.objects.all().filter(email__icontains="hotmail")
    filtradopor = " "
    selecaoCombobox = None
    valorProcurado = None
    msgAoUsuario = None
    v_contatos = contato.objects.all()
    if request.method == 'POST':
        if request.POST.get("searchcombobox",""):
            selecaoCombobox = request.POST.get("searchcombobox","")
            if selecaoCombobox == "Select" or request.POST.get("valorProcurado","") == "" or request.POST.get("valorProcurado","") == None:
                    msgAoUsuario = "Preencha o Tipo e campo Pesquisa"
                    return render(request, 'search.html', locals())
            if request.POST.get("valorProcurado",""):
             valorProcurado = request.POST.get("valorProcurado","")
            if selecaoCombobox == "Nome":
                filtradopor = "Filtro: Nome do Contato = "+valorProcurado
                v_contatos = contato.objects.all().filter(nome__icontains=valorProcurado)
                qtdadeRegis = v_contatos.count();
            if selecaoCombobox == "Cidade":
                filtradopor = "Filtro: Cidade = "+valorProcurado
                v_contatos = contato.objects.all().filter(cidade__icontains=valorProcurado)
                qtdadeRegis = v_contatos.count();
            if selecaoCombobox == "E-mail":
                filtradopor = "Filtro: Endereco de email = "+valorProcurado
                v_contatos = contato.objects.all().filter(email__icontains=valorProcurado)
                qtdadeRegis = v_contatos.count();
            return render(request, 'search.html', locals())
    else:
        return render(request, 'search.html', locals())


#PRODUTOS

def edita_produto(request, produto_id=None):
        if produto_id:
            v_produto = produto.objects.get(pk=produto_id)
        else:
            v_produto = None

        if request.method == 'POST':
            form = ProdutoForm(request.POST, instance = v_produto)

            if form.is_valid():
                resultado = form.save()
                if resultado:
                    return redirect('/produto/search')
        else:
            form = ProdutoForm(instance=v_produto)

        return render(request,'CadastroProdutoNovo.html', locals())


def produtos(request):
    v_produtos = produto.objects.all()

    return render(request, 'MostrarProdutos.html', locals())

def excluir_produto(request, produto_id=None):
    if produto_id:
        produto.objects.get(pk=produto_id).delete()

    return redirect('/produto/search/')


def search_produto(request):
   # pesquisa COnTem v_contatos = contato.objects.all().filter(email__icontains="hotmail")
    filtradopor = " "
    selecaoCombobox = None
    valorProcurado = None
    msgAoUsuario = None
    v_produtos = produto.objects.all()

    if request.method == 'POST':
        if request.POST.get("searchcombobox",""):
            selecaoCombobox = request.POST.get("searchcombobox","")
            if selecaoCombobox == "Select" or request.POST.get("valorProcurado","") == "" or request.POST.get("valorProcurado","") == None:
                    msgAoUsuario = "Preencha o Tipo e campo Pesquisa"
                    return render(request, 'searchProduto.html', locals())
            if request.POST.get("valorProcurado",""):
             valorProcurado = request.POST.get("valorProcurado","")
            if selecaoCombobox == "Descricao":
                filtradopor = "Filtro: Nome do Produto = "+valorProcurado
                v_produtos = produto.objects.all().filter(descricao__icontains=valorProcurado)
                qtdadeRegis = v_produtos.count();
            if selecaoCombobox == "CodBarras":
                filtradopor = "Filtro: Codigo de barras = "+valorProcurado
                v_produtos = produto.objects.all().filter(barrasCod=valorProcurado)
                qtdadeRegis = v_produtos.count();
            if selecaoCombobox == "Status":
                filtradopor = "Filtro: Status = "+valorProcurado
                v_produtos = produto.objects.all().filter(status__icontains=valorProcurado)
                qtdadeRegis = v_produtos.count();
            return render(request, 'searchProduto.html', locals())
    else:
        return render(request, 'searchProduto.html', locals())




#faltaImplementaçao
def falta_implementacao(request):

    url = request.get_full_path()


    return render(request, 'FuncaoNaoImplementada.html', locals())

#about
def about(request):



    return render(request, 'about.html', locals())

