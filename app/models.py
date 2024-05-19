from django.db import models




class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)
    class Meta:
        abstract = True

class Unversity(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title



class Sponsor(BaseModel):

    class Choice(models.TextChoices):
        NEW = 'yangi','Yangi'
        MADIRATION =  'madiratsiyada', 'Madiratsiyada'
        DONE = 'tasdiqlangan', 'Tasdiqlangan'
        CANCEL = 'bekor_qilingan', 'Bekor qilingan'

    class SponsorChoice(models.TextChoices):
        YURIDIK = 'yuridik', 'Yuridik'
        JISMONIY = 'jismoniy', 'Jismoniy'

    class PaymentChoise(models.TextChoices):
        CARD = 'plastik_karta', 'Plastik karta'
        CASH = 'naqt_pul', 'Naqt pul'

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    organization = models.CharField(max_length=100)
    sponsor_type = models.CharField(max_length=100, choices=SponsorChoice.choices, default=SponsorChoice.JISMONIY)
    conditions = models.CharField(max_length=20, choices=Choice.choices , default=Choice.NEW )
    payment_type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.full_name
    

class Student(BaseModel):

    class Choise(models.TextChoices):
        BAKALAVR = 'bakalavr', 'Bakalavr'
        MAGISTER = 'magister', 'Magister'

    full_name = models.CharField(max_length=100)
    student_type = models.CharField(max_length=100, choices=Choise.choices, default=Choise.BAKALAVR)
    unversity = models.ForeignKey(Unversity, on_delete=models.PROTECT)
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.full_name


class StudentSponsor(BaseModel):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.PROTECT,related_name='student_sponsors')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    student = models.ForeignKey(Student, on_delete=models.PROTECT,related_name='student_sponsors')

    
    def __str__(self) -> str:
        return self.sponsor
    
   



