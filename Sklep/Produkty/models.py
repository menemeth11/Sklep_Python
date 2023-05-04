from django.db import models


# Create your models here.
class Kategorie(models.Model):
    nazwa = models.CharField(max_length=60) #varchar(60)

    def __str__(self):
        return self.nazwa #wyświetlana nazwa produktu w panelu admin

    class Meta:
        verbose_name = "Kategoria" #liczba pojedyncza
        verbose_name_plural = "Kategorie" #liczba mnoga


class Producenci(models.Model):
    nazwa = models.CharField(max_length=60) #varchar(60)
    opis = models.TextField(blank=True) #text, opis nie jest wymagalny

    def __str__(self):
        return self.nazwa #wyświetlana nazwa produktu w panelu admin

    class Meta:
        verbose_name = "Producent" #liczba pojedyncza
        verbose_name_plural = "Producenci" #liczba mnoga


class Stan(models.Model):
    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Stan" #liczba pojedyncza
        verbose_name_plural = "Stany" #liczba mnoga


class Produkty(models.Model):
    kategoria = models.ForeignKey(Kategorie, on_delete=models.CASCADE, null=True,blank=True)
    producent = models.ForeignKey(Producenci, on_delete=models.CASCADE, null=True)
    stan = models.ForeignKey(Stan, on_delete=models.CASCADE, null=True, blank=True)
    nazwa = models.CharField(max_length=100) #varchar(100)
    opis = models.TextField(blank=True) #text, opis nie jest wymagalny
    cena = models.DecimalField(max_digits=12,decimal_places=2) #12 cyfr, 2po przecinku

    def __str__(self):
        return self.nazwa #wyświetlana nazwa produktu w panelu admin

    class Meta:
        verbose_name = "Produkt" #liczba pojedyncza
        verbose_name_plural = "Produkty" #liczba mnoga