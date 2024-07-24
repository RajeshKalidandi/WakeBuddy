class AlarmManager:
    def __init__(self):
        self.alarms = []

    def set_alarm(self, alarm_time):
        self.alarms.append(alarm_time)
        print(f"Alarm set for {alarm_time}")

    def check_alarms(self, current_time):
        if current_time in self.alarms:
            self.trigger_alarm()

    def trigger_alarm(self):
        print("Alarm! Time to wake up!")
