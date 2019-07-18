from netmiko import ConnectHandler

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.12',
    'username': 'cisco',
    'password': 'cisco'
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.13',
    'username': 'cisco',
    'password': 'cisco'
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.14',
    'username': 'cisco',
    'password': 'cisco'
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.15',
    'username': 'cisco',
    'password': 'cisco'
}

all_devices = [iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
        print("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN_' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
