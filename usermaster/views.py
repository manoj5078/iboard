from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect, render
from usermaster.forms import MachineForm, ControlForm, ProcessForm, SkillForm, MaintainForm, SwsForm, SafetyForm, PfdForm, GaugesForm, VideoForm
from usermaster.models import Machine, Controlmachine, Processmachine, Skillmachine, Maintainmachine, Swsmachine, Safetymachine, Pfdmachine, Gaugesmachine, Video
# Create your views here.

def home(request):
    return render(request,'usermaster/home.html')

def addnew(request):  
    if request.method == "POST":  
        form = MachineForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponseRedirect('/usermaster/machine_master/')  
            except:  
                pass 
    else:  
        form = MachineForm()  
    return render(request,'usermaster/index.html',{'form':form})  

def index(request):  
    machines = Machine.objects.all()  
    return render(request,"usermaster/show.html",{'machines':machines}) 

def edit(request, id):  
    machine = Machine.objects.get(id=id)  
    return render(request,'usermaster/edit.html',{'machine':machine})

def update(request, id):  
    machine = Machine.objects.get(id=id)  
    form = MachineForm(request.POST,instance=machine)  
    if form.is_valid():  
        form.save()  
        return HttpResponseRedirect('/usermaster/machine_master/')  
    return render(request,'usermaster/edit.html',{'machine': machine})

def destroy(request, id):  
    machine = Machine.objects.get(id=id)  
    machine.delete()  
    return HttpResponseRedirect("/usermaster/machine_master/") 

def images_view(request):
    return render(request,'usermaster/image.html')

#Control Process
def control_upload(request):  
    if request.method == 'POST':
        form = ControlForm(request.POST, request.FILES)  
        if form.is_valid():
            model_instance = form.save()
            model_instance.save()
            messages.success(request, 'File Uploaded')
    else:
        form = ControlForm()
    controlmachines = Controlmachine.objects.all()
    return render(request,'usermaster/control_uploadfile.html',{'form':form,'controlmachines':controlmachines})

def control_index(request):  
    controlmachines = Controlmachine.objects.all()  
    return render(request,"usermaster/control_show.html",{'controlmachines':controlmachines}) 

def control_destroy(request, id):
    controlmachines = Controlmachine.objects.get(id=id)  
    controlmachines.delete()  
    return HttpResponseRedirect('/usermaster/controlfile/')

def upload(request):
    controlmachines = Controlmachine.objects.all()
    return render(request,'usermaster/upload.html',{'controlmachines':controlmachines})

def save_machine(request):
   if request.method == "POST":
      machine_name = request.POST.get('machinename', '')
      operation_no = request.POST.get('operationname','')
      choiced_cmachine = Controlmachine.objects.filter(machine_name=machine_name, operation_no=operation_no)
      controlmachines = Controlmachine.objects.all()
      return render(request,'usermaster/upload.html',{'controlmachines':controlmachines,'choiced_cmachine':choiced_cmachine})

#Process Sheet
def process_upload(request):  
    if request.method == 'POST':
        form = ProcessForm(request.POST, request.FILES)  
        if form.is_valid():
            model_instance = form.save()
            model_instance.save()
            messages.success(request, 'File Uploaded')
    else:
        form = ProcessForm()
    processmachiness = Processmachine.objects.all()
    return render(request,'usermaster/process_uploadfile.html',{'form':form,'processmachiness':processmachiness})

def process_index(request):  
    processmachines = Processmachine.objects.all()  
    return render(request,"usermaster/process_show.html",{'processmachines':processmachines}) 

def process_destroy(request, id):  
    processmachines = Processmachine.objects.get(id=id)  
    processmachines.delete()  
    return HttpResponseRedirect('/usermaster/processfile/')

def p_upload(request):
    pmachines = Processmachine.objects.all()
    return render(request,'usermaster/p_upload.html',{'pmachines':pmachines})

def p_save_machine(request):
   if request.method == "POST":
      machine_name = request.POST.get('machinename', '')
      operation_no = request.POST.get('operationname','')
      choiced_pmachine = Processmachine.objects.filter(machine_name=machine_name, operation_no=operation_no)
      pmachines = Processmachine.objects.all()
      return render(request,'usermaster/p_upload.html',{'pmachines':pmachines,'choiced_pmachine':choiced_pmachine})

#Skill Matrix
def skill_upload(request):  
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)  
        if form.is_valid():
            model_instance = form.save()
            model_instance.save()
            messages.success(request, 'File Uploaded')
    else:
        form = SkillForm()
    skillmachiness = Skillmachine.objects.all()
    return render(request,'usermaster/skill_uploadfile.html',{'form':form,'skillmachiness':skillmachiness})

