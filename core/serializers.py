from rest_framework import serializers

from core.models import Home, Services, UpcomingEvent, Structure, POs, AC, PMY, \
                        NLM, UBA, Awards, Reports, ActivityCalendar, \
                            Assets, VT, Sapling, BDC, Camp, Seminar, Others, \
                                HomeUpdate


class HomeSerializer(serializers.ModelSerializer):
    """Serializer for Home"""
    class Meta:
        model = Home
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    """Serializer for Services"""
    class Meta:
        model = Services
        fields = '__all__'

class UpcomingEventSerializer(serializers.ModelSerializer):
    """Serializer for Upcoming Event"""
    class Meta:
        model = UpcomingEvent
        fields = '__all__'

class StructureSerializer(serializers.ModelSerializer):
    """Serializer for Structure Image"""
    class Meta:
        model = Structure
        fields = '__all__'

class POSerializer(serializers.ModelSerializer):
    """Serializer for POs"""
    class Meta:
        model = POs
        fields = '__all__'

class ACSerializer(serializers.ModelSerializer):
    """Serializer for AC"""
    class Meta:
        model = AC
        fields = '__all__'

class PMYSerializer(serializers.ModelSerializer):
    """Serializer for PMY"""
    class Meta:
        model = PMY
        fields = '__all__'

# class DLSerializer(serializers.ModelSerializer):
#     """Serializer for DL"""
#     class Meta:
#         model = DL
#         fields = '__all__'

class NLMSerializer(serializers.ModelSerializer):
    """Serializer for NLM"""
    class Meta:
        model = NLM
        fields = '__all__'

# class SBMSerializer(serializers.ModelSerializer):
#     """Serializer for SBM"""
#     class Meta:
#         model = SBM
#         fields = '__all__'

class UBASerializer(serializers.ModelSerializer):
    """Serializer for UBA"""
    class Meta:
        model = UBA
        fields = '__all__'

class AwardsSerializer(serializers.ModelSerializer):
    """Serializer for Awards"""
    class Meta:
        model = Awards
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    """Serializer for Reports"""
    class Meta:
        model = Reports
        fields = '__all__'

class ActivityCalendarSerializer(serializers.ModelSerializer):
    """Serializer for Activity Calendar"""
    class Meta:
        model = ActivityCalendar
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    """Serializer for Assets"""
    class Meta:
        model = Assets
        fields = '__all__'

class VTSerializer(serializers.ModelSerializer):
    """Serializer for VT"""
    class Meta:
        model = VT
        fields = '__all__'

class SaplingSerializer(serializers.ModelSerializer):
    """Serializer for Sapling"""
    class Meta:
        model = Sapling
        fields = '__all__'

class BDCSerializer(serializers.ModelSerializer):
    """Serializer for BDC"""
    class Meta:
        model = BDC
        fields = '__all__'

class CampSerializer(serializers.ModelSerializer):
    """Serializer for Camp"""
    class Meta:
        model = Camp
        fields = '__all__'

class SeminarSerializer(serializers.ModelSerializer):
    """Serializer for Seminar"""
    class Meta:
        model = Seminar
        fields = '__all__'

class OtherSerializer(serializers.ModelSerializer):
    """Serializer for Seminar"""
    class Meta:
        model = Others
        fields = '__all__'

class HUSerializer(serializers.ModelSerializer):
    """Serializer for Homepage awards and year updates"""
    class meta:
        model = HomeUpdate
        fields = '__all__'
