from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from core.models import Home, Services, UpcomingEvent, Structure, POs, AC, PMY, \
                        NLM, UBA, Awards, Reports, ActivityCalendar, \
                            Assets, VT, Sapling, BDC, Camp, Seminar, Others, HomeUpdate
from core.serializers import HomeSerializer, ServiceSerializer, UpcomingEventSerializer, \
                                StructureSerializer, POSerializer, ACSerializer, PMYSerializer, \
                                 NLMSerializer, UBASerializer,\
                                AwardsSerializer, ReportSerializer, ActivityCalendarSerializer, \
                                AssetSerializer, VTSerializer, SaplingSerializer, BDCSerializer, \
                                CampSerializer, SeminarSerializer, OtherSerializer, HUSerializer

class HomeListView(generics.ListAPIView):
    """API view for Home"""
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class ServiceListView(generics.ListAPIView):
    """API view for """
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class UpcomingEventListView(generics.ListAPIView):
    """API view for upcoming events"""
    queryset = UpcomingEvent.objects.all()
    serializer_class = UpcomingEventSerializer

class StructureListView(generics.ListAPIView):
    """API view for upcoming events"""
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer

class POListView(generics.ListAPIView):
    """API view for PO"""
    queryset = POs.objects.all()
    serializer_class = POSerializer

class ACListView(generics.ListAPIView):
    """API view for AC"""
    queryset = AC.objects.all()
    serializer_class = ACSerializer

class PMYListView(generics.ListAPIView):
    """API view for PMY"""
    queryset = PMY.objects.all()
    serializer_class = PMYSerializer

# class DLListView(generics.ListAPIView):
#     """API view for DL"""
#     queryset = DL.objects.all()
#     serializer_class = DLSerializer

class NLMListView(generics.ListAPIView):
    """API view for NLM"""
    queryset = NLM.objects.all()
    serializer_class = NLMSerializer

# class SBMListView(generics.ListAPIView):
#     """API view for """
#     queryset = SBM.objects.all()
#     serializer_class = SBMSerializer

class UBAListView(generics.ListAPIView):
    """API view for UBA"""
    queryset = UBA.objects.all()
    serializer_class = UBASerializer

class AwardsListView(generics.ListAPIView):
    """API view for Awards"""
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer

class ReportListView(generics.ListAPIView):
    """API view for Reports"""
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer

class ActivityCalendarListView(generics.ListAPIView):
    """API view for Activity Calendar"""
    queryset = ActivityCalendar.objects.all()
    serializer_class = ActivityCalendarSerializer

class AssetListView(generics.ListAPIView):
    """API view for Assets"""
    queryset = Assets.objects.all()
    serializer_class = AssetSerializer

class VTListView(generics.ListAPIView):
    """API view for VT"""
    queryset = VT.objects.all()
    serializer_class = VTSerializer

class SaplingListView(generics.ListAPIView):
    """API view for Sapling"""
    queryset = Sapling.objects.all()
    serializer_class = SaplingSerializer

class BDCListView(generics.ListAPIView):
    """API view for BDC"""
    queryset = BDC.objects.all()
    serializer_class = BDCSerializer

class CampListView(generics.ListAPIView):
    """API view for Camp"""
    queryset = Camp.objects.all()
    serializer_class = CampSerializer

class SeminarListView(generics.ListAPIView):
    """API view for Seminar"""
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer

class OtherListView(generics.ListAPIView):
    """API view for Seminar"""
    queryset = Others.objects.all()
    serializer_class = OtherSerializer

def EventYears(request):
    """API view for Other event years list"""
    data = list(Others.objects.values_list('year', flat=True).distinct().order_by('year')) # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)

class HU(generics.ListAPIView):
    """API view for homepage awards count and corona warning removal"""
    queryset = HomeUpdate.objects.all()
    serializer_class = HUSerializer

def handler404(request, exception, template_name="index.html"):
    response = render_to_response('/not-found')
    response.status_code = 404
    return render(request, response)

def handler500(request, *args, **argv):
    return render(request, 'index.html', status=500)
