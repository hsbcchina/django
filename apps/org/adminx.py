'''
Created on 2018年1月19日

@author: bert
'''
import xadmin
from .models import City,CourseOrg,Teacher
 
#城市
class CityAdmin(object):
    list_display=['name','desc','add_time']
    search_fields=['name','desc']
    list_filter=['name','desc','add_time']
xadmin.site.register(City,CityAdmin)


#课程机构
class CourseOrgAdmin(object):
    list_display=['name','desc','address','add_time']
    search_fields=['name','desc','address']
    list_filter=['name','desc','address','add_time']
xadmin.site.register(CourseOrg,CourseOrgAdmin)


#教师
class TeacherAdmin(object):
    list_display=['name','work_years','work_company','add_time']
    search_fields=['name','work_years','work_company']
    list_filter=['name','work_years','work_company','add_time']
xadmin.site.register(Teacher,TeacherAdmin)






