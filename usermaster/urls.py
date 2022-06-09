from usermaster import views
from django.urls import path


app_name = 'usermaster' 

urlpatterns = [
    path('',views.home,name='home'),
    path('machine_master/',views.index,name='index'),  
    path('addnew',views.addnew),  
    path('edit/<int:id>',views.edit),  
    path('update/<int:id>',views.update),  
    path('delete/<int:id>',views.destroy),
    path('image_view/',views.images_view,name='images_view'),
    #Control
    path('controlfile/',views.control_index,name='control_index'),
    path('cdelete/<int:id>',views.control_destroy,name='control_destroy'),
    path('controlupload/',views.control_upload,name='control_upload'),
    path('upload/',views.upload,name='upload'),
    path('save',views.save_machine,name='save_machine'),
    #Process
    path('processfile/',views.process_index,name='process_index'),
    path('pdelete/<int:id>',views.process_destroy,name='process_destroy'),
    path('processupload/',views.process_upload,name='process_upload'),
    path('pupload/',views.p_upload,name='p_upload'),
    path('psave',views.p_save_machine,name='p_save_machine'),

    #Skill Matrix
    path('skillfile/',views.skill_index,name='skill_index'),
    path('skdelete/<int:id>',views.skill_destroy,name='skill_destroy'),
    path('skillupload/',views.skill_upload,name='skill_upload'),
    path('skupload/',views.sk_upload,name='sk_upload'),
    path('sksave',views.skill_save_machine,name='skill_save_machine'),

    #Maintenance 
    path('maintainfile/',views.maintain_index,name='maintain_index'),
    path('mdelete/<int:id>',views.maintain_destroy,name='maintain_destroy'),
    path('maintainupload/',views.maintain_upload,name='maintain_upload'),
    path('mupload/',views.m_upload,name='m_upload'),
    path('msave',views.maintain_save_machine,name='maintain_save_machine'),

    #SWS
    path('swsfile/',views.sws_index,name='sws_index'),
    path('swdelete/<int:id>',views.sws_destroy,name='sws_destroy'),
    path('swsupload/',views.sws_upload,name='sws_upload'),
    path('swupload/',views.sw_upload,name='sw_upload'),
    path('swsave',views.sws_save_machine,name='sws_save_machine'),

    #Safety
    path('safetyfile/',views.safety_index,name='safety_index'),
    path('sfdelete/<int:id>',views.safety_destroy,name='safety_destroy'),
    path('safetyupload/',views.safety_upload,name='safety_upload'),
    path('sfupload/',views.sf_upload,name='sf_upload'),
    path('sfsave',views.safety_save_machine,name='safety_save_machine'),

    #PFD
    path('pfdfile/',views.pfd_index,name='pfd_index'),
    path('pfdelete/<int:id>',views.pfd_destroy,name='pfd_destroy'),
    path('pfdupload/',views.pfd_upload,name='pfd_upload'),
    path('pfupload/',views.pf_upload,name='pf_upload'),
    path('pfsave',views.pfd_save_machine,name='pfd_save_machine'),

    #Gauges
    path('gaugesfile/',views.gauges_index,name='gauges_index'),
    path('gdelete/<int:id>',views.gauges_destroy,name='gauges_destroy'),
    path('gaugesupload/',views.gauges_upload,name='gauges_upload'),
    path('gaugeupload/',views.gauge_upload,name='gauge_upload'),
    path('gsave',views.gauges_save_machine,name='gauges_save_machine'),

    #video
    path('videos/',views.showvideo,name='showvideo'),
    path('video/',views.viewvideo,name='viewvideo'),
    path('vdelete/<int:id>',views.videos_destroy,name='videos_destroy'),

]