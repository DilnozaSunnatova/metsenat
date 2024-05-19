from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Sponsor, Student,StudentSponsor
from .serializer import SponsorSerializer, StudentSerializer,StudentDetailSerializer,StudentSponsorSerializer,StudentSponsorListSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView,ListAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db.models import Sum


class SponsorCreatreAPIView(CreateAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()

class SponsorUpdateAPIView(UpdateAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()

class SponsorListAPIView(ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('conditions',)
    search_fields = ('full_name','payment_type')




class StudentSponsorCreatreAPIView(CreateAPIView):
    serializer_class = StudentSponsorSerializer
    queryset = StudentSponsor.objects.all()

class StudentUpdateAPIView(UpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('student_type','unversity',)
    search_fields = ('full_name',)

class SponsorListAPIView(ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()
    filter_backends = []
    filterset_fields = ()
    search_fields = ()
    


class StudentDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()


class StudentSponsorListAPIView(ListAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorListSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ('student',)

class StatisticAPIView(APIView):
    def get(self,request):
        from django.db.models import Sum
        total_paid_amount  = StudentSponsor.objects.aggregate(total=Sum('amount'))['total'] or 0
        total_required_amount = Student.objects.aggregate(total=Sum('contract_amount'))['total'] or 0
        total_unpaid_amount = total_required_amount-total_paid_amount
        return Response(
            data={
            "total_paid_amount": total_paid_amount,
            "total_required_amount":total_required_amount,
            "total_unpaid_amount": total_unpaid_amount
        })
    


class GraphicAPIView(APIView):

    def get(self,request):

        from datetime import datetime
        this_year = datetime.now().year
        result = []
        for i in range(1,13):
            sponsor_amount = Sponsor.objects.filter(
                created_at__month=i,
                created_at__year=this_year,
                status='apporved'
                ).aggregate(total=Sum('amount'))['total'] or 0
            
            student_amount = Student.objects.filter(
                created_at__month=i,
                created_at__year=this_year,

            ).aaggregate(total=Sum('contract_amount'))['total'] or 0
            
            result.append({
                "month": i,
                "sponsor_amount": sponsor_amount,
                "student_amount": student_amount
            })


        return Response(result)

        










# class SonsorAPIView(APIView):

#     def get(self, request, *args, **kwargs):
#         sponsor = Sponsor.objects.all()
#         serializer = SponsorSerializer(sponsor, many=True)
#         return Response(serializer.data)
    

# class StudentAPIView(APIView):

#     def get(self, request, *args, **kwargs):
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data)
