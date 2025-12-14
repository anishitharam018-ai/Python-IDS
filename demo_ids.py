from ids import SimpleIDS
from behavior import BehaviorEngine
import time

ids = SimpleIDS()
beh = BehaviorEngine()

print("=== IDS Demo Starting ===")

users = [
    {"user":"UserA", "device":"Device_X", "location":"India"},
    {"user":"UserA", "device":"Device_Y", "location":"USA"},   # triggers new device + location alert
]

for u in users:
    beh.check_device(u["user"], u["device"])
    beh.check_location(u["user"], u["location"])
    ids.record_failed_login("192.168.1.10")  # failed login
    time.sleep(1)

for port in range(1, 12):
    ids.record_port_access("192.168.1.20", port)
    time.sleep(0.2)

for _ in range(18):
    ids.record_request()
    time.sleep(0.1)

print("=== IDS Demo Completed ===")
