#Michael Frazer
#Network Engineering 2 - Lab 1
#Learning about netmiko for an OSPF lab.
#I am feeling very embarrased about how bad this code is.
#I am looking forward to learning how to make these routers objects. 
#I apologize if you are reading this "code" maybe... don't.

import netmiko, time

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

MF5 = {
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
    ipAddress = subnet[:startFinal + 1] + str(final) + ' 255.255.255.252'

    net_connect = netmiko.ConnectHandler(**device)
    net_connect.enable()
    config_ipv4 = ['int ' + interface, 'ip address ' + ipAddress, 'no shut', 'negotiation auto']
    net_connect.send_config_set(config_ipv4)

    return ipAddress


def assignIPV6(device, subnet, routerNumber, interface):
    slash = subnet.find('/')
    if routerNumber == 0:
    	completeIPV6Address = subnet
    else:    
    	slash = subnet.find('/')
    	completeIPV6Address = subnet[:slash] + str(routerNumber) + subnet[slash:]

    return completeIPV6Address

#This function (like this entire script) is going to be extremely hardcoded due to a lack of time and expirence
def wildCardCalculator(ipAddress):
    space = ipAddress.find(' ')    
    wildCardIP = ipAddress[:space + 1] + '0.0.0.3'

    return wildCardIP

def wcAssigner(routerList):
    temp = []
    for each in routerList:
        temp.append(wildCardCalculator(each))
    return temp

def ospfConfV4(device, ip):
    net_connect = netmiko.ConnectHandler(**device)
    net_connect.enable()
    config_ospf = ['router ospf 1', 'network ' + ip + ' area 0']
    net_connect.send_config_set(config_ospf)

def ospfConfV6(device, ip, interface):
    nenet_connect = netmiko.ConnectHandler(**device)
    net_connect.enable()
    config_ospf = ['ipv6 unicast-routing', 'int ' + interface, 'ospfv3 1 ipv6 area 0']

#The following is the configuration of all the ip addresses to the correct interfaces
#The sleep command is a workaround for my poor coding as telnetting in so rapidly was breaking the connection
#Router MF1 Config
MF1V4G0 = assignIPV4(MF1, ipv4[0], 1, 'g0/0')
time.sleep(1)
MF1V4G1 = assignIPV4(MF1, ipv4[1], 1, 'g1/0')
time.sleep(1)
MF1V6G0 = assignIPV6(MF1, ipv6[0], 0, 'g0/0')
time.sleep(1)
MF1V6G1 = assignIPV6(MF1, ipv6[1], 0, 'g1/0')

#Router MF2 Config
MF2V4G0 = assignIPV4(MF2, ipv4[0], 2, 'g0/0')
time.sleep(1)
MF2V4G1 = assignIPV4(MF2, ipv4[2], 1, 'g1/0')
time.sleep(1)
MF2V6G0 = assignIPV6(MF2, ipv6[0], 1, 'g0/0')
time.sleep(1)
MF2V6G1 = assignIPV6(MF2, ipv6[2], 0, 'g1/0')

#Router MF3 Config
MF3V4G1 = assignIPV4(MF3, ipv4[2], 2, 'g1/0')
time.sleep(1)
MF3V4G2 = assignIPV4(MF3, ipv4[4], 1, 'g2/0')
time.sleep(1)
MF3V6G1 = assignIPV6(MF3, ipv6[2], 1, 'g1/0')
time.sleep(1)
MF3V6G2 = assignIPV6(MF3, ipv6[4], 0, 'g2/0')

#Router MF4 Config
MF4V4G1 = assignIPV4(MF4, ipv4[1], 2, 'g1/0')
time.sleep(1)
MF4V4G0 = assignIPV4(MF4, ipv4[3], 1, 'g0/0')
time.sleep(1)
MF4V6G1 = assignIPV6(MF4, ipv6[1], 1, 'g1/0')
time.sleep(1)
MF4V6G0 = assignIPV6(MF4, ipv6[3], 0, 'g0/0')

#Router MF5 Config
MF5V4G0 = assignIPV4(MF5, ipv4[3], 2, 'g0/0')
time.sleep(1)
MF5V4G2 = assignIPV4(MF5, ipv4[4], 2, 'g2/0')
time.sleep(1)
MF5V6G0 = assignIPV6(MF5, ipv6[3], 1, 'g0/0')
time.sleep(1)
MF5V6G2 = assignIPV6(MF5, ipv6[4], 1, 'g2/0')

ipv4MF1 = [MF1V4G0, MF1V4G1]
ipv4MF2 = [MF2V4G0, MF2V4G1]
ipv4MF3 = [MF3V4G1, MF3V4G2]
ipv4MF4 = [MF4V4G0, MF4V4G1]
ipv4MF5 = [MF5V4G0, MF5V4G2]

ipv6MF1 = [MF1V6G0, MF1V6G1]
ipv6MF2 = [MF2V6G0, MF2V6G1]
ipv6MF3 = [MF3V6G1, MF3V6G2]
ipv6MF4 = [MF4V6G0, MF4V6G1]
ipv6MF5 = [MF5V6G0, MF5V6G2]


wcMF1 = wcAssigner(ipv4MF1)
wcMF2 = wcAssigner(ipv4MF2)
wcMF3 = wcAssigner(ipv4MF3)
wcMF4 = wcAssigner(ipv4MF4)
wcMF5 = wcAssigner(ipv4MF5)

allWCIPs = [wcMF1, wcMF2, wcMF3, wcMF4, wcMF5]
allipv6 = [ipv6MF1, ipv6MF2, ipv6MF3, ipv6MF4, ipv6MF5]

for i in range(len(allWCIPs)):
    router = routers[i]
    for each in allWCIPs[i]:
        ospfConfV4(router, each)
        time.sleep(1)





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
