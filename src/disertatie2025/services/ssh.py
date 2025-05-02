from netmiko import ConnectHandler

def push_config(ip, config_text):
    conn = ConnectHandler(ip=ip, device_type="cisco_ios", username="admin", password="admin")
    output = conn.send_config_set(config_text.splitlines())
    conn.disconnect()
    return output

def run_command(ip, command):
    conn = ConnectHandler(ip=ip, device_type="cisco_ios", username="admin", password="admin")
    output = conn.send_command(command)
    conn.disconnect()
    return output
