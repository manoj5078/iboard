from django import forms  
from usermaster.models import Machine, Controlmachine, Processmachine, Skillmachine, Maintainmachine, Swsmachine, Safetymachine, Pfdmachine, Gaugesmachine, Video





class MachineForm(forms.ModelForm):  
    class Meta:  
        model = Machine 
        fields = ['machine_name','operation_no'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'machine_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'operation_no': forms.TextInput(attrs={ 'class': 'form-control' }),
      }

#Control Form
class ControlForm(forms.ModelForm):  
    class Meta:  
        model = Controlmachine 
        fields = ['machine_name', 'operation_no', 'control_uploadfile'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'machine_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'operation_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'control_uploadfile': forms.ClearableFileInput(attrs={ 'class': 'form-control' }),
      }

#Process Form
class ProcessForm(forms.ModelForm):  
    class Meta:  
        model = Processmachine 
        fields = ['machine_name', 'operation_no', 'process_uploadfile'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'machine_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'operation_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'process_uploadfile': forms.ClearableFileInput(attrs={ 'class': 'form-control' }),
      }

#Skill Matrix Form
class SkillForm(forms.ModelForm):  
    class Meta:  
        model = Skillmachine 
        fields = ['machine_name', 'operation_no', 'skill_uploadfile'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'machine_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'operation_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'skill_uploadfile': forms.ClearableFileInput(attrs={ 'class': 'form-control' }),
      }

#Maintenance Form
class MaintainForm(forms.ModelForm):  
    class Meta:  
        model = Maintainmachine 
        fields = ['machine_name', 'operation_no', 'maintain_uploadfile'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'machine_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'operation_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'maintain_uploadfile': forms.ClearableFileInput(attrs={ 'class': 'form-control' }),
      }

#SWS Form
class SwsForm(forms.ModelForm):  
    class Meta:  
        model = Swsmachine 
        fields = ['machine_name', 'operation_no', 'sws_uploadfile'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'machine_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'operation_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'sws_uploadfile': forms.ClearableFileInput(attrs={ 'class': 'form-control' }),
      }

#Safety Form
class SafetyForm(forms.ModelForm):  
    class Meta:  
        model = Safetymachine 
        fields = ['machine_name', 'operation_no', 'safety_uploadfile'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'machine_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'operation_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'safety_uploadfile': forms.ClearableFileInput(attrs={ 'class': 'form-control' }),
      }

#Pfd Form
class PfdForm(forms.ModelForm):  
    class Meta:  
        model = Pfdmachine 
        fields = ['machine_name', 'operation_no', 'pfd_uploadfile'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'machine_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'operation_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'pfd_uploadfile': forms.ClearableFileInput(attrs={ 'class': 'form-control' }),
      }


#Gauges Form
class GaugesForm(forms.ModelForm):  
    class Meta:  
        model = Gaugesmachine 
        fields = ['machine_name', 'operation_no', 'gauges_uploadfile'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'machine_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'operation_no': forms.TextInput(attrs={ 'class': 'form-control' }),
            'gauges_uploadfile': forms.ClearableFileInput(attrs={ 'class': 'form-control' }),
      }

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]

