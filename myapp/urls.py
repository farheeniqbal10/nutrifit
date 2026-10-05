"""
URL configuration for AI_DIET_CONSULTANT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.loginn),
    path('addbatch/',views.addbatch),
    path('updatebatch/<id>',views.updatebatch),
    path('updatebatch_post/<id>',views.updatebatch_post),
    path('deletebatch/<id>',views.deletebatch),
    path('updatetrainer/<id>',views.updatetrainer),
    path('edittrainer/<id>',views.updatetraineradmin),
    path('updatetrainer_post/<id>',views.updatetrainer_post),
    path('edittrainer_post/<id>',views.updatetraineradmin_post),
    path('deletetrainer/<id>',views.deletetrainer),
    path('addtrainer', views.addtrainer),
    path('assigntrainer/<id>', views.assigntrainer),
    path('viewtrainer',views.viewtrainer),
    path('adminhome', views.adminhome),
    path('viewbatch', views.viewbatch),
    path('viewfeedback', views.viewfeedback),
    path('viewrequest/<id>', views.viewrequest),
    path('rejectrequest/<id>',views.rejectrequest),
    path('deleterequest/<id>',views.deleterequest),
    path('addbatch_post', views.addbatch_post),
    path('login_post', views.login_post),
    path('addtrainer_post', views.addtrainer_post),
    path('assignbatch_post/<id>', views.assignbatch_post),
    path('addtips/<uid>',views.addtips),
    path('addworkout/<uid>',views.addworkout),
    path('uploaddietplan/<id>/<uid>',views.uploaddietplan),
    path('uploaddietplan_post/<id>/<uid>',views.uploaddietplan_post),
    path('viewdietplan/<uid>',views.viewdietplan),
    path('editdietplan/<id>',views.editdietplan),
    path('editdietplan_post/<id>',views.editdietplan_post),
    path('deletedietplan/<id>',views.deletedietplan),
    path('viewassignedbatch/',views.viewassignedbatch),
    path('viewhealthinfo/<id>',views.viewhealthinfo),
    path('viewmembers/<id>',views.viewmembers),
    path('viewprofile/',views.viewprofile),
    path('viewtips/<uid>',views.viewtips),
    path('viewworkout/<uid>',views.viewworkout),
    path('trainerhome/',views.trainerhome),
    path('addtips_post/<uid>',views.addtips_post),
    path('addworkout_post/<uid>',views.addworkout_post),
    path('viewbatchinfo',views.viewbatchinfo),
    path('viewbatchtrainer/<id>',views.viewbatchtrainer),
    path('viewbatchmember/<id>',views.viewbatchmember),
    path('edittip/<id>',views.edittip),
    path('edittip_post/<id>',views.edittip_post),
    path('deletetip/<id>',views.deletetip),
    path('editworkout/<id>',views.editworkout),
    path('editworkout_post/<id>',views.editworkout_post),
    path('deleteworkout/<id>',views.deleteworkout),
    path('register',views.register),
    path('register_post',views.register_post),
    path('viewuserprofile',views.viewuserprofile),
    path('updateuser/<id>',views.updateuser),
    path('updateuser_post/<id>',views.updateuser_post),
    path('userhome/',views.userhome),
    path('uploadhealth/',views.uploadhealth),
    path('sendfeedback/',views.sendfeedback),
    path('viewbatchuser/',views.viewbatchuser),
    path('user_exit_batch/<id>',views.user_exit_batch),
    path('viewtipsuser/',views.viewtipsuser),
    path('viewdietplanuser/',views.viewdietplanuser),
    path('viewworkoutuser/',views.viewworkoutuser),
    path('uploadhealthpost/',views.uploadhealth_post),
    path('sendfeedback_post/',views.sendfeedback_post),
    path('sendrequest/<id>/<jid>',views.sendrequest),
    path('viewhealth/',views.viewhealth),
    path('updatehealth/<id>',views.updatehealth),
    path('updatehealth_post/<id>',views.updatehealth_post),
    path('mybatch/',views.mybatch),
    path('chattrainer/<id>',views.chattrainer),
    path('chatuser/<id>',views.chatuser),
    path('chatsent',views.chatsnd),
    path('Uchatsent',views.Uchatsent),
    path('chatreply',views.chatrply),
    path('Uchatreply',views.Uchatrply),
    path('myprogress',views.myprogress),
    path('myprogresstrainer/<id>',views.myprogresstrainer),
    path('forgot_pass',views.forgot_pass),
    path('forgot_pass_post',views.forgot_pass_post),
    path('deleteuser/<id>',views.deleteuser),
    path('deleteuserprofile/<id>',views.deleteuserprofile),










]
