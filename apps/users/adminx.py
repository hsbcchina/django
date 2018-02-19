'''
Created on 2018年1月18日

@author: bert
'''
import xadmin
from xadmin import views
from .models import EmailVerifyCode,Banner


class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True
xadmin.site.register(views.BaseAdminView,BaseSetting)

class GlobalSetting:
    site_title='马红在线'
    site_footer='马宏实业'
    menu_style='accordion'
xadmin.site.register(views.CommAdminView,GlobalSetting)

#邮箱验证码
class EmailVerifyCodeAdmin(object):
    list_display=['email','code','send_type','send_time']
    search_fields=['email','code','send_type']
    list_filter=['email','code','send_type','send_time']
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeAdmin)

#轮播图
class BannerAdmin(object):
    list_display=['title','img','url','index','add_time']
    search_fields=['title','img','url','index']
    list_filter=['title','img','url','index','add_time']
xadmin.site.register(Banner,BannerAdmin)





