#_*_encoding:utf-8 _*_
from datetime import datetime

from django.db import models


# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=50,verbose_name=u'城市')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    desc=models.CharField(max_length=200,verbose_name=u'描述')
    
    class Meta:
        verbose_name=u'城市'
        verbose_name_plural=verbose_name
        
    def __str__(self):
        return self.name
#课程机构
class CourseOrg(models.Model):
    name=models.CharField(max_length=50,verbose_name=u'机构名称')
    desc=models.TextField(verbose_name=u' 机构描述')
    click_num=models.IntegerField(default=0,verbose_name=u'点击数')
    fav_num=models.IntegerField(default=0,verbose_name=u'收藏人数')
    img=models.ImageField(upload_to='org/%Y/%m',verbose_name=u'封面图',max_length=100)
    address=models.CharField(max_length=150,verbose_name=u'机构地址')
    city=models.ForeignKey(City,verbose_name=u'城市',on_delete=models.CASCADE )
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    
    
    class Meta:
        verbose_name=u'课程机构'
        verbose_name_plural=verbose_name
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name=models.CharField(max_length=50,verbose_name=u'教师名称')
    work_years=models.IntegerField(default=0,verbose_name=u'工作年限')
    work_company=models.CharField(max_length=50,verbose_name=u'就职公司')
    work_position=models.CharField(max_length=50,verbose_name=u'公司职位')
    points=models.CharField(max_length=50,verbose_name=u'教学特点')
    click_num=models.IntegerField(default=0,verbose_name=u'点击数')
    fav_num=models.IntegerField(default=0,verbose_name=u'收藏人数')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    org=models.ForeignKey(CourseOrg,verbose_name=u'所属机构',on_delete=models.CASCADE) 
    
    
    class Meta:
        verbose_name=u'教师'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
    
    
    
    
    
    
    
    
    

        



















