from django.db import models
from django.utils.translation import gettext_lazy as _

class Supplier(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Nome do fornecedor"
    )

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.name



class Invoice(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name="Fornecedor"
    )
    file = models.FileField(
        upload_to='invoices/',
        verbose_name="Ficheiro PDF"
    )
    invoice_number = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Número da fatura"
    )
    invoice_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da fatura"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em"
    )

    class Meta:
        verbose_name = "Fatura"
        verbose_name_plural = "Faturas"

    def __str__(self):
        return f"Fatura {self.invoice_number}"



class PQRDocument(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    file = models.FileField(upload_to='pqr/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class DailyRevenue(models.Model):
    date = models.DateField(verbose_name=_("Data"))
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Valor (€)")
    )

    class Meta:
        verbose_name = _("Receita diária")
        verbose_name_plural = _("Receitas diárias")

    def __str__(self):
        return f"{self.date} - {self.amount} €"


class Expense(models.Model):
    date = models.DateField(verbose_name=_("Data"))
    description = models.CharField(
        max_length=255,
        verbose_name=_("Descrição")
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Valor (€)")
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Fornecedor")
    )

    class Meta:
        verbose_name = _("Despesa")
        verbose_name_plural = _("Despesas")

    def __str__(self):
        return f"{self.description} - {self.amount} €"



    def __str__(self):
        return f"{self.description} - {self.amount} €"


