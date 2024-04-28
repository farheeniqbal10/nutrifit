from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import demjson
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import datetime
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg

import matplotlib.pyplot as plt
# Create your views here.
from myapp.models import *


#admin side
def loginn(requset):
    return render(requset,'admin/login.html')

def addbatch(requset):
    return render(requset, 'admin/Add Batch.html')

def addtrainer(requset):
    return render(requset, 'admin/Add Trainer.html')

def assigntrainer(requset,id):
    res=Trainer.objects.all()
    return render(requset, 'admin/Assign Trainer.html',{'data':res,'id': id})

def viewbatch(requset):
    res = Batch.objects.all()
    if res.exists():
        l=[]
        for i in res:
            a=i.Batch_Capacity
            re = assign.objects.filter(REQUEST__BATCH_id=i.id,
                                       REQUEST__status="approved").count()

            b=int(a)-int(re)
            l.append({
                "re":re,
                "Batch_title":i.Batch_title,
                "Batch_Capacity":i.Batch_Capacity,
                "Time_from":i.Time_from,
                "Time_to":i.Time_to,
                "c":b,
                "id":i.id,

            })


        return render(requset, 'admin/View Batch.html',{'data':l})
    else:
        return render(requset,'admin/nobatches.html')
def viewfeedback(requset):
    res=feedback.objects.all()
    if res.exists():
        return render(requset, 'admin/view feedback.html',{'data':res})
    else:
        return render(requset,'admin/nofeedback.html')

def viewrequest(requset,id):
    res = Request.objects.filter(BATCH=Batch.objects.get(id=id),status="pending")
    if res.exists():
        return render(requset, 'admin/View Request.html',{'data':res})
    else:
        return render(requset,'admin/norequest.html')

def viewtrainer(requset):
    res=Trainer.objects.all()
    if res.exists():
        return render(requset, 'admin/View Trainer.html',{'data':res})
    else:
        return render(requset,'admin/notrainer.html')

def adminhome(requset):
    res=Request.objects.filter(status="pending")
    if res.exists():
        lst=[]
        for i in res:
            bat=i.BATCH.Batch_title
            lst.append("New user request in " + bat)
        return render(requset, 'index.html', {'lst':lst})
    else:
        return render(requset, 'index.html')

def login_post(requset):
     usernam=requset.POST['textfield']
     passwor = requset.POST['textfield2']
     r=Login.objects.filter(username=usernam,password=passwor)
     if r.exists():
         r=r[0]
         if r.usertype=="admin":
             return redirect('/adminhome')
         elif r.usertype=="trainer":
             requset.session['lid']=r.id
             return redirect('/trainerhome')
         elif r.usertype=="user":
             requset.session['lid']=r.id
             return redirect('/userhome')
         else:
             return HttpResponse("<script>alert('Invalid username or password');window.location='/'</script>")
     else:
         return HttpResponse("<script>alert('Invalid username or password');window.location='/'</script>")


def viewbatchinfo(requset):
    res=Batch.objects.all()
    return render(requset,'admin/view batch info.html',{'data':res})


def viewbatchtrainer(requset,id):
    requset.session['bid']=id
    a=Request.objects.filter(BATCH=Batch.objects.get(id=id),status="approved")
    data=[]
    tid=[]
    if a.exists():
        for i in a:
            res=assign.objects.get(REQUEST=i)

            if res.TRAINER.id not in tid:
                r=assign.objects.filter(REQUEST__BATCH_id=id, TRAINER=Trainer.objects.get(id=res.TRAINER.id)).count()

                tid.append(res.TRAINER.id)
                data.append({'d' : res, 'r' : r})
        return render(requset,'admin/view batch trainer.html',{'data':data})
    else:
        return render(requset,'admin/nobatchtrainer.html')

def viewbatchmember(requset,id):
    bid=requset.session['bid']
    tid = Trainer.objects.get(id=id)
    re = assign.objects.filter(TRAINER=tid)
    if re.exists():
        l=[]
        for i in re:

            res = Request.objects.filter(id=i.REQUEST.id,BATCH=bid)
            for ij in res:
                l.append({
                    "name":ij.USER.name,
                    "sex":ij.USER.sex,
                    "age":ij.USER.age,
                    "time":ij.time,
                    "id": ij.USER.id,
                    "bid":bid,
                })
        return render(requset, 'admin/view batch members.html',{'data':l,'bid':bid})
    else:
        return render(requset,'admin/nobatchmember.html')
