from function.Page import Page


class chat_Window(Page):
    def __init__(self):
        Page.__init__(self)
        # 会话窗口界面
        self.last_msg = self.poco("com.enigma.im:id/rv_chat").child("android.view.ViewGroup$MarginLayoutParams")[0].offspring("com.enigma.im:id/fl_message_content")
        self.input_box = self.poco("com.enigma.im:id/text")
        self.into_details = self.poco("com.enigma.im:id/fl_header")