def skill_index(request):  
    skillmachines = Skillmachine.objects.all()  
    return render(request,"usermaster/skill_show.html",{'skillmachines':skillmachines}) 

def skill_destroy(request, id):  
    skillmachines = Skillmachine.objects.get(id=id)  
    skillmachines.delete()  
    return HttpResponseRedirect('/usermaster/skillfile/')

def sk_upload(request):
    skillmachines = Skillmachine.objects.all()
    return render(request,'usermaster/skill_upload.html',{'skillmachines':skillmachines})

def skill_save_machine(request):
   if request.method == "POST":
      machine_name = request.POST.get('machinename', '')
      operation_no = request.POST.get('operationname','')
      choiced_skillmachine = Skillmachine.objects.filter(machine_name=machine_name, operation_no=operation_no)
      skillmachines = Skillmachine.objects.all()
      return render(request,'usermaster/skill_upload.html',{'skillmachines':skillmachines,'choiced_skillmachine':choiced_skillmachine})

#Maintenance
def maintain_upload(request):  
    if request.method == 'POST':
        form = MaintainForm(request.POST, request.FILES)  
        if form.is_valid():
            model_instance = form.save()
            model_instance.save()
            messages.success(request, 'File Uploaded')
    else:
        form = MaintainForm()
    maintainmachiness = Maintainmachine.objects.all()
    return render(request,'usermaster/maintain_uploadfile.html',{'form':form,'maintainmachiness':maintainmachiness})

def maintain_index(request):  
    maintainmachines = Maintainmachine.objects.all()  
    return render(request,"usermaster/maintain_show.html",{'maintainmachines':maintainmachines}) 

def maintain_destroy(request, id):  
    maintainmachines = Maintainmachine.objects.get(id=id)  
    maintainmachines.delete()  
    return HttpResponseRedirect('/usermaster/maintainfile/')

def m_upload(request):
    maintainmachines = Maintainmachine.objects.all()
    return render(request,'usermaster/m_upload.html',{'maintainmachines':maintainmachines})

def maintain_save_machine(request):
   if request.method == "POST":
      machine_name = request.POST.get('machinename', '')
      operation_no = request.POST.get('operationname','')
      choiced_maintainmachine = Maintainmachine.objects.filter(machine_name=machine_name, operation_no=operation_no)
      maintainmachines = Maintainmachine.objects.all()
      return render(request,'usermaster/m_upload.html',{'maintainmachines':maintainmachines,'choiced_maintainmachine':choiced_maintainmachine})

#SWS
def sws_upload(request):  
    if request.method == 'POST':
        form = SwsForm(request.POST, request.FILES)  
        if form.is_valid():
            model_instance = form.save()
            model_instance.save()
            messages.success(request, 'File Uploaded')
    else:
        form = SwsForm()
    swsmachiness = Swsmachine.objects.all()
    return render(request,'usermaster/sws_uploadfile.html',{'form':form,'swsmachiness':swsmachiness})

def sws_index(request):  
    swsmachines = Swsmachine.objects.all()  
    return render(request,"usermaster/sws_show.html",{'swsmachines':swsmachines}) 

def sws_destroy(request, id):  
    swsmachines = Swsmachine.objects.get(id=id)  
    swsmachines.delete()  
    return HttpResponseRedirect('/usermaster/swsfile/')

def sw_upload(request):
    swsmachines = Swsmachine.objects.all()
    return render(request,'usermaster/sw_upload.html',{'swsmachines':swsmachines})

def sws_save_machine(request):
   if request.method == "POST":
      machine_name = request.POST.get('machinename', '')
      operation_no = request.POST.get('operationname','')
      choiced_swsmachine = Swsmachine.objects.filter(machine_name=machine_name, operation_no=operation_no)
      swsmachines = Swsmachine.objects.all()
      return render(request,'usermaster/sw_upload.html',{'swsmachines':swsmachines,'choiced_swsmachine':choiced_swsmachine})


#Safety
def safety_upload(request):  
    if request.method == 'POST':
        form = SafetyForm(request.POST, request.FILES)  
        if form.is_valid():
            model_instance = form.save()
            model_instance.save()
            messages.success(request, 'File Uploaded')
    else:
        form = SafetyForm()
    safetymachiness = Safetymachine.objects.all()
    return render(request,'usermaster/safety_uploadfile.html',{'form':form,'safetymachiness':safetymachiness})

