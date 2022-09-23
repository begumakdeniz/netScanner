import scapy.all as scapy
import optparse

def getInfo():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ip", dest = "ip", help = "your IP")
    parse_object.add_option("-m", "--mac", dest = "macaddress", help = "your mac address")

    (user_input, arguments) = parse_object.parse_args()

    if not user_input.ip:
        print("Enter IP Address")

    return user_input

def scan_net(ip):
    arp_request = scapy.ARP(pdst = "10.0.2.1/24")
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast/arp_request
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout = 1)

    answered_list.summary()

user_ip_address = getInfo()
scan_net(user_ip_address.ip)