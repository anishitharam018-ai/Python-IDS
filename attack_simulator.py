from ids import SimpleIDS
from behavior import BehaviorEngine
import time
import random

ids = SimpleIDS()
beh = BehaviorEngine()

print("=== ATTACK SIMULATOR STARTED ===")


print("\n[Attack] Brute Force Login Attempts...")
for _ in range(6):
    ids.record_failed_login("192.168.1.50")
    time.sleep(0.5)

print("\n[Attack] Port Scanning...")
for port in range(1, 20):
    ids.record_port_access("192.168.1.77", port)
    time.sleep(0.1)


print("\n[Attack] Login from NEW DEVICE")
beh.check_device("UserA", "Hacker_Device_001")


print("\n[Attack] Login from NEW LOCATION")
beh.check_location("UserA", "Russia")

print("\n[Attack] High Traffic Burst...")
for _ in range(20):
    ids.record_request()
    time.sleep(0.05)

print("\n=== ATTACK SIMULATOR FINISHED ===")
