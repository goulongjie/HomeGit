from function.Page import Page



class page_common(Page):
    def __init__(self):
        Page.__init__(self)

        # 聊天列表界面
        self.icon_chart = self.poco("com.enigma.im:id/nv_menu_session").offspring("com.enigma.im:id/iv_icon")
        self.icon_contacts = self.poco("com.enigma.im:id/nv_menu_contacts ").offspring("com.enigma.im:id/iv_icon")
        self.icon_my = self.poco("com.enigma.im:id/nv_menu_settings").offspring("com.enigma.im:id/iv_icon")


