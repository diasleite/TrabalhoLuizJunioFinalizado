# -*- coding: utf-8 -*-

from django.utils.functional import total_ordering

from django.db import models

Status_Lista = (
    ('A','Ativo'),
    ('I','Inativo')
)

class contato(models.Model):
    status = models.CharField(verbose_name=u'Status',max_length=1, default='A', choices=Status_Lista)
    nome = models.CharField(verbose_name=u'Nome',max_length=100)
    doc = models.CharField(verbose_name=u'CPF/CNPJ',max_length=20, unique=True)
    telefone = models.CharField(verbose_name=u'Telefone',max_length=25, null=True,blank=True)#para um campo poder ser opcional null=Treu e blank=True
    logradouro = models.CharField(verbose_name=u'Logradouro',max_length=20)
    endereco = models.CharField(verbose_name=u'Endereço',max_length=40)
    numero = models.PositiveIntegerField(verbose_name=u'Numero')
    bairro = models.CharField(verbose_name=u'Bairro',max_length=20)
    cidade = models.CharField(verbose_name=u'Cidade',max_length=20)
    estado = models.CharField(verbose_name=u'Estado',max_length=20)
    dataNascimento = models.DateField(verbose_name=u'Data Nascimento', null=True, blank=True)
    dataCadastro = models.DateField(verbose_name=u'Data Cadastro')
    limiteCompra = models.DecimalField(decimal_places=2,max_digits=18,verbose_name=u'Limite para compra',default=0, help_text='Valor limite para compra')
    email = models.EmailField(verbose_name=u'E-mail',max_length=100)

    class Meta:
        ordering = ['nome', 'cidade']


    def __unicode__(self):
      return self.nome+' | '+self.cidade+' | '

Status_produto=(
    ('A','Ativo'),
    ('I','Inativo')
)
GruproLista=(
    ('Limpeza','Limpeza'),
    ('Açougue','Açougue'),
    ('Perfumaria','Perfumaria'),
    ('Alimentos','Alimentos'),
    ('Outro','Outro')

)
Lista_Unidades=(
    ('Kg','Kilo'),
    ('UN','Unidade'),
    ('g','Grama'),
    ('Cx','Caixa'),
    ('Kg','Kilo')
)
class produto(models.Model):
    status = models.CharField(verbose_name=u'Status',max_length=1, default='A',choices=Status_produto)
    descricao = models.CharField(verbose_name=u'Descriçao Produto',max_length=100, null=True, blank=True)
    grupo = models.CharField(verbose_name=u'Grupro',max_length=40,choices=GruproLista)
    barrasCod = models.CharField(verbose_name=u'Codigo de Barras', max_length=13)
    unidade = models.CharField(verbose_name=u'Unidade de Calculo', max_length=25, choices=Lista_Unidades)
    custo = models.DecimalField(verbose_name=u'Valor de Custo',decimal_places=2,max_digits=10,default=0)
    frete = models.DecimalField(verbose_name=u'Valor de Frete',decimal_places=2,max_digits=10,default=0)
    porcentagemSobreVenda = models.DecimalField(verbose_name=u'Porcentagem sobre venda(%)',decimal_places=2,max_digits=10,default=0)
    PrecoVenda=models.DecimalField(verbose_name=u'Preço de Venda',decimal_places=2,max_digits=10,default=0)
    quantidade = models.IntegerField(verbose_name=u'QuantidadeEmEstoque',default=0)

    def __unicode__(self):
     return self.descricao+' | '+self.barrasCod+' | '+self.status