def assignbatch_post(requset,id):

    tnr=requset.POST['select']
    r=Request.objects.get(id=id)
    res=assign.objects.filter(REQUEST=r)
    if res.exists():
        return HttpResponse("<script>alert('already added');window.location='/viewbatch#abc'</script>")

    else:
        d = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        obj=assign()
        obj.REQUEST=Request.objects.get(id=id)
        obj.TRAINER=Trainer.objects.get(id=tnr)
        obj.time=d
        obj.save()
        Request.objects.filter(id=id).update(status='approved')

        return HttpResponse("<script>alert('added');window.location='/viewbatch#abc'</script>")



def addbatch_post(requset):
    batchtitle=requset.POST['textfield5']
    batchcapacity=requset.POST['textfield']
    from1=requset.POST['textfield2']
    to=requset.POST['textfield3']
    r = Batch.objects.filter(Batch_title=batchtitle,Batch_Capacity=batchcapacity,Time_from=from1,Time_to=to)
    r1= Batch.objects.filter(Batch_title=batchtitle)
    if r1.exists():
        if r.exists():
             return HttpResponse("<script>alert('Already Exist');window.location='addbatch/'</script>")
        return HttpResponse("<script>alert('Batch name exists');window.location='addbatch/'</script>")
    else:
        obj=Batch()
        obj.Batch_Capacity=batchcapacity
        obj.Time_from=from1
        obj.Time_to=to
        obj.Batch_title=batchtitle
        obj.save()
        return HttpResponse('<script>alert("Added");window.location="/viewbatch#abc"</script>')


def addtrainer_post(requset):
    name1=requset.POST['textfield']
    place1=requset.POST['textfield2']
    pin1=requset.POST['textfield3']
    post1=requset.POST['textfield4']
    age1=requset.POST['textfield5']
    gender1=requset.POST['RadioGroup1']
    qualification1=requset.POST['textarea']
    experience1=requset.POST['textarea2']
    mnumber1=requset.POST['textfield6']
    email1=requset.POST['textfield7']
    p=random.randint(0000,9999)
    r = Trainer.objects.filter(name=name1,place=place1,pin=pin1,post=post1,age=age1,sex=gender1,qualification=qualification1,experience=experience1,
                               mobilenumber=mnumber1,email=email1)
    r1=Login.objects.filter(username=email1)
    import smtplib

    #dietconsultant2024@gmail.com
    #rkdjjzbccfsaonne

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("nutrifit20241@gmail.com", "yuxxqtudpztjkzbl")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "nutrifit20241@gmail.com"
    msg['To'] = email1
    msg['Subject'] = "Your Password for Nutrifit"
    body = "Username : " + str(email1)+ "\nPassword : "+str(p)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    if r.exists():
        if r1.exists():
            return HttpResponse("<script>alert('Email Already Exists');window.location='addtrainer#abc'</script>")

        return HttpResponse("<script>alert('Trainer Already Exists');window.location='addtrainer#abc'</script>")

    else:
        obj2=Login()
        obj2.username=email1
        obj2.password=p
        obj2.usertype='trainer'
        obj2.save()
        obj=Trainer()
        obj.name=name1
        obj.place=place1
        obj.pin=pin1
        obj.post = post1
        obj.age=age1
        obj.sex = gender1
        obj.qualification = qualification1
        obj.experience = experience1
        obj.mobilenumber = mnumber1
        obj.email = email1
        obj.LOGIN=obj2
        obj.save()

        return HttpResponse("<script>alert('added');window.location='viewtrainer#abc'</script>")

def updatebatch(requset,id):
    res=Batch.objects.get(id=id)
    return render(requset,'admin/update Batch.html',{'data':res,'id':id})

def updatebatch_post(requset,id):
    batchcapacity=requset.POST['textfield']
    from1=requset.POST['textfield2']
    to=requset.POST['textfield3']
    batchtitle=requset.POST['textfield5']
    Batch.objects.filter(id=id).update(Batch_title=batchtitle,Batch_Capacity=batchcapacity,Time_from=from1,Time_to=to)
    return HttpResponse("<script>alert('added');window.location='/viewbatch#abc'</script>")

def deletebatch(requset,id):
    Batch.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('added');window.location='/viewbatch#abc'</script>")

def updatetrainer(requset,id):
    res=Trainer.objects.get(id=id)
    return render(requset,'admin/update Trainer.html',{'data':res,'id':id})

