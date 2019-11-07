from django.contrib import admin
from echo.models import Devices, DeviceRecords, Records


class DeviceDisplay(admin.ModelAdmin):
    list_display = ('id', 'type', 'unit')


class DeviceRecordDisplay(admin.ModelAdmin):
    list_display = ('device', 'record', 'value', 'created')


class RecordDisplay(admin.ModelAdmin):
    list_display = ('id', 'record_time')


admin.site.register(Devices, DeviceDisplay)
admin.site.register(Records, RecordDisplay)
admin.site.register(DeviceRecords, DeviceRecordDisplay)
