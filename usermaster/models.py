from os import link
from django.db import models

# Create your models here.
class Machine(models.Model):
    def __str__(self):
        return self.machine_name
    machine_name = models.CharField(max_length=100)
    operation_no = models.IntegerField()

    link1 = 'Edit'
    link2 = 'Delete'
  
    class Meta:  
        db_table = "machine"

#Control Model
class Controlmachine(models.Model):  
    machine_name = models.CharField(max_length=100)  
    operation_no = models.IntegerField()  
    control_uploadfile = models.FileField(upload_to='control_files/')

    link1 = 'Edit'
    link2 = 'Delete'
  
    class Meta:  
        db_table = "controlmachine"

    def cdelete(self, *args, **kwargs):
        self.machine_name.delete()
        self.operation_no.delete()
        self.control_uploadfile.delete()
        super.delete(*args, *kwargs)

#Process Model
class Processmachine(models.Model):  
    machine_name = models.CharField(max_length=100)  
    operation_no = models.IntegerField()  
    process_uploadfile = models.FileField(upload_to='process_files/')

    link1 = 'Edit'
    link2 = 'Delete'
    class Meta:  
        db_table = "processmachine"
    
    def pdelete(self, *args, **kwargs):
        self.machine_name.delete()
        self.operation_no.delete()
        self.process_uploadfile.delete()
        super.delete(*args, *kwargs)

#Skill Matrix
class Skillmachine(models.Model):  
    machine_name = models.CharField(max_length=100)  
    operation_no = models.IntegerField()  
    skill_uploadfile = models.FileField(upload_to='skill_files/')

    link1 = 'Edit'
    link2 = 'Delete'
  
    class Meta:  
        db_table = "skillmachine"

    def skdelete(self, *args, **kwargs):
        self.machine_name.delete()
        self.operation_no.delete()
        self.skill_uploadfile.delete()
        super.delete(*args, *kwargs)

#Maintenance
class Maintainmachine(models.Model):  
    machine_name = models.CharField(max_length=100)  
    operation_no = models.IntegerField()  
    maintain_uploadfile = models.FileField(upload_to='maintain_files/')

    link1 = 'Edit'
    link2 = 'Delete'
  
    class Meta:  
        db_table = "maintainmachine"

    def mdelete(self, *args, **kwargs):
        self.machine_name.delete()
        self.operation_no.delete()
        self.maintain_uploadfile.delete()
        super.delete(*args, *kwargs)

#SWS
class Swsmachine(models.Model):  
    machine_name = models.CharField(max_length=100)  
    operation_no = models.IntegerField()  
    sws_uploadfile = models.FileField(upload_to='sws_files/')

    link1 = 'Edit'
    link2 = 'Delete'
  
    class Meta:  
        db_table = "swsmachine"

    def swdelete(self, *args, **kwargs):
        self.machine_name.delete()
        self.operation_no.delete()
        self.sws_uploadfile.delete()
        super.delete(*args, *kwargs)

#Safety
class Safetymachine(models.Model):  
    machine_name = models.CharField(max_length=100)  
    operation_no = models.IntegerField()  
    safety_uploadfile = models.FileField(upload_to='safety_files/')

    link1 = 'Edit'
    link2 = 'Delete'
  
    class Meta:  
        db_table = "safetymachine"
    
    def sfdelete(self, *args, **kwargs):
        self.machine_name.delete()
        self.operation_no.delete()
        self.safety_uploadfile.delete()
        super.delete(*args, *kwargs)

#PFD
class Pfdmachine(models.Model):  
    machine_name = models.CharField(max_length=100)  
    operation_no = models.IntegerField()  
    pfd_uploadfile = models.FileField(upload_to='pfd_files/')

    link1 = 'Edit'
    link2 = 'Delete'
  
    class Meta:  
        db_table = "pfdmachine"

    def pfdelete(self, *args, **kwargs):
        self.machine_name.delete()
        self.operation_no.delete()
        self.pfd_uploadfile.delete()
        super.delete(*args, *kwargs)

#Gauges
class Gaugesmachine(models.Model):  
    machine_name = models.CharField(max_length=100)  
    operation_no = models.IntegerField()  
    gauges_uploadfile = models.FileField(upload_to='gauges_files/')

    link1 = 'Edit'
    link2 = 'Delete'
  
    class Meta:  
        db_table = "gaugesmachine"

    def gdelete(self, *args, **kwargs):
        self.machine_name.delete()
        self.operation_no.delete()
        self.gauges_uploadfile.delete()
        super.delete(*args, *kwargs)

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    link1 = 'Edit'
    link2 = 'Delete'

    def __str__(self):
        return self.name + ": " + str(self.videofile)

    def vdelete(self, *args, **kwargs):
        self.name.delete()
        self.videofile.delete()
        super.delete(*args, *kwargs)


