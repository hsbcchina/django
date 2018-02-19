'''
Created on 2018年1月19日

@author: bert
'''
import xadmin
from .models import UserAsk,CourseComment,UserFavourite,UserMessage,UserCourse
 
#用户咨询
class UserAskAdmin(object):
    list_display=['name','mobile','course_name','add_time']
    search_fields=['name','mobile','course_name']
    list_filter=['name','mobile','course_name','add_time']
xadmin.site.register(UserAsk,UserAskAdmin)

#课程评论
class CourseCommentAdmin(object):
    list_display=['user','course','comments','add_time']
    search_fields=['user','course','comments']
    list_filter=['user','course','comments','add_time']
xadmin.site.register(CourseComment,CourseCommentAdmin)

#课程收藏
class UserFavouriteAdmin(object):
    list_display=['user','fav_id','fav_type','add_time']
    search_fields=['user','fav_id','fav_type']
    list_filter=['user','fav_id','fav_type','add_time']
xadmin.site.register(UserFavourite,UserFavouriteAdmin)

#用户消息
class UserMessageAdmin(object):
    list_display=['user','msg','has_read','add_time']
    search_fields=['user','msg','has_read']
    list_filter=['user','msg','has_read','add_time']
xadmin.site.register(UserMessage,UserMessageAdmin)

#用户课程
class UserCourseAdmin(object):
    list_display=['user','course','add_time']
    search_fields=['user','course']
    list_filter=['user','course','add_time']
xadmin.site.register(UserCourse,UserCourseAdmin)


