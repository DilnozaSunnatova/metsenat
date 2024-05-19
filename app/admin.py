from django.contrib import admin
from . models import Sponsor, Student, StudentSponsor, Unversity, BaseModel

admin.site.register(Sponsor)
admin.site.register(Student)
admin.site.register(StudentSponsor)
admin.site.register(Unversity)
