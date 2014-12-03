# -*- coding: utf-8 -*-
from django import forms

from django.db import models

from django.forms import ModelForm
from models import *

class ContatoForm(ModelForm):
        class Meta:
          model = contato

class ProdutoForm(ModelForm):
        class Meta:
          model = produto

class searchForm(ModelForm):
         Pesquisa = forms.CharField(max_length=100)