from rest_framework.serializers import Serializer, ModelSerializer
from .models import Sponsor, Student, StudentSponsor, Unversity, BaseModel
from rest_framework import serializers
from django.db.models import Sum



class SponsorSerializer(ModelSerializer):

    class Meta:
        model = Sponsor
        exclude = ('organization','updated_at','sponsor_type' )

class StudentSerializer(ModelSerializer):
    unversity = serializers.StringRelatedField(source='unversity.title')
    allocated_money = serializers.SerializerMethodField()

    def get_allocated_money (self,obj):

        student_paid_money = obj.student_sponsors.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0 

        return student_paid_money
    

    class Meta:
        model = Student
        exclude = ('phone','created_at','updated_at' )
        


class StudentDetailSerializer(ModelSerializer):
    unversity = serializers.StringRelatedField(source='unversity.title')
    

    allocated_money = serializers.SerializerMethodField()

    def get_allocated_money (self,obj):

        student_paid_money = obj.student_sponsors.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0 

        return student_paid_money
    
    class Meta:
        model = Student
        exclude = ('created_at','updated_at' )


class StudentSponsorSerializer(ModelSerializer):
    
    class Meta:
        model = StudentSponsor
        fields = ('id', 'student','sponsor','amount')
    def validate(self, attrs):
        amount = attrs.get('amount')
        sponsor = attrs.get('sponsor')
        student = attrs.get('student')
        
        student_paid_money = student.student_sponsors.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0 

        if student.contract_amount -student_paid_money < amount:
            raise serializers.ValidationError(
                detail={'error': f"Siz {student.contract_amount - student_paid_money} som to'lasangiz yetarli"}
            )
        

        sponsor_paid_money = sponsor.student_sponsors.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0 
        if sponsor.amount - sponsor_paid_money < amount:
            raise serializers.ValidationError(
                detail={'error': f"Sizning hisobingizda {sponsor.amount - sponsor_paid_money} som mavjud"}
            )
        
        return attrs 
        return super().validate(attrs)
    
class StudentSponsorListSerializer(ModelSerializer):
    sponsor = serializers.StringRelatedField(source="sponsor.full_name")

    class Meta:
        model = StudentSponsor
        fields = ("id","sponsor","amount")

    

















