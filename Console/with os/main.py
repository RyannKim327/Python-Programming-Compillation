import os
from tkinter import messagebox

def set_dns_settings(interface_name, dns_servers):
	command = f"netsh interface ip set dnsservers name=\"{interface_name}\" static {dns_servers[0]} primary"
	
	if os.system(command) == 0:
		command = f"netsh interface ip add DNS name=\"{interface_name}\" {dns_servers[1]} index=2"
	
	return os.system(command)

interface_name = ["Ethernet", "Wi-Fi"]
dns_servers = ["208.67.222.123", "208.67.220.123"] 

result = set_dns_settings(interface_name[0], dns_servers)
if result == 0:
    messagebox.showinfo("", f"DNS settings updated for interface: {interface_name[0]}")
else:
	messagebox.showerror("", f"[{interface_name[0]}]Failed to update DNS settings.")

result = set_dns_settings(interface_name[1], dns_servers)
if result == 0:
    messagebox.showinfo("", f"DNS settings updated for interface: {interface_name[1]}")
else:
	messagebox.showerror("", f"[{interface_name[1]}]Failed to update DNS settings.")
