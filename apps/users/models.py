#_*_encoding:utf-8 _*_
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
#用户model
class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name=u'昵称',default="")
    birthday=models.DateField(verbose_name=u'生日',null=True,blank=True)
    gender=models.CharField(choices=(('male',u"男"),('female',u'女')),default="female",max_length=6,verbose_name=u'性别')
    add=models.CharField(max_length=100,verbose_name=u'地址',default="")
    mobile=models.CharField(max_length=11,verbose_name=u'电话',null=True,blank=True)
    img=models.ImageField(upload_to="img/%Y/%m",default=u'img/def.png',max_length=100,verbose_name=u'头像')
    
    class Meta:
        verbose_name=u'用户信息'
        verbose_name_plural=verbose_name
        
    def __str__(self):
        return self.username
    
    
#邮箱验证码    
class EmailVerifyCode(models.Model):
    code=models.CharField(max_length=20,verbose_name=u'邮箱验证码')
    email=models.EmailField(max_length=50,verbose_name=u'邮箱')
    send_type=models.CharField(choices=(('register',u'注册'),('forget',u'找回密码')),max_length=10,verbose_name=u'验证码类型')
    send_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    
    class Meta:
        verbose_name=u'邮箱验证码'
        verbose_name_plural=verbose_name
        
    def __str__(self):
        return '{0}({1})'.format(self.code,self.email)
#轮播图        
class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name=u'标题')
    img=models.ImageField(upload_to='banner/%Y/%m',verbose_name=u'轮播图',max_length=20)
    url=models.URLField(max_length=200,verbose_name=u'访问地址')
    index=models.IntegerField(default=100,verbose_name=u'顺序')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    
    class Meta:
        verbose_name=u'轮播图'
        verbose_name_plural=verbose_name
        














