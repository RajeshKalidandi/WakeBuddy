from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDTimePicker  # Updated import
from kivymd.uix.toolbar import MDToolbar  # Added import

import datetime
from time_picker import CustomTimePicker
KV = '''
ScreenManager:
    MainScreen:
    AlarmScreen:

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'WakeBuddy'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["clock", lambda x: app.set_alarm()]]
        MDLabel:
            text: "Welcome to WakeBuddy!"
            halign: "center"
        MDRaisedButton:
            text: "Set Alarm"
            on_release: app.show_time_picker()
        MDLabel:
            id: alarm_time
            text: "No alarm set"
            halign: "center"

<AlarmScreen>:
    name: 'alarm'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Alarm'
            left_action_items: [["arrow-left", lambda x: app.back_to_main()]]
        MDLabel:
            text: "Alarm is ringing!"
            halign: "center"
        MDRaisedButton:
            text: "Stop Alarm"
            on_release: app.stop_alarm()
'''

class MainScreen(Screen):
    pass

class AlarmScreen(Screen):
    pass

class WakeBuddyApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(AlarmScreen(name='alarm'))
        self.alarm_time = None
        return Builder.load_string(KV)

    def navigation_draw(self):
        pass

    def set_alarm(self):
        self.show_time_picker()

    def show_time_picker(self):
        time_picker = CustomTimePicker()
        time_picker.on_save = self.on_save
        time_picker.open()

    def on_save(self, time_str):
        self.alarm_time = datetime.datetime.strptime(time_str, "%H:%M").time()
        self.root.get_screen('main').ids.alarm_time.text = f"Alarm set for {time_str}"
        Clock.schedule_once(self.check_alarm, 1)

    def check_alarm(self, dt):
        if self.alarm_time:
            current_time = datetime.datetime.now().time()
            if current_time >= self.alarm_time:
                self.sm.current = 'alarm'
            else:
                Clock.schedule_once(self.check_alarm, 1)

    def stop_alarm(self):
        self.sm.current = 'main'
        self.root.get_screen('main').ids.alarm_time.text = "No alarm set"
        self.alarm_time = None

    def back_to_main(self):
        self.sm.current = 'main'

if __name__ == '__main__':
    WakeBuddyApp().run()
