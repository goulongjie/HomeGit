from function.Page import Page
from time import sleep


class page_login(Page):
    def __init__(self):
        Page.__init__(self)

        # 选择国家码界面
        self.ele_code355 = self.poco(text="+355")
        self.ele_countryCode = self.poco("com.enigma.im:id/connect_text_view")
        self.ele_setCountryCode = self.poco("com.enigma.im:id/searchView")

        # 登录界面
        #:::手机号输入框
        self.ele_setPhone = self.poco("com.enigma.im:id/input_phone").offspring("com.enigma.im:id/input")
        #:::验证码输入框
        self.ele_setAuthCode = self.poco("com.enigma.im:id/input_code").offspring("com.enigma.im:id/input")
        #:::清空按钮
        self.ele_clearInput = self.poco(name="com.enigma.im:id/btn_clear", type="android.widget.ImageView")
        #:::发送验证码
        self.ele_sendCode = self.poco("com.enigma.im:id/handle")
        #:::登录按钮
        self.ele_loginBtn = self.poco("com.enigma.im:id/btn_login_pic")
        #:::登录此账户
        self.ele_loginThis = self.poco("com.enigma.im:id/yes_title")
        #:::取消关联账户
        self.ele_cancelLoginThis = self.poco("com.enigma.im:id/no_title")
        #:::设备丢失
        self.ele_deviceLoss = self.poco("com.enigma.im:id/loss")
        self.ele_confirmLoss = self.poco("com.enigma.im:id/btn_right")
        self.ele_cancelLoss = self.poco("com.enigma.im:id/btn_left")
        #:::两步验证页面
        self.ele_page_doubleverify = self.poco(text="两步验证", name="com.enigma.im:id/tv_toolbar_title")
        self.ele_setDoublePwd = self.poco("com.enigma.im:id/input")
        self.ele_next = self.poco(text="下一步")


    def clear_input(self):
        self.ele_clearInput.click()

    def click_deviceLoss(self):
        self.ele_deviceLoss.click()
        self.ele_confirmLoss.click()

    def set_countryCode(self,code="+355"):
        if not self.ele_code355.exists():
            self.ele_countryCode.click()
            self.ele_setCountryCode.set_text(code)
            self.poco(text=code,name="com.enigma.im:id/code").click()

    def set_loginInfo(self,phone="20000000006",code="666666"):
        self.ele_setPhone.set_text(phone)
        self.ele_sendCode.click()
        self.ele_setAuthCode.set_text(code)

    def doubleAuth(self,text="123"):
        self.ele_setDoublePwd.set_text(text)
        self.ele_next.click()


    def login(self,countryCode="+355",phone="20000000006",authCode="666666",choose="0"):
        #设置国家码
        if not self.ele_code355.exists():
            self.ele_countryCode.click()
            self.ele_setCountryCode.set_text(countryCode)
            self.poco(text=countryCode,name="com.enigma.im:id/code").click()
        #设置登录信息
        self.ele_setPhone.set_text(phone)
        self.ele_sendCode.click()
        self.ele_setAuthCode.set_text(authCode)
        #点击登录
        self.ele_loginBtn.click()
        #是否是自己的账号：：：0-是   1-不是
        if choose == "0":
            self.ele_loginThis.click()
            #设备丢失（强制登录）
            self.ele_deviceLoss.click()
            self.ele_confirmLoss.click()
            if self.ele_page_doubleverify.exists():
                self.ele_setDoublePwd.set_text("123")
                self.ele_next.click()
        elif choose == "1":
            self.ele_cancelLoginThis.click()




if __name__ == "__main__":
    page_login().login()