def updatetraineradmin(requset,id):
    res=Trainer.objects.get(id=id)
    return render(requset,'admin/edit Trainer.html',{'data':res,'id':id})

def updatetrainer_post(requset,id):
    name1 = requset.POST['textfield']
    place1 = requset.POST['textfield2']
    pin1 = requset.POST['textfield3']
    post1 = requset.POST['textfield4']
    age1 = requset.POST['textfield5']
    gender1 = requset.POST['RadioGroup1']
    qualification1 = requset.POST['textarea']
    experience1 = requset.POST['textarea2']
    mnumber1 = requset.POST['textfield6']
    email1 = requset.POST['textfield7']
    Trainer.objects.filter(id=id).update(name=name1,place=place1,pin=pin1,post=post1,age=age1,sex=gender1,qualification=qualification1,experience=experience1,mobilenumber=mnumber1,email=email1)
    return HttpResponse("<script>alert('added');window.location='/viewprofile/#abc'</script>")

def updatetraineradmin_post(requset,id):
    name1 = requset.POST['textfield']
    place1 = requset.POST['textfield2']
    pin1 = requset.POST['textfield3']
    post1 = requset.POST['textfield4']
    age1 = requset.POST['textfield5']
    gender1 = requset.POST['RadioGroup1']
    qualification1 = requset.POST['textarea']
    experience1 = requset.POST['textarea2']
    mnumber1 = requset.POST['textfield6']
    email1 = requset.POST['textfield7']
    Trainer.objects.filter(id=id).update(name=name1,place=place1,pin=pin1,post=post1,age=age1,sex=gender1,qualification=qualification1,experience=experience1,mobilenumber=mnumber1,email=email1)
    return HttpResponse("<script>alert('added');window.location='/viewtrainer#abc'</script>")

def deletetrainer(requset,id):
    trainer_instance = Trainer.objects.get(id=id)

    login_instance = trainer_instance.LOGIN

    trainer_instance.delete()
    login_instance.delete()

    return HttpResponse("<script>alert('Trainer and associated Login deleted');window.location='/viewtrainer#abc'</script>")

def rejectrequest(requset,id):
    return render(requset,"admin/send reason.html",{"id":id})


def deleterequest(requset,id):
    reason=requset.POST['textarea']
    Request.objects.filter(id=id).update(status='rejected   '+reason)

    return HttpResponse("<script>alert('rejected!');window.location='/viewbatch#abc'</script>")

#Trainer side

def addtips(requset, uid):
    return render(requset,'trainer/add tips.html', {'uid':uid})

def addworkout(requset,uid):
    return render(requset,'trainer/add workout.html',{'uid':uid})

def uploaddietplan(requset,id, uid):
    health.objects.filter(id=id)
    return render(requset,'trainer/Upload Diet Plan.html',{'id':id, 'uid':uid})

def uploaddietplan_post(requset,id, uid):
    title1=requset.POST['time']
    description1=requset.POST['description']
    d1 = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    r = Trainer.objects.get(LOGIN=requset.session['lid'])
    obj = diet()
    obj.date = d1
    obj.title=title1
    obj.description=description1
    obj.TRAINER=r
    obj.USER_id=uid
    obj.save()
    return HttpResponse("<script>alert('Added');window.location.href='/uploaddietplan/{}/{}';</script>".format(id,uid))



def viewdietplan(requset,uid):
    res=diet.objects.filter(USER_id=uid)
    if res.exists():
        return render(requset,'trainer/viewdietplan.html',{'data':res})
    else:
        return render(requset,'trainer/nodietplan.html')


def editdietplan(requset,id):
    res = diet.objects.get(id=id)

    return render(requset, 'trainer/edit Diet Plan.html', {'data': res, 'id': id})

def editdietplan_post(requset,id):
    title1=requset.POST['time']
    description1=requset.POST['description']
    d1 = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    diet.objects.filter(id=id).update(title=title1, description=description1, date=d1)
    return HttpResponse("<script>alert('Edited Successfully');window.location='/trainerhome'</script>")

def deletedietplan(requset,id):
    diet.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Edited Successfully');window.location='/trainerhome'</script>")




