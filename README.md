# SSH Brute-Force Detection Lab (SIEM + Python)
SSH Brute-Force Detection Lab (SIEM + Python)

The Python detection script parsed /var/log/auth.log, identified 192.168.56.102 as the attacking host, and detected 17,407 failed SSH authentication attempts, triggering a brute-force alert.


**Tools & Technologies**

- Kali Linux
- Ubuntu Server
- Hydra
- Python 3
- Splunk Enterprise (SIEM)
- Linux CLI tools (grep, awk)

**Attack Simulation**

Hydra was used to attack the ubuntu server 

Following bash script was used to perform the attack:

hydra -l vboxuser -P /usr/share/wordlists/rockyou.txt ssh://192.168.56.101
