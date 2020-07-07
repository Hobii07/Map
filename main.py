from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
# from Helpers import username_helper, password_helper
username_helper = """
MDTextField:
    hint_text: "Enter username"
    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
    size_hint_x: None
    width: 300
"""
password_helper = """
MDTextField:
    hint_text: "Enter password"
    helper_text: "forgot password(?)"
    helper_text_mode: "persistent"
    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    size_hint_x: None
    width: 300
"""

class TestApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        # label = MDLabel(text='hello world', halign='center', theme_text_color='Custom',
        #                 text_color=(0, 1, 0, 1),
        #                 font_style='Caption')
        screen = Screen()
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        btn_SignIn = MDRectangleFlatButton(text='Sign In',
                                           pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                           on_release=self.show_data)
        btn_SignUp = MDRectangleFlatButton(text='Sign Up',
                                           pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                           on_release=self.show_data)
        btn_Terms = MDFlatButton(text='Terms and Conditions',
                                 pos_hint={'center_x': 0.5, 'center_y': 0.1})
        screen.add_widget(btn_SignIn)
        screen.add_widget(btn_SignUp)
        screen.add_widget(btn_Terms)
        screen.add_widget(self.username)
        screen.add_widget(self.password)

        # icon_label = MDIcon(icon='language-python', halign='left')
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text + ' does not exist'
        btn_close = MDFlatButton(text='Close', on_release=self.close_dialog)
        btn_more = MDFlatButton(text='More')
        self.dialog = MDDialog(title='Check', text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[btn_close, btn_more])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


TestApp().run()
