import time
from collections import defaultdict

class SimpleIDS:
    def __init__(self):
        
        self.port_hits = defaultdict(list)           
        self.failed_logins = defaultdict(list)       
        self.request_times = []                      

        self.PORT_SCAN_THRESHOLD = 10     
        self.BRUTE_FORCE_THRESHOLD = 5    
        self.TRAFFIC_SPIKE_THRESHOLD = 15 

    # -------- LOGGING FUNCTION --------
    def log_alert(self, message):
        print(message)
        with open("logs/alerts.log", "a", encoding="utf-8") as f:
            f.write(message + "\n")
    # ---------------------------------

    def record_port_access(self, ip, port):
        current_time = time.time()
        self.port_hits[ip].append((port, current_time))

        self.port_hits[ip] = [
            (p, t) for (p, t) in self.port_hits[ip] if current_time - t < 10
        ]

        if len(self.port_hits[ip]) > self.PORT_SCAN_THRESHOLD:
            self.log_alert(f"⚠️ ALERT: Possible Port Scan detected from {ip}!")


    def record_failed_login(self, ip):
        current_time = time.time()
        self.failed_logins[ip].append(current_time)

        self.failed_logins[ip] = [
            t for t in self.failed_logins[ip] if current_time - t < 20
        ]

        if len(self.failed_logins[ip]) > self.BRUTE_FORCE_THRESHOLD:
            self.log_alert(f"⚠️ ALERT: Brute Force Attack detected from {ip}!")


    def record_request(self):
        current_time = time.time()
        self.request_times.append(current_time)

        self.request_times = [
            t for t in self.request_times if current_time - t < 5
        ]

        if len(self.request_times) > self.TRAFFIC_SPIKE_THRESHOLD:
            self.log_alert("⚠️ ALERT: Traffic Spike / DoS-like behavior detected!")


if __name__ == "__main__":
    ids = SimpleIDS()

    print("Running IDS Core Engine Test...")

    for _ in range(6):
        ids.record_failed_login("192.168.1.10")
        time.sleep(1)

    for port in range(1, 15):
        ids.record_port_access("192.168.1.20", port)
        time.sleep(0.3)

    for _ in range(20):
        ids.record_request()
        time.sleep(0.1)
