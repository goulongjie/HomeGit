from function.page_common import page_common


class page_my(page_common):
    def __init__(self):
        page_common.__init__(self)

        # 我的界面
        self.ele_myInfo = self.poco("com.enigma.im:id/user_item").offspring("android.widget.LinearLayout")
        self.ele_logoutBtn = self.poco("com.enigma.im:id/btn_logout")
        self.ele_confirmLogout = self.poco("com.enigma.im:id/btn_right")


