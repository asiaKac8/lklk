from django.db import models

# Create your models here.

# model for iris prediction
class PredictionResults(models.Model):
    class Meta:
        verbose_name_plural = "Iris User Input History "
    id = models.AutoField(primary_key=True)
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=30)
    def __str__(self):
        return self.classification


# iris import export
class IrisImportExport(models.Model):
    class Meta:
        verbose_name_plural = "Iris Imported from CSV "
    id = models.AutoField(primary_key=True)
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=30)
    def __str__(self):
        return self.classification


#
class UniversalTable(models.Model):
    class Meta:
        verbose_name_plural = "UniversalTable"
    id = models.AutoField(primary_key=True)
    a2 = models.FloatField()
    a3 = models.FloatField()
    a4 = models.FloatField()
    a5 = models.FloatField()
    a6 = models.FloatField()
    a7 = models.FloatField()
    a8 = models.FloatField()
    a9 = models.FloatField()
    a10 = models.FloatField()
    c1 = models.CharField(max_length=40)
    def __str__(self):
        #return str(self.id_dana)
        return str(self.c1)



# universal model 
class Zbior(models.Model):
    class Meta:
        verbose_name_plural = "01 Zbior"
    id_zbior = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwa



class Atrybut(models.Model):
    class Meta:
        verbose_name_plural = "02 Atrybut"
    id_atrybut = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)
    id_zbior = models.ForeignKey(Zbior, on_delete=models.CASCADE)
    def __str__(self):
        return self.nazwa


class Klasa(models.Model):
    class Meta:
        verbose_name_plural = "03 Klasa"
    id_klasa = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwa



class Obserwacja(models.Model):
    class Meta:
        verbose_name_plural = "04 Obserwacja"
    id_obserwacja = models.AutoField(primary_key=True)
    id_klasa = models.ForeignKey(Klasa, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.id_obserwacja)



class Dana(models.Model):
    class Meta:
        verbose_name_plural = "05 Dana"
    id_dana = models.AutoField(primary_key=True)
    wartosc = models.FloatField()
    id_atrybut = models.ForeignKey(Atrybut, on_delete=models.CASCADE)
    id_obserwacja = models.ForeignKey(Obserwacja, on_delete=models.CASCADE)
    def __str__(self):
        #return str(self.id_dana)
        return str(self.wartosc)
