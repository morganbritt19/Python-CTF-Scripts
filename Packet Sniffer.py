# This is a basic implementation of a packet sniffer using Scapy
# It will output simple information regarding captured packets like src/dst IPs and protocol

import scapy.all as scapy

def packet_callback(packet):
    # Process the packet and print relevant information
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        print(f"Packet: {ip_src} -> {ip_dst}, Protocol: {protocol}")

if __name__ == "__main__":
    # Set the network interface to sniff on (replace 'eth0' with your interface)
    interface = 'eth0'

    try:
        # Start sniffing packets on the specified interface
        scapy.sniff(iface=interface, store=False, prn=packet_callback)
    except KeyboardInterrupt:
        print("\nPacket sniffing stopped.")
