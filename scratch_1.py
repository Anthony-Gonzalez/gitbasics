from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.2',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print(output)

config_commands = ['int l0', 'ip add 1.1.1.1 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range (2,21):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN_' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)
    
