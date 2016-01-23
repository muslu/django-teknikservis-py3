from django.utils import timezone
from django.utils.crypto import get_random_string
from django.db import models




class Teknisyen ( models.Model ) :
    Aktif               =       models.BooleanField(default = True)
    AdSoyad             =       models.CharField ( 'Adı Soyadı', max_length = 250 )
    KayitTarihi         =       models.DateField ( "Kayıt Tarihi", default=timezone.now)

    def __unicode__(self):
        return self.AdSoyad

    class Meta:
        verbose_name_plural             =       "Teknisyenler"
        verbose_name                    =       "Teknisyen"


    def Yazdir ( self ) :
        return '<a href="/yazdir/{}" target="_blank">Yazdır</a>'.format(self.id)
    Yazdir.short_description       =       'Yazdır'
    Yazdir.allow_tags              =       True

    def EkAlanTest(self):
        return self.AdSoyad.replace(' ', '_______')
    EkAlanTest.short_description       =       'Burası alanın başlığı'




class Musteriler ( models.Model ) :
    Aktif               =       models.BooleanField(default = True)
    Kodu                =       models.CharField ( 'Müşteri Kod', default=''.join(get_random_string(length=8, allowed_chars='1234567890')), max_length = 8, unique=True)
    Unvan               =       models.CharField ( 'Ticari Ünvan', max_length = 250 )
    Yetkili             =       models.CharField ( 'Yetkili Adı Soyadı', max_length = 250 )
    Telefon             =       models.CharField ( 'Telefon', max_length = 13, blank = True )
    KayitTarihi         =       models.DateField ( "Kayıt Tarihi", default=timezone.now)

    def __str__(self):
        return "Müşteri Kodu: {} - Adı: {}".format(self.Kodu, self.Yetkili)

    class Meta:
        verbose_name_plural             =       "Müşteriler"
        verbose_name                    =       "Müşteri"


    def AramaYap ( self ) :
        if self.Telefon:
            return '<a href="tel:{}" target="_blank">Numarayı Ara</a>'.format(self.Telefon)
        else:
            return 'Telefon No kayıt edilmedi'

    AramaYap.short_description       =       'Ara'
    AramaYap.allow_tags              =       True



class Durumlar (models.Model ):
    Durumu              =       models.CharField('Durum', max_length=30, help_text='Metin alanının altında kayıt girerken yardımcı olabilecek konuları anlatan kısa bir açıklama yazabilirsiniz.')

    def __unicode__(self):
        return self.Durumu

    class Meta:
        verbose_name_plural             =       "Durumlar"
        verbose_name                    =       "Durum"



class Aksesuarlar (models.Model ):
    Adi              =       models.CharField('Adi', max_length=30, help_text='Ürünle beraber getirilen tüm aksesuarlar. Örn: Batarya, Çanta' )

    def __unicode__(self):
        return self.Adi

    class Meta:
        verbose_name_plural             =       "Aksesuarlar"
        verbose_name                    =       "Aksesuar"




class ServisForm ( models.Model ) :
    Musteri             =       models.ForeignKey ( Musteriler )
    TeslimEden          =       models.CharField ( 'Teslim Eden', max_length = 130 )
    # TeslimAlan          =       models.ForeignKey ( Teknisyen, default=int(Teknisyen.objects.get(id=1).id)  )
    TeslimAlan          =       models.ForeignKey ( Teknisyen  )
    FormNo              =       models.CharField ( 'Form No', default=''.join(get_random_string(length=8, allowed_chars='1234567890')), max_length = 8, unique=True)
    KayitTarihi         =       models.DateTimeField ( "Kayıt Tarihi", default=timezone.now)

    def __unicode__(self):
        return self.FormNo

    class Meta:
        verbose_name_plural             =       "Formlar"
        verbose_name                    =       "Servis Form"

    def Yazdir ( self ) :
        return '<a href="/yazdir/{}" target="_blank">Yazdır</a>'.format(self.id)
    Yazdir.short_description       =       'Yazdır'
    Yazdir.allow_tags              =       True




class Urunler ( models.Model ) :
    ServisFormu         =       models.ForeignKey ( ServisForm )
    Cins                =       models.CharField ( 'Cinsi', max_length = 30 )
    Marka               =       models.CharField ( 'Marka', max_length = 50 )
    Model               =       models.CharField ( 'Model', max_length = 50 )
    SeriNo              =       models.CharField ( 'Seri No', max_length = 250 )
    GarantiBitis        =       models.DateField ( "Garanti Bitiş", default=timezone.now )
    Sikayet             =       models.TextField ( 'Şikayet' )
    Aksesuar            =       models.ManyToManyField ( Aksesuarlar, blank=True )
    Durum               =       models.ForeignKey ( Durumlar )
    Not                 =       models.TextField ( 'Yapılan İşlemler', blank=True )
    TeslimatTarihi      =       models.DateField ( "Teslimat Tarihi", default=timezone.now, blank=True )
    def __unicode__(self):
        return "{} {} {}".format(self.Cins, self.Marka, self.Model)

    class Meta:
        verbose_name_plural             =       "Ürünler"
        verbose_name                    =       "Ürün"
