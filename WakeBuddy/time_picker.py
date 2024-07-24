from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivymd.uix.dialog import MDDialog
from kivy.uix.label import Label
from kivymd.uix.button import MDFabButton  # Updated import

# ... rest of your code ...

class CustomTimePicker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.hour_spinner = Spinner(values=[str(i).zfill(2) for i in range(24)], size_hint_y=None, height=44)
        self.minute_spinner = Spinner(values=[str(i).zfill(2) for i in range(60)], size_hint_y=None, height=44)
        
        self.add_widget(Label(text='Hour'))
        self.add_widget(self.hour_spinner)
        self.add_widget(Label(text='Minute'))
        self.add_widget(self.minute_spinner)
        
        self.buttons_layout = BoxLayout(size_hint_y=None, height=50)
        self.save_button = MDFabButton(text='Save', on_release=self.save)
        self.cancel_button = MDFabButton(text='Cancel', on_release=self.cancel)
        
        self.buttons_layout.add_widget(self.save_button)
        self.buttons_layout.add_widget(self.cancel_button)
        
        self.add_widget(self.buttons_layout)
        
    def save(self, instance):
        hour = self.hour_spinner.text
        minute = self.minute_spinner.text
        time_str = f"{hour}:{minute}"
        self.dialog.dismiss()
        self.on_save(time_str)
        
    def cancel(self, instance):
        self.dialog.dismiss()
    
    def on_save(self, time_str):
        pass
        
    def open(self):
        self.dialog = MDDialog(title="Select Time", type="custom", content_cls=self)
        self.dialog.open()
