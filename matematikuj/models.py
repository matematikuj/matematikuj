from django.db import models
Rocniky = [('6',"6.ročník"),('7',"7.ročník"),('8',"8.ročník"),('9',"9.ročník"),]

# databáze názvu menu + výsledný odkaz
class Menu_bloky(models.Model): 
    nazev = models.CharField(max_length = 30)
    odkaz = models.CharField(max_length = 50)

    def __str__(self):
        return self.nazev


class Tema(models.Model):
    ZS = 'ZŠ'
    SS = 'SŠ'
    SKOLA = (('1',ZS),('2',SS),)
    skola = models.CharField(max_length=2, choices=SKOLA, default=ZS)
    tema = models.CharField(max_length=30)
    podtema = models.CharField(max_length=50, blank=True)
    kapitola = models.CharField(max_length=50, blank=True)
    padding_left = 0
    padding_right = 0 #pomoc do view na počítaní velikosti okna

    def __str__(self):
        if self.kapitola == '':
            if self.podtema == '':
                return self.tema
            else:
                return self.tema + '|' + self.podtema
        else:
            return self.tema + '| ' + self.podtema + '| ' + self.kapitola
    class Meta:
        verbose_name = 'Téma'
        verbose_name_plural = 'Témata'
        ordering = ["tema","podtema","kapitola"]

'''
class Tema_ZS(models.Model):

    tema = models.CharField(max_length=50, blank=True)
    kapitola = models.CharField(max_length=50, blank=True)
    padding_left = 0
    padding_right = 0 #pomoc do view na počítaní velikosti okna

    def __str__(self):
        if self.kapitola == '':
            return self.tema
        else:
            return self.tema + '| ' + self.kapitola
    class Meta:
        verbose_name = 'Téma ZŠ'
        verbose_name_plural = 'Témata pro ZŠ'
'''        

class Pocetni_priklady(models.Model):
    tema = models.ForeignKey(Tema, on_delete = models.CASCADE)
    zadani = models.TextField()
    reseni = models.TextField()
    ident = 1
    ukaz_reseni = False

    class Meta:
        verbose_name = 'Příklad'
        verbose_name_plural = 'Příklady'

'''
class Pocetni_priklady_ZS(models.Model):
    tema = models.ForeignKey(Tema_ZS, on_delete = models.CASCADE)
    typ = models.CharField(max_length=50, blank=True)
    rocnik = models.CharField(max_length=15,choices=Rocniky,default='6')
    zadani = models.TextField()
    reseni = models.TextField()
    ident = 1
    ukaz_reseni = False

    def __str__(self):
        return self.tema
    class Meta:
        verbose_name = 'Příklad na ZŠ'
        verbose_name_plural = 'Příklady pro ZŠ'
'''
class Priklady_do_testu_k_maturite(models.Model):
    zadani = models.TextField()
    reseni = models.TextField()
    priklad_v_testu = models.IntegerField()
    A = models.CharField(max_length=300)
    B = models.CharField(max_length=300)
    C = models.CharField(max_length=300)
    D = models.CharField(max_length=300)
    E = models.CharField(max_length=300)
    Spravna_odpoved = models.CharField(max_length=1)

# Create your models here.