def viewassignedbatch(requset):
    r = Trainer.objects.get(LOGIN=requset.session['lid'])
    res = assign.objects.filter(TRAINER=r, REQUEST__status="approved")
    if res.exists():
        L = []
        seen_batch_ids = set()

        for i in res:
            re = Request.objects.filter(id=i.REQUEST.id).order_by('BATCH').values()
            rr = Request.objects.filter(BATCH=i.REQUEST.BATCH.id, status="approved").count()
            r1 = assign.objects.filter(REQUEST__BATCH_id=i.REQUEST.BATCH.id, TRAINER=r, REQUEST__status="approved").count()

            for ij in re:
                batch_id = i.REQUEST.BATCH.id

                if batch_id not in seen_batch_ids:
                    a = i.REQUEST.BATCH.Batch_Capacity
                    L.append({
                        "title": i.REQUEST.BATCH.Batch_title,
                        "Batch_Capacity": i.REQUEST.BATCH.Batch_Capacity,
                        "Time_from": i.REQUEST.BATCH.Time_from,
                        "Time_to": i.REQUEST.BATCH.Time_to,
                        "id": batch_id,
                        "rr": rr,
                        "r1": r1,
                        "c": int(a) - int(rr),
                    })
                    seen_batch_ids.add(batch_id)

        return render(requset, 'trainer/view assigned batch.html', {'data': L})
    else:
        return render(requset,'trainer/nobatches.html')

def viewhealthinfo(request, id):
    try:
        user = User.objects.get(id=id)
        request_obj = Request.objects.filter(USER=user).latest('id')  # Assuming the latest request contains the batch information
        batch_id = request_obj.BATCH.id
        health_records = health.objects.filter(USER=user).order_by('-id')
        return render(request, 'trainer/view health info.html', {'data': health_records, 'uid': id, 'batch_id': batch_id})
    except (User.DoesNotExist, Request.DoesNotExist):
        return render(request, 'trainer/nohealth.html')

def viewmembers(requset,id):
    tid = Trainer.objects.get(LOGIN=requset.session['lid'])
    l=[]

    re = assign.objects.filter(TRAINER=tid, REQUEST__status="approved")
    if re.exists():
        for i in re:
            res = Request.objects.filter(BATCH=id, id=i.REQUEST.id)
            for ij in res:
                l.append({
                    "name":ij.USER.name,
                    "place":ij.USER.place,
                    "age":ij.USER.age,
                    "sex":ij.USER.sex,
                    "occupation":ij.USER.occupation,
                    "mobilenumber":ij.USER.mobilenumber,
                    "email":ij.USER.email,
                    "id":ij.USER.id
                })

        return render(requset,'trainer/view members.html',{'data':l})
    else:
        return render(requset,'trainer/nomembers.html')

def viewprofile(requset):
    res=Trainer.objects.get(LOGIN=requset.session['lid'])
    return render(requset,'trainer/view profile.html',{'data':res})

def viewtips(requset,uid):
    r = Trainer.objects.get(LOGIN=requset.session['lid'])
    res = tips.objects.filter(TRAINER=r, USER_id=uid)
    if res.exists():
        return render(requset,'trainer/view tips.html',{'data':res})
    else:
        return render(requset,'trainer/notips.html')


def viewworkout(requset,uid):
    r = Trainer.objects.get(LOGIN=requset.session['lid'])
    res = workout.objects.filter(TRAINER=r,USER_id=uid)
    if res.exists():
        return render(requset,'trainer/view workout.html',{'data':res})
    else:
        return render(requset,'trainer/noworkout.html')


def trainerhome(requset):
    return render(requset,'trainerIndex.html')

def addtips_post(requset,uid):
    title=requset.POST['textfield']
    description=requset.POST['textarea']
    d = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    r = Trainer.objects.get(LOGIN=requset.session['lid'])
    obj=tips()
    obj.title=title
    obj.description=description
    obj.date=d
    obj.TRAINER=r
    obj.USER_id=uid

    obj.save()

    return HttpResponse("<script>alert('Added');window.location.href='/viewtips/{}#abc';</script>".format(uid))


def addworkout_post(requset,uid):
    title=requset.POST['textfield']
    description=requset.POST['textarea']
    video=requset.FILES['fileField']
    d = datetime.datetime.now().strftime("%d%m%Y-%H%M%S")
    d1 = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    r = Trainer.objects.get(LOGIN=requset.session['lid'])
    fs=FileSystemStorage()
    fs.save(r"C:\Users\farhe\PycharmProjects\AI_DIET_CONSULTANT\myapp\static\videos\\" + d +".mp4", video)
    path="/static/videos/" + d + ".mp4"
    r1 = workout.objects.filter(title=title,description=description)
    if r1.exists():
        return HttpResponse("<script>alert('Added');window.location.href='/viewworkout/{}#abc';</script>".format(uid))
    else:
        obj=workout()
        obj.title=title
        obj.description=description
        obj.date=d1
        obj.video=path
        obj.TRAINER=r
        obj.USER_id=uid
        obj.save()
        return HttpResponse("<script>alert('Added');window.location.href='/viewworkout/{}#abc';</script>".format(uid))

