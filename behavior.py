class BehaviorEngine:
    def __init__(self):
        
        self.known_devices = set()
        self.last_location = None

    # -------- LOGGING FUNCTION --------
    def log_alert(self, message):
        print(message)
        with open("logs/alerts.log", "a", encoding="utf-8") as f:
            f.write(message + "\n")
    # ---------------------------------

    def check_device(self, user, device_id):
        if device_id not in self.known_devices:
            self.log_alert(
                f"⚠️ ALERT: New Device Detected for {user}! Device = {device_id}"
            )
            self.known_devices.add(device_id)

    def check_location(self, user, location):
        if self.last_location is None:
            self.last_location = location
            return

        if location != self.last_location:
            self.log_alert(
                f"⚠️ ALERT: Location Change Detected for {user}! From {self.last_location} → {location}"
            )
            self.last_location = location


if __name__ == "__main__":
    beh = BehaviorEngine()

    print("Testing Behavior Engine...")

    beh.check_device("UserA", "Device_X")
    beh.check_device("UserA", "Device_Y")  # new device alert

    beh.check_location("UserA", "India")
    beh.check_location("UserA", "USA")     # location change alert
