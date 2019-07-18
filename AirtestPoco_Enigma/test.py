from airtest.core.api import *
from function.Page import Page

# auto_setup(__file__)
# dev = connect_device("android:///127.0.0.1:7555")
# devs = device()
# print(devs.list_app(third_only=True))
# poco = AndroidUiautomationPoco(dev)
# start_app('com.enigma.im',activity=None)
# sleep(3)



# perform swipe without UI selected
# x = poco('android.widget.FrameLayout').get_position()
# print(x)
# end = [x, y-5]
# dir = [0, -0.1]
# poco.swipe([x, y], end)  # drag from point A to point B
# poco.swipe([x, y], direction=dir)  # drag from point A toward given direction and length
# poco('android.widget.FrameLayout').swipe( direction=[1,0])





    #     def swipe_to_left(self):
    #         swipe(self.right_point,self.left_point)
    #         sleep(2)
    #     def swipe_to_right(self):
    #         swipe(self.left_point,self.right_point)
    #         sleep(2)
class Basefunc(Page):
    def __init__(self):
        Page.__init__(self)


    #滑动操作
    def left_swipe(self):
        print("左滑开始：：：：")
        self.enigma_main.swipe(direction=[1,0])
        print("左滑结束：：：：")

    def right_swipe(self):
        print("右滑开始：：：：")
        self.enigma_main.swipe(direction=[-1,0])
        print("右滑结束：：：：")

    def up_swipe(self):
        print("上滑开始：：：：")
        self.enigma_main.swipe(direction=[0,1])
        print("上滑结束：：：：")

    def down_swipe(self):
        print("下滑开始：：：：")
        self.enigma_main.swipe(direction=[0,-1])
        print("下滑结束：：：：")

    def login(self,phone="20000000006",doublePwd="123"):
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
            if not self.code355.exists():
                self.country_code.click()
                self.search_code.set_text("355")
                self.poco(text="阿尔巴尼亚").click()
            # 输入手机号
            self.input_phone.set_text(phone)
            # 发送验证码
            self.send_code.click()
            # 输入验证码
            self.input_code.set_text("666666")
            # 点击登录按钮
            self.login_btn.click()
            # 确认登录此账户
            self.confirm_login.click()
            # 选择登录方式:::设备丢失
            self.device_loss.click()
            self.confirm_loss.click()
            # 二次验证
            if self.page_doubleverify.exists():
                self.input_double_passwd.set_text(doublePwd)
                self.next.click()

        except Exception as e:
            print(f"登录失败：：：{e}")

    def logout(self):
        while not self.icon_settings.exists():
            self.left_swipe()
            sleep(2)

        #self.icon_settings.wait_for_appearance()
        self.icon_settings.click()
        self.my_info.wait_for_appearance()
        self.my_info.click()
        self.logout_btn.wait_for_appearance()
        self.logout_btn.click()
        self.confirm_logout.click()



if __name__=="__main__":
    # while 1:
        # Basefunc().login()
        # Basefunc().logout()
    Basefunc().up_swipe()