def edittip(requset,id):
    res = tips.objects.get(id=id)
    return render(requset, 'trainer/edit tip.html', {'data': res, 'id': id})

def edittip_post(requset,id):
    title = requset.POST['textfield']
    description = requset.POST['textarea']
    d = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    tips.objects.filter(id=id).update(title=title,description=description,date=d)
    return HttpResponse("<script>alert('edited');window.location='/trainerhome'</script>")

def deletetip(requset,id):
    tips.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/trainerhome'</script>")

def editworkout(requset,id):
    res = workout.objects.get(id=id)
    return render(requset, 'trainer/editworkout.html', {'data': res, 'id': id})

def editworkout_post(requset,id):
    title=requset.POST['textfield']
    description=requset.POST['textarea']
    video=requset.FILES['fileField']
    d = datetime.datetime.now().strftime("%d%m%Y-%H%M%S")
    d1 = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\farhe\PycharmProjects\AI_DIET_CONSULTANT\myapp\static\videos\\" + d +".mp4", video)
    path="/static/videos/" + d + ".mp4"
    workout.objects.filter(id=id).update(title=title, description=description, video=path,date=d1)
    return HttpResponse("<script>alert('edited');window.location='/trainerhome'</script>")


def deleteworkout(requset,id):
    workout.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/trainerhome'</script>;")

def chattrainer(requset,id):
    requset.session['uid']=id
    return render(requset,"trainer/chat.html")

def chatsnd(request):

      if request.method=="POST":
        d=datetime.datetime.now().strftime("%Y-%m-%d")
        c = request.session['lid']
        m=request.POST['m']
        cc = Trainer.objects.get(LOGIN__id=c)
        uu = User.objects.get(id=request.session['uid'])
        obj=chat()
        obj.date=d
        obj.usertype='trainer'
        obj.TRAINER=cc
        obj.USER=uu
        obj.chat=m
        obj.save()
        v = {}
        if int(obj) > 0:
            v["status"] = "ok"
        else:
            v["status"] = "error"
        r = demjson.encode(v)
        return r




def chatrply(request):

        c = request.session['lid']
        cc=Trainer.objects.get(LOGIN__id=c)
        uu=User.objects.get(id=request.session['uid'])
        res = chat.objects.filter(TRAINER_id=cc,USER_id=uu)
        v = []
        if len(res) > 0:
            for i in res:
                v.append({
                    'type':i.usertype,
                    'chat':i.chat,
                })

            return JsonResponse({"status": "ok", "data": v, "id": cc.id})
        else:
            return JsonResponse({"status": "error"})

#user side

def chatuser(requset,id):
    requset.session['uid']=id
    return render(requset,"user/chat.html")

def Uchatsent(request):
      if request.method=="POST":

        d=datetime.datetime.now().strftime("%Y-%m-%d")

        c = request.session['lid']

        m=request.POST['m']
        cc = User.objects.get(LOGIN__id=c)
        uu = Trainer.objects.get(id=request.session['uid'])

        obj=chat()
        obj.chat_date=d

        obj.usertype='user'
        obj.TRAINER=uu
        obj.USER=cc
        obj.date=d
        obj.chat=m
        obj.save()
        v = {}
        v["status"] = "ok"
        r = demjson.encode(v)

        return JsonResponse({'status':"ok"})




def Uchatrply(request):

        c = request.session['lid']
        uu=User.objects.get(LOGIN__id=c)
        cc=Trainer.objects.get(id=request.session['uid'])
        res = chat.objects.filter(TRAINER_id=cc,USER_id=uu)
        v = []
        if len(res) > 0:
            for i in res:
                v.append({
                    'type':i.usertype,
                    'chat':i.chat,
                })

            return JsonResponse({"status": "ok", "data": v, "id": cc.id})
        else:
            return JsonResponse({"status": "error"})



def register(requset):
    return render(requset, "user/register.html")

def viewuserprofile(requset):
    res = User.objects.get(LOGIN=requset.session['lid'])
    return render(requset,"user/viewprofile.html",{"data":res})

