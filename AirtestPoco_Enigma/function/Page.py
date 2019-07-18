from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco



class Page():
    def __init__(self):

        auto_setup(__file__)
        dev = connect_device("android:///127.0.0.1:7555")
        # devs = device()
        #打印手机APP列表
        # print(devs.list_app(third_only=True))
        self.poco = AndroidUiautomationPoco(dev)
        start_app('com.enigma.im', activity=None)
        sleep(2)

        self.enigma_main = self.poco('android.widget.FrameLayout')

    #     # 选择国家码界面
    #     self.code355 = self.poco(text="+355")
    #     self.country_code = self.poco("com.enigma.im:id/connect_text_view")
    #     self.search_code = self.poco("com.enigma.im:id/searchView")
    #
    #     # 登录界面
    #     #:::手机号输入框
    #     self.input_phone = self.poco("com.enigma.im:id/input_phone").offspring("com.enigma.im:id/input")
    #     #:::验证码输入框
    #     self.input_code = self.poco("com.enigma.im:id/input_code").offspring("com.enigma.im:id/input")
    #     #:::清空按钮
    #     self.login_clear = self.poco(name="com.enigma.im:id/btn_clear", type="android.widget.ImageView")
    #     #:::发送验证码
    #     self.send_code = self.poco("com.enigma.im:id/handle")
    #     #:::登录按钮
    #     self.login_btn = self.poco("com.enigma.im:id/btn_login_pic")
    #     #:::登录此账户
    #     self.confirm_login = self.poco("com.enigma.im:id/yes_title")
    #     #:::取消关联账户
    #     self.cancel_login = self.poco("com.enigma.im:id/no_title")
    #     #:::设备丢失
    #     self.device_loss = self.poco("com.enigma.im:id/loss")
    #     self.confirm_loss = self.poco(text="确定")
    #     self.cancel_loss = self.poco(text="取消")
    #     #:::两步验证页面
    #     self.page_doubleverify = self.poco(text="两步验证", name="com.enigma.im:id/tv_toolbar_title")
    #     self.input_double_passwd = self.poco("com.enigma.im:id/input")
    #     self.next = self.poco(text="下一步")
    #
    # # 聊天列表界面
    #     self.icon_chart = self.poco("com.enigma.im:id/nv_menu_session").offspring("com.enigma.im:id/iv_icon")
    #     self.icon_contacts = self.poco("com.enigma.im:id/nv_menu_contacts ").offspring("com.enigma.im:id/iv_icon")
    #     self.icon_settings = self.poco("com.enigma.im:id/nv_menu_settings").offspring("com.enigma.im:id/iv_icon")

    # # 会话窗口界面
    #     self.last_msg = self.poco("com.enigma.im:id/rv_chat").child("android.view.ViewGroup$MarginLayoutParams")[0].offspring("com.enigma.im:id/fl_message_content")
    #     self.input_box = self.poco("com.enigma.im:id/text")
    #     self.into_details = self.poco("com.enigma.im:id/fl_header")

    # # 我的界面
    #     self.my_info = self.poco("com.enigma.im:id/user_item").offspring("android.widget.LinearLayout")
    #     self.logout_btn = self.poco("com.enigma.im:id/btn_logout")
    #     self.confirm_logout = self.poco("com.enigma.im:id/btn_right")

    # 滑动操作
    def left_swipe(self):
        print("左滑开始：：：：")
        self.enigma_main.swipe(direction=[1, 0])
        print("左滑结束：：：：")

    def right_swipe(self):
        print("右滑开始：：：：")
        self.enigma_main.swipe(direction=[-1, 0])
        print("右滑结束：：：：")

    def up_swipe(self):
        print("上滑开始：：：：")
        self.enigma_main.swipe(direction=[0, 1])
        print("上滑结束：：：：")

    def down_swipe(self):
        print("下滑开始：：：：")
        self.enigma_main.swipe(direction=[0, -1])
        print("下滑结束：：：：")


