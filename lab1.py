import netmiko

device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.122.2',
    'port': 23,
    'password': 'password',
    'secret': 'secret'
    }

MF1 = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.122.10',
    'port': 23,
    'password': 'password',
    'secret': 'TELE31831'
    }

MF2 = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.122.20',
    'port': 23,
    'password': 'password',
    'secret': 'TELE31831'
    }

MF3 = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.122.30',
    'port': 23,
    'password': 'password',
    'secret': 'TELE31831'
    }

MF4= {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.122.40',
    'port': 23,
    'password': 'password',
    'secret': 'TELE31831'
    }

MF5= {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.122.50',
    'port': 23,
    'password': 'password',
    'secret': 'TELE31831'
    }

routers = [MF1, MF2, MF3, MF4, MF5]

for each in routers:
    net_connect = netmiko.ConnectHandler(**each)
    output = net_connect.send_command('show ip route')
    print (output)

#List of IPV4 Networks
ipv4 = ['12.81.0.4/30', '12.81.4.8/30', '12.81.7.16/30', '12.81.8.20/30', '12.81.9.24/30']

#List of IPV6 Networks
ipv6 = ['2607:f798:12:81:0:4::/127', '2607:f798:12:81:4:8::/127', '2607:f798:12:81:7:16::/127', '2607:f798:12:81:8:20::/127', '2607:f798:12:81:9:24::/127',]


def assignIPV4(device, subnet, routerNumber, interface):



def assignIPV6(device, subnet, routerNumber, interface):






#net_connect.enable()

#config_commands = ['int g4/0', 'ip address 192.168.2.1 255.255.255.0', 'no shut']
#output = net_connect.send_config_set(config_commands)


#output1 = net_connect.send_command('conf t')
#print (output1)

#output2 = net_connect.send_command('int g1/0')
#print (output2)

#output3 = net_connect.send_command('ip address 192.168.2.1 255.255.255.0')
#print (output3)

#output = net_connect.send_command('show int')
#print (output)
