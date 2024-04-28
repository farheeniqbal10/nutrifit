from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=20)


class Trainer(models.Model):
    LOGIN=models.ForeignKey(Login,default=1,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    pin=models.CharField(max_length=20)
    post=models.CharField(max_length=20)
    age=models.CharField(max_length=3)
    sex=models.CharField(max_length=6)
    qualification = models.CharField(max_length=100)
    email=models.CharField(max_length=100, default="")
    mobilenumber = models.CharField(max_length=20, default="1234")
    experience = models.CharField(max_length=200)


class Batch(models.Model):
    Batch_title=models.CharField(max_length=20,default="")
    Batch_Capacity=models.CharField(max_length=20)
    Time_from=models.CharField(max_length=20)
    Time_to=models.CharField(max_length=20)

class User(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    pin = models.CharField(max_length=20)
    post = models.CharField(max_length=20)
    age = models.CharField(max_length=6)
    sex = models.CharField(max_length=6)
    email=models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)

class Request(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    BATCH=models.ForeignKey(Batch,default=1, on_delete=models.CASCADE)
    time=models.CharField(max_length=20)
    status=models.CharField(max_length=200)

class assign(models.Model):
    REQUEST=models.ForeignKey(Request, default=1, on_delete=models.CASCADE)
    TRAINER=models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)

class feedback(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)
    feedback=models.CharField(max_length=2000)

class health(models.Model):
    USER=models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    height=models.CharField(max_length=3)
    weight=models.CharField(max_length=3)
    activelevel=models.CharField(max_length=30)
    medical=models.CharField(max_length=500)
    bmi=models.CharField(max_length=10)
    foodtype=models.CharField(max_length=10)
    target=models.CharField(max_length=10)
    targetweight = models.CharField(max_length=10, default="")
    estimatedtime=models.CharField(max_length=10,default="")
    weeklytarget=models.CharField(max_length=10,default="")
    allergies=models.CharField(max_length=500,default="None")

class diet(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    title = models.CharField(max_length=200,default="")
    description = models.CharField(max_length=3000,default="")


class tips(models.Model):
    TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    USER=models.ForeignKey(User,default=1,on_delete=models.CASCADE)

class workout(models.Model):
    TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    video = models.CharField(max_length=500)
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

class chat(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    usertype = models.CharField(max_length=10)
    chat = models.CharField(max_length=300)








