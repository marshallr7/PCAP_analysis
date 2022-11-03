from scapy.all import *
from scapy.layers.inet import TCP

import const

DEBUG = 0

total_tcp_info = []  # [[8080, 127.0.0.1, 8081, 127.0.0.2], [9090, 128.0.0.1, 9091, 128.0.0.2]]


def store_packet_info(packet_list: list, source_port: int, source_ip: str, destination_port: int, destination_ip: str):
    packet_list.append([source_port, source_ip, destination_port, destination_ip])


def print_packet(source_port: int, source_ip: str, destination_port: int, destination_ip: str):
    print(f"Source IP:\n"
          f"\t{source_ip}:{source_port}\n"
          f"Destination IP:\n"
          f"\t{destination_ip}:{destination_port}\n")


def print_packets(packet_list: list):
    [print_packet(packet[0], packet[1], packet[2], packet[3]) for packet in packet_list]


def parse_file(packet_storage: list, packet_file: str):
    for packet in rdpcap(packet_file):
        if packet.haslayer(TCP):
            store_packet_info(packet_storage, packet["Ether"]["TCP"].sport, packet["Ether"]["IP"].src,
                              packet["Ether"]["TCP"].dport, packet["Ether"]["IP"].dst)


def get_tcp_flow_from_sender(packet_storage: list, sender: str):
    # TCP flow is identified by a port, IP, destination port, destination IP
    tcp_from_sender = 0
    for packet in packet_storage:
        if packet[1] == sender:
            tcp_from_sender += 1
    return tcp_from_sender


def get_total_tcp_flow(packet_storage: list):
    return len(packet_storage)


if __name__ == "__main__":
    parse_file(total_tcp_info, const.FILE)
    if DEBUG:
        print_packets(total_tcp_info)
    print(f"Total amount of TCP Flow connections: {get_total_tcp_flow(total_tcp_info)}")
    print(f"Total number of TCP Flow connections from sender ({const.SENDER}): "
          f"{get_tcp_flow_from_sender(total_tcp_info, const.SENDER)}")
