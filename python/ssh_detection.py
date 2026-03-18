from collections import defaultdict

LOG_FILE = "/var/log/auth.log"
THRESHOLD = 20

ip_count = defaultdict(int)

with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()

            for i in range(len(parts)):
                if parts[i] == "from" and i + 1 < len(parts):
                    ip = parts[i + 1]
                    ip_count[ip] += 1
                    break

print("=== SSH Brute-Force Detection Results ===")

if not ip_count:
    print("No failed SSH login attempts found.")
else:
    for ip, count in sorted(ip_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip} -> {count} failed attempts")

        if count >= THRESHOLD:
            print(f"ALERT: Possible brute-force attack detected from {ip}")
