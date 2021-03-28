from rest_framework import serializers
from django.contrib.gis.geos import Point
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from .models import Peak, Record
from rest_framework_gis.serializers import GeometryField
from django.core.exceptions import ValidationError
import json
from django.contrib.gis.geos import GEOSException
from django.contrib.gis.geos import GEOSGeometry
from rest_framework_gis.serializers import GeometryField

class GeometryPointFieldSerializerFields(GeometryField):

    def to_internal_value(self, value):
        try:
            value = value.split(",")
        except:
            raise ValidationError(
                ("Enter the co-ordinates in (latitude,longitude). Ex-12,13")
            )
        try:
            latitude = float(value[0])
        except ValueError:
            raise ValidationError(
                ("Enter the co-ordinates in (latitude,longitude). Ex-12,13")
            )
        try:
            longitude = float(value[1])
        except ValueError:
            raise ValidationError(
                ("Enter the co-ordinates in (latitude,longitude). Ex-12,13")
            )
        value = {
            "type": "Point",
            "coordinates": [longitude, latitude]
        }
        value = json.dumps(value)
        try:
            return GEOSGeometry(value)
        except (ValueError, GEOSException, TypeError):
            raise ValidationError(
                ('Invalid format: string or unicode input unrecognized as GeoJSON, WKT EWKT or HEXEWKB.'))

    def to_representation(self, value):
        """ """
        value = super(
            GeometryPointFieldSerializerFields, self).to_representation(value)
        # change to compatible with google map
        data = {
            "type": "Point",
            "coordinates": [
                value['coordinates'][1], value['coordinates'][0]
            ]
        }
        return data
class PeakSerializer(serializers.ModelSerializer):
	coordinates = GeometryPointFieldSerializerFields()
	class Meta:
		model = Peak
		fields = ('id','peak_name', 'coordinates','altitude')

class RecordSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Record
		fields = ('id','forecasted_at', 'peak', 'temperature')