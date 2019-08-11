#!/usr/bin/env python  这一行Linux上才需要
# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 下午10:23
# @Author  : Archerx
# @Site    : https://blog.ixuchao.cn
# @File    : tasks.py


import nmap

def namp_port_scan(ip_addr, resp):
    scanner = nmap.PortScanner()
    # 1)SYN ACK Scan == syn
    # 2)UDP Scan  == udp
    # 3)Comprehensive Scan == com
    if resp == 'syn_normal':
        scanner.scan(ip_addr, '22,80,443,3306,9711', '-v -sS -Pn -sV')
        print(scanner[ip_addr]['tcp'])
        print("Ip Status: ", scanner[ip_addr]['status'])
    if resp == 'syn':
        # print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sS')
        # print(scanner.scaninfo())
        # print(scanner[ip_addr])
        print(scanner[ip_addr]['tcp'])
        print("Ip Status: ", scanner[ip_addr]['status'])
        # print(scanner[ip_addr].all_protocols())
        # print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    elif resp == 'udp':
        scanner.scan(ip_addr, '1-1024', '-v -sU')
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    elif resp == 'com':
        scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    else:
        pass


if __name__ == '__main__':
    namp_port_scan('123.207.155.221', 'syn_normal')