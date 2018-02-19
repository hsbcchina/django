'''
Created on 2018年1月19日

@author: bert
'''
import xadmin
from .models import Course,Lensson,Video,CourseResource
 
#课程 
class CourseAdmin(object):
    list_display=['name','desc','detail','add_time']
    search_fields=['name','desc','detail']
    list_filter=['name','desc','detail','add_time']
xadmin.site.register(Course,CourseAdmin) 
 
 
#章节 
class LenssonAdmin(object):
    list_display=['name','course','add_time']
    search_fields=['name','course']
    list_filter=['name','course__name','add_time']
xadmin.site.register(Lensson,LenssonAdmin) 

#章节 
class VideoAdmin(object):
    list_display=['name','lesson','add_time']
    search_fields=['name','lesson']
    list_filter=['name','lesson','add_time']
xadmin.site.register(Video,VideoAdmin) 
 
#课程资源 
class CourseResourceAdmin(object):
    list_display=['name','course','add_time']
    search_fields=['name','course']
    list_filter=['name','course','add_time']
xadmin.site.register(CourseResource,CourseResourceAdmin)  
 
 
 
 
 
 
 