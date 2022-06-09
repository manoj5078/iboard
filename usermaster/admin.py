from django.contrib import admin

from usermaster.models import Gaugesmachine, Machine,Controlmachine, Maintainmachine, Pfdmachine, Processmachine, Safetymachine, Skillmachine, Swsmachine, Video

# Register your models here.
admin.site.site_header = 'i-board S3-Line Master'
admin.site.site_title = 'iboard'
admin.site.index_title = 'Manage Machines'

class MachineAdmin(admin.ModelAdmin):
    list_display = ('machine_name','operation_no','link1','link2')
    search_fields = ('machine_name','operation_no',)
    list_display_links = ('link1','link2',)

class ControlAdmin(admin.ModelAdmin):
    list_display = ('machine_name','operation_no','control_uploadfile','link1','link2')
    search_fields = ('machine_name','operation_no',)
    list_display_links = ('link1','link2',)

class ProcessAdmin(admin.ModelAdmin):
    list_display = ('machine_name','operation_no','process_uploadfile','link1','link2')
    search_fields = ('machine_name','operation_no',)
    list_display_links = ('link1','link2',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('machine_name','operation_no','skill_uploadfile','link1','link2')
    search_fields = ('machine_name','operation_no',)
    list_display_links = ('link1','link2',)

class MaintainAdmin(admin.ModelAdmin):
    list_display = ('machine_name','operation_no','maintain_uploadfile','link1','link2')
    search_fields = ('machine_name','operation_no',)
    list_display_links = ('link1','link2',)

class SwsAdmin(admin.ModelAdmin):
    list_display = ('machine_name','operation_no','sws_uploadfile','link1','link2')
    search_fields = ('machine_name','operation_no',)
    list_display_links = ('link1','link2',)

class SafetyAdmin(admin.ModelAdmin):
    list_display = ('machine_name','operation_no','safety_uploadfile','link1','link2')
    search_fields = ('machine_name','operation_no',)
    list_display_links = ('link1','link2',)

class PfdAdmin(admin.ModelAdmin):
    list_display = ('machine_name','operation_no','pfd_uploadfile','link1','link2')
    search_fields = ('machine_name','operation_no',)
    list_display_links = ('link1','link2',)

class GaugesAdmin(admin.ModelAdmin):
    list_display = ('machine_name','operation_no','gauges_uploadfile','link1','link2')
    search_fields = ('machine_name','operation_no',)
    list_display_links = ('link1','link2',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('name','videofile','link1','link2')
    search_fields = ('name',)
    list_display_links = ('link1','link2',)

admin.site.register(Machine, MachineAdmin)
admin.site.register(Controlmachine, ControlAdmin)
admin.site.register(Processmachine, ProcessAdmin)
admin.site.register(Skillmachine, SkillAdmin)
admin.site.register(Maintainmachine,MaintainAdmin)
admin.site.register(Swsmachine,SwsAdmin)
admin.site.register(Safetymachine,SafetyAdmin)
admin.site.register(Pfdmachine,PfdAdmin)
admin.site.register(Gaugesmachine,GaugesAdmin)
admin.site.register(Video,VideoAdmin)