def safety_index(request):  
    safetymachines = Safetymachine.objects.all()  
    return render(request,"usermaster/safety_show.html",{'safetymachines':safetymachines}) 

def safety_destroy(request, id):  
    safetymachines = Safetymachine.objects.get(id=id)  
    safetymachines.delete()  
    return HttpResponseRedirect('/usermaster/safetyfile/')

def sf_upload(request):
    safetymachines = Safetymachine.objects.all()
    return render(request,'usermaster/sf_upload.html',{'safetymachines':safetymachines})

def safety_save_machine(request):
   if request.method == "POST":
      machine_name = request.POST.get('machinename', '')
      operation_no = request.POST.get('operationname','')
      choiced_safetymachine = Safetymachine.objects.filter(machine_name=machine_name, operation_no=operation_no)
      safetymachines = Safetymachine.objects.all()
      return render(request,'usermaster/sf_upload.html',{'safetymachines':safetymachines,'choiced_safetymachine':choiced_safetymachine})

#PFD
def pfd_upload(request):  
    if request.method == 'POST':
        form = PfdForm(request.POST, request.FILES)  
        if form.is_valid():
            model_instance = form.save()
            model_instance.save()
            messages.success(request, 'File Uploaded')
    else:
        form = PfdForm()
    pfdmachiness = Pfdmachine.objects.all()
    return render(request,'usermaster/pfd_uploadfile.html',{'form':form,'pfdmachiness':pfdmachiness})

def pfd_index(request):  
    pfdmachines = Pfdmachine.objects.all()  
    return render(request,"usermaster/pfd_show.html",{'pfdmachines':pfdmachines}) 

def pfd_destroy(request, id):  
    pfdmachines = Pfdmachine.objects.get(id=id)  
    pfdmachines.delete()  
    return HttpResponseRedirect('/usermaster/pfdfile/')

def pf_upload(request):
    pfdmachines = Pfdmachine.objects.all()
    return render(request,'usermaster/pf_upload.html',{'pfdmachines':pfdmachines})

def pfd_save_machine(request):
   if request.method == "POST":
      machine_name = request.POST.get('machinename', '')
      operation_no = request.POST.get('operationname','')
      choiced_pfdmachine = Pfdmachine.objects.filter(machine_name=machine_name, operation_no=operation_no)
      pfdmachines = Pfdmachine.objects.all()
      return render(request,'usermaster/pf_upload.html',{'pfdmachines':pfdmachines,'choiced_pfdmachine':choiced_pfdmachine})


#Gauges
def gauges_upload(request):  
    if request.method == 'POST':
        form = GaugesForm(request.POST, request.FILES)  
        if form.is_valid():
            model_instance = form.save()
            model_instance.save()
            messages.success(request, 'File Uploaded')
    else:
        form = GaugesForm()
    gaugesmachiness = Gaugesmachine.objects.all()
    return render(request,'usermaster/gauges_uploadfile.html',{'form':form,'gaugesmachiness':gaugesmachiness})

def gauges_index(request):  
    gaugesmachines = Gaugesmachine.objects.all()  
    return render(request,"usermaster/gauges_show.html",{'gaugesmachines':gaugesmachines}) 

def gauges_destroy(request, id):  
    gaugesmachines = Gaugesmachine.objects.get(id=id)  
    gaugesmachines.delete()  
    return HttpResponseRedirect('/usermaster/gaugesfile/')

def gauge_upload(request):
    gaugesmachines = Gaugesmachine.objects.all()
    return render(request,'usermaster/gauge_upload.html',{'gaugesmachines':gaugesmachines})

def gauges_save_machine(request):
   if request.method == "POST":
      machine_name = request.POST.get('machinename', '')
      operation_no = request.POST.get('operationname','')
      choiced_gaugesmachine = Gaugesmachine.objects.filter(machine_name=machine_name, operation_no=operation_no)
      gaugesmachines = Gaugesmachine.objects.all()
      return render(request,'usermaster/gauge_upload.html',{'gaugesmachines':gaugesmachines,'choiced_gaugesmachine':choiced_gaugesmachine})


def showvideo(request):
    lastvideo= Video.objects.all()
    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Video Uploaded')
    context= {'lastvideo': lastvideo,
              'form': form
              }
    return render(request, 'usermaster/video.html', context)

def viewvideo(request):
    lastvideo= Video.objects.all()
    context= {'lastvideo':lastvideo}
    return render(request,'usermaster/view_video.html',context)

def videos_destroy(request, id):  
    lastvideo = Video.objects.get(id=id)  
    lastvideo.delete()  
    return HttpResponseRedirect('/usermaster/videos/')