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

#List of IPV4 Networks
ipv4 = ['12.81.0.4/30', '12.81.4.8/30', '12.81.7.16/30', '12.81.8.20/30', '12.81.9.24/30']

#List of IPV6 Networks
ipv6 = ['2607:f798:12:81:0:4::/127', '2607:f798:12:81:4:8::/127', '2607:f798:12:81:7:16::/127', '2607:f798:12:81:8:20::/127', '2607:f798:12:81:9:24::/127',]


def assignIPV4(device, subnet, routerNumber, interface):
    dot = subnet.find('.')
    startFinal = subnet.find('.', dot + 4)
    endFinal = subnet.find('/')
    
    final = int(subnet[startFinal + 1:endFinal]) + routerNumber
    ipAddress = subnet[:startFinal + 1] + str(final) + ' 255.255.255.0'

    net_connect = netmiko.ConnectHandler(**device)
    net_connect.enable()
    config_ipv4 = ['int ' + interface, 'ip address ' + ipAddress]
    net_connect.send_config_set(config_ipv4)


def assignIPV6(device, subnet, routerNumber, interface):
    colon = subnet.find(':')
    endFinal = 


#Router MF1 Config
assignIPV4(MF1, ipv4[0], 1, g0/0)
assignIPV4(MF1, ipv4[1], 1, g1/0)

#Router MF2 Config
assignIPV4(MF2, ipv4[0], 2, g0/0)
assignIPV4(MF2, ipv4[2], 1, g1/0)

#Router MF3 Config
assignIPV4(MF3, ipv4[2], 2, g1/0)
assignIPV4(MF3, ipv4[4], 1, g2/0)

#Router MF4 Config
assignIPV4(MF4, ipv4[1], 2, g1/0)
assignIPV4(MF4, ipv4[3], 1, g0/0)

#Router MF5 Config
assignIPV4(MF5, ipv4[3], 2, g0/0)
assignIPV4(MF5, ipv4[4], 2, g2/0)


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