def register_post(requset):
    name1=requset.POST['textfield']
    place1=requset.POST['textfield2']
    pin1=requset.POST['textfield3']
    post1=requset.POST['textfield4']
    age1=requset.POST['textfield5']
    gender1=requset.POST['RadioGroup1']
    occupation1=requset.POST['textfield8']
    password1=requset.POST['textfield9']
    cpassword=requset.POST['textfield10']
    mnumber1=requset.POST['textfield6']
    email1=requset.POST['textfield7']

    r = User.objects.filter(name=name1,place=place1,pin=pin1,post=post1,age=age1,sex=gender1,occupation=occupation1,
                            mobilenumber=mnumber1,email=email1)
    r1 = Login.objects.filter(username=email1)
    if r.exists():
        if r1.exists():
            return HttpResponse("<script>alert('Email Already Exists');window.location='register'</script>")

        return HttpResponse("<script>alert('Trainer Already Exists');window.location='register'</script>")
    else:
        obj2=Login()
        obj2.username=email1
        obj2.password=password1
        obj2.usertype='user'
        obj2.save()
        obj=User()
        obj.name=name1
        obj.place=place1
        obj.pin=pin1
        obj.post = post1
        obj.age=age1
        obj.sex = gender1
        obj.occupation = occupation1
        obj.mobilenumber = mnumber1
        obj.email = email1
        obj.LOGIN=obj2
        obj.save()
        return HttpResponse("<script>alert('Registered Successfully');window.location='/'</script>")

def updateuser(requset,id):
    res=User.objects.get(id=id)
    res1 = Login.objects.get(id=id)
    return render(requset,'user/updateprofile.html',{'data':res,'id':id,'data1':res1})

def updateuser_post(requset,id):
    name1 = requset.POST['textfield']
    place1 = requset.POST['textfield2']
    pin1 = requset.POST['textfield3']
    post1 = requset.POST['textfield4']
    age1 = requset.POST['textfield5']
    gender1 = requset.POST['RadioGroup1']
    occupation1 = requset.POST['textfield8']
    password1 = requset.POST['textfield9']
    mnumber1 = requset.POST['textfield6']
    email1 = requset.POST['textfield7']
    User.objects.filter(id=id).update(name=name1, place=place1, pin=pin1, post=post1, age=age1, sex=gender1,
                                         occupation=occupation1,mobilenumber=mnumber1,email=email1)
    Login.objects.filter(id=requset.session['lid']).update(password=password1)
    return HttpResponse("<script>alert('Updated Successfully');window.location='/viewuserprofile'</script>")

def userhome(requset):
    return render(requset,'userIndex.html')

def uploadhealth(requset):
    res = health.objects.filter(USER_id=User.objects.get(LOGIN_id=requset.session['lid'])).order_by('-id')

    if res.exists():
        return render(requset, 'user/uploadhealthinfo.html',{'data': res[0]})
    else:
        return render(requset, 'user/uploadhealthinfo.html')

def uploadhealth_post(requset):
    height1=requset.POST['textfield']
    weight1=requset.POST['textfield2']
    height=float(height1)/100
    bmi1= round(float(weight1) / (height * height), 2)
    active=requset.POST['select']
    foodtype1=requset.POST['RadioGroup1']
    target1=requset.POST['RadioGroup2']
    targetweight1=requset.POST['textfield3']
    weeklytarget1=requset.POST['select2']
    estimatedtime1=requset.POST['textfield4']
    mcondition1=requset.POST.getlist('CheckboxGroup1')
    allergies1=requset.POST['textfield6']
    uid = User.objects.get(LOGIN=requset.session['lid'])

    obj=health()
    obj.height=height1
    obj.weight=weight1
    obj.activelevel=active
    obj.medical=",".join(mcondition1)
    obj.bmi=bmi1
    obj.foodtype=foodtype1
    obj.target=target1
    obj.targetweight=targetweight1
    obj.estimatedtime=estimatedtime1
    obj.weeklytarget=weeklytarget1
    obj.USER=uid
    obj.allergies=allergies1

    obj.save()

    return HttpResponse("<script>window.location='/viewhealth#abc'</script>")

def sendfeedback(requset):
    return render(requset, 'user/send feedback.html')

def sendfeedback_post(requset):
    feedbackk=requset.POST['textarea']
    d1 = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    r = feedback.objects.filter(time=d1)
    if r.exists():
        return HttpResponse("alert('already submitted');window.location='sendfeedback/#abc'")
    else:
        obj=feedback()
        obj.feedback=feedbackk
        obj.time=d1
        obj.USER=User.objects.get(LOGIN=requset.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Successfully Sent');window.location='/userhome'</script>")



def viewtipsuser(requset):
    res = tips.objects.filter(USER__LOGIN_id=requset.session['lid'])
    if res.exists():
        return render(requset,'user/view tips.html',{'data':res})
    else:
        return render(requset,'user/notips.html')

def viewworkoutuser(requset):
    res = workout.objects.filter(USER__LOGIN_id=requset.session['lid'])
    if res.exists():
        return render(requset,'user/view workout.html',{'data':res})
    else:
        return render(requset,'user/noworkouts.html')


def viewbatchuser(request):

    batches = Batch.objects.all()

    if batches.exists():


        batch_list = []
        request_list = []




        for batch in batches:

            assignment_count = assign.objects.filter(REQUEST__BATCH=batch.id).count()


            capacity_remaining = int(batch.Batch_Capacity) - int(assignment_count)


            batch_list.append({
                "id": batch.id,
                "Batch_title": batch.Batch_title,
                "Batch_Capacity": batch.Batch_Capacity,
                "Time_from": batch.Time_from,
                "Time_to": batch.Time_to,
                "Capacity_remaining": capacity_remaining,
                "assignment_count": assignment_count,
            })

        user_requests2 = Request.objects.filter(USER__LOGIN__id=request.session['lid']).order_by('-id')


        if user_requests2.exists():
            user_requests2 = user_requests2[0]

            request_list.append({
                "status": user_requests2.status,
            })
        else:

            request_list.append({})


        return render(request, 'user/view batch.html', {'data': batch_list, 'data1': request_list})
    else:
        return render(request, 'user/nobatches.html')


def sendrequest(requset,id,jid):
    d1 = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

    res = Request.objects.filter(
        Q(USER=User.objects.get(LOGIN=requset.session['lid']), status="approved") |
        Q(USER=User.objects.get(LOGIN=requset.session['lid']), status="pending")
    )
    res1 = health.objects.filter(USER__LOGIN_id=requset.session['lid'])
    res3= Batch.objects.filter(Batch_Capacity=jid)
    if res3.exists():
        return HttpResponse("<script>alert('Batch is full');window.location='/viewbatchuser#abc'</script>")
    else:
        if res1.exists():
            if res.exists():
                return HttpResponse("<script>alert('already sent');window.location='/viewbatchuser#abc'</script>")
            obj=Request()
            obj.USER=User.objects.get(LOGIN=requset.session['lid'])
            obj.BATCH_id=id
            obj.time=d1
            obj.status="pending"
            obj.save()
            return HttpResponse("<script>alert('Successfully sent');window.location='/viewbatchuser#abc'</script>")
        else:
            return HttpResponse("<script>alert('Please enter health details before sending request');window.location='/uploadhealth/#abc'</script>")


def viewhealth(requset):
    res = health.objects.filter(USER__LOGIN_id= requset.session['lid']).order_by('-id')
    if res.exists():
        return render(requset, 'user/viewhealthuser.html', {'data': res[0]})
    else:
        return HttpResponse("<script>alert('Enter Health Details');window.location='/uploadhealth#abc'</script>")



def updatehealth(requset,id):
    res = health.objects.get(id=id)
    return render(requset,'user/updatehealth.html',{'data':res})

def updatehealth_post(requset,id):
    height1 = requset.POST['textfield']
    weight1 = requset.POST['textfield2']
    height = float(height1) / 100
    bmi1 = round(float(weight1) / (height * height), 2)
    active = requset.POST['select']
    foodtype1 = requset.POST['RadioGroup1']
    target1 = requset.POST['RadioGroup2']
    targetweight1 = requset.POST['textfield3']
    weeklytarget1 = requset.POST['select2']
    estimatedtime1 = requset.POST['textfield4']
    mcondition1 = requset.POST.getlist('CheckboxGroup1')
    allergies1 = requset.POST['textfield6']
    health.objects.filter(id=id).update(height=height1,weight=weight1,bmi=bmi1,activelevel=active,foodtype=foodtype1,
                                        target=target1,targetweight=targetweight1,weeklytarget=weeklytarget1,estimatedtime=estimatedtime1,
                                        medical=",".join(mcondition1),allergies=allergies1)
    return HttpResponse("<script>alert('edited');window.location='/viewhealth'</script>")

def mybatch(requset):
    r=Request.objects.filter(USER__LOGIN_id=requset.session['lid'], status="approved")
    if r.exists():
        l=[]
        for i in r:
            res=assign.objects.filter(REQUEST=i.id)
            for ij in res:
                l.append({
                    "name":i.BATCH.Batch_title,
                    "cap": i.BATCH.Batch_Capacity,
                    "tfrom": i.BATCH.Time_from,
                    "tTo": i.BATCH.Time_to,
                    "tname": ij.TRAINER.name,
                    "id":ij.TRAINER.id,
                    "bid":i.id
                })

        return render(requset,'user/mybatch.html',{'data':l})
    else:
        return HttpResponse("<script>alert('You are not assigned to any batch!!!');window.location='/userhome';</script>")


def user_exit_batch(request, id):
    Request.objects.filter(id=id).update(status="Left")
    return HttpResponse("<script>alert('Successfully left the batch');window.location='/userhome';</script>")

def viewdietplanuser(requset):
    res =diet.objects.filter(USER__LOGIN_id=requset.session['lid'])
    if res.exists():
        return render(requset,'user/viewdietplanuser.html',{'data':res})
    else:
        return render(requset,'user/nodietplan.html')

def myprogress(requset):
    res = health.objects.filter(USER=User.objects.get(LOGIN_id=requset.session['lid'])).order_by('-id')
    res2 = health.objects.filter(USER=User.objects.get(LOGIN_id=requset.session['lid']))

    if res2.exists():
        lis = []
        months = []
        cnt = 1
        for i in res2:
            lis.append(int(i.weight))
            months.append("Month " + str(cnt))
            cnt += 1

        fig, ax = plt.subplots()
        ax.plot(months, lis)

        canvas = FigureCanvasAgg(fig)
        response = HttpResponse(content_type='image/png')
        canvas.print_png(response)


        d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        plt.savefig(r"C:\Users\farhe\PycharmProjects\AI_DIET_CONSULTANT\myapp\static\charts\\" + d + ".png")

        path = "/static/charts/" + d + ".png"
        return render(requset, 'user/myprogress.html', {'data': res, 'chart_path': path})
    else:
        return HttpResponse("<script>alert('Please enter health details');window.location='/uploadhealth/#abc'</script>")

def myprogresstrainer(requset,id):
    res = health.objects.filter(USER=id).order_by('-id')
    res2 = health.objects.filter(USER=id)

    if res2.exists():
        lis = []
        months = []
        cnt = 1
        for i in res2:
            lis.append(int(i.weight))
            months.append("Month " + str(cnt))
            cnt += 1

        fig, ax = plt.subplots()
        ax.plot(months, lis)

        canvas = FigureCanvasAgg(fig)
        response = HttpResponse(content_type='image/png')
        canvas.print_png(response)


        d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        plt.savefig(r"C:\Users\farhe\PycharmProjects\AI_DIET_CONSULTANT\myapp\static\charts\\" + d + ".png")

        path = "/static/charts/" + d + ".png"
        return render(requset, 'trainer/myprogresstrainer.html', {'data': res, 'chart_path': path})
    else:
        return HttpResponse("<script>alert('Progress not available');window.location='/trainerhome'</script>")

def forgot_pass(request):
    return render(request, "forget_password.html")

def forgot_pass_post(request):
    email=request.POST['textfield']
    log_obj=Login.objects.filter(username=email)
    if log_obj.exists():
        res=log_obj[0]
        import smtplib

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("nutrifit20241@gmail.com", "yuxxqtudpztjkzbl")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "nutrifit20241@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Your Password for NUTRIFIT"
        body = " Your password is : " + str(res.password)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)

        return HttpResponse("<script>alert('Password sent to mail');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('Username not found');window.location='/'</script>")

def deleteuser(requset,id):

        user_to_delete = User.objects.get(id=id)

        login_to_delete = user_to_delete.LOGIN

        user_to_delete.delete()


        login_to_delete.delete()

        return HttpResponse("<script>alert('User deleted successfully');window.location='/viewbatch#abc'</script>")

def deleteuserprofile(requset,id):

        user_to_delete = User.objects.get(id=id)

        login_to_delete = user_to_delete.LOGIN

        user_to_delete.delete()

        login_to_delete.delete()

        return HttpResponse("<script>alert('Profile deleted successfully');window.location='/'</script>")
