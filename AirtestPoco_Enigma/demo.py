# # encoding=utf8
#
# __author__ = "Administrator"
#
# from airtest.core.api import *
# # from airtest.core.android import minitouch
# from airtest.cli.parser import cli_setup
# from poco.exceptions import PocoTargetTimeout
# auto_setup(__file__)
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
#
# # PKG = "com.enigma.im"
# # APK = "enigma-2.05.5-extserver-formal.apk"
#
# '''
# basedir – 设置当前脚本的所在路径，也可以直接传 __file__ 变量进来
# devices – 一个内容为 connect_device uri 字符串的列表
# logdir – 可设置脚本运行时的log保存路径，默认值为None则不保存log，如果设置为True则自动保存在<basedir>/log目录中
# project_root – 用于设置PROJECT_ROOT变量，方便 using 接口的调用
# '''
# if not cli_setup():
#     auto_setup(basedir=__file__, devices=["android:///127.0.0.1:7555"], logdir=True)
#     print("————————————————连接成功——————————————")
#
# # #实例化poco
# poco = AndroidUiautomationPoco(use_airtest_input=True,screenshot_each_action=False)
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.exceptions import PocoTargetTimeout

dev = auto_setup(__file__,devices=["android:///127.0.0.1:7555"])

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(dev)


class Basefunc():
    def __init__(self):
        #         self.left_point=(0.2*self.width,0.75*self.height)
        #         self.right_point=(0.8*self.width,0.75*self.height)
        #         self.up_point=(0.5*self.width,0.25*self.height)
        #         self.down_point=(0.5*self.width,0.75*self.height)

        # 搜索国家码
        self.country_code = poco("com.enigma.im:id/connect_text_view")
        self.search_code = poco("com.enigma.im:id/searchView")

        # 登录界面
        self.input_phone = poco("com.enigma.im:id/input_phone").offspring("com.enigma.im:id/input")
        self.input_code = poco("com.enigma.im:id/input_code").offspring("com.enigma.im:id/input")
        self.login_clear = poco(name="com.enigma.im:id/btn_clear", type="android.widget.ImageView")
        self.send_code = poco("com.enigma.im:id/handle")
        self.login_btn = poco("com.enigma.im:id/btn_login_pic")
        self.force_login = poco("com.enigma.im:id/btn_register")
        self.confirm_login = poco("com.enigma.im:id/btn_right")

        # 聊天列表
        self.icon_chart = poco("com.enigma.im:id/nv_menu_session").offspring("com.enigma.im:id/iv_icon")
        self.icon_contacts = poco("com.enigma.im:id/nv_menu_contacts ").offspring("com.enigma.im:id/iv_icon")
        self.icon_settings = poco("com.enigma.im:id/nv_menu_settings").offspring("com.enigma.im:id/iv_icon")

        # 会话窗口
        #         self.last_msg = poco("com.enigma.im:id/rv_chat").child("android.view.ViewGroup$MarginLayoutParams")[0].offspring("com.enigma.im:id/fl_message_content")
        self.input_box = poco("com.enigma.im:id/text")
        self.into_details = poco("com.enigma.im:id/fl_header")

        # 我的
        self.my_info = poco("com.enigma.im:id/user_item").offspring("android.widget.LinearLayout")
        self.logout_btn = poco("com.enigma.im:id/btn_logout")
        self.confirm_logout = poco("com.enigma.im:id/btn_right")

    #     def swipe_to_left(self):
    #         swipe(self.right_point,self.left_point)
    #         sleep(2)
    #     def swipe_to_right(self):
    #         swipe(self.left_point,self.right_point)
    #         sleep(2)

    def left_swipe(self):
        print("左滑开始：：：：")
        swipe((50, 700), (650, 700))
        print("左滑成功：：：：")

    def down_swipe(self):
        swipe((350, 1200), (350, 200))

    def login(self, phone="20000000006"):
        try:
            if not self.input_phone.exists():
                self.left_swipe()
                sleep(2)
            if not self.input_phone.exists():
                self.logout()

            self.input_phone.click()
            if self.login_clear.exists():
                self.login_clear.click()

            # 选择国家码
            if not poco(text="+355").exists():
                self.country_code.click()
                self.search_code.set_text("355")
                poco(text="阿尔巴尼亚").click()
            # 输入手机号
            self.input_phone.set_text(phone)
            # 发送验证码
            self.send_code.click()
            # 输入验证码
            self.input_code.set_text("666666")
            # 点击登录按钮
            self.login_btn.click()
            # 强制登录
            if self.force_login.exists():
                self.force_login.click()
                self.confirm_login.click()

        except Exception:
            print("登录失败：：：")

    def logout(self):
        while not self.icon_settings.exists():
            self.left_swipe()
            sleep(2)

        #         self.icon_settings.wait_for_appearance()
        self.icon_settings.click()
        self.my_info.wait_for_appearance()
        self.my_info.click()
        self.logout_btn.wait_for_appearance()
        self.logout_btn.click()
        self.confirm_logout.click()










