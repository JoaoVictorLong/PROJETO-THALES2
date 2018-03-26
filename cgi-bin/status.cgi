#!/usr/bin/python
import os

var=raw_input()

status=var.split("=")[0]
print("content-type: text/html")
print("")

if status == "firewall":
        print("<h1>Status do Firewall...</h1>")
        print("<textarea rows='100' cols='100'>")
        os.system("iptables -L -v > firewall.tmp")
        a=open("firewall.tmp", "r")
        aberto=a.read()
        a.close
        print(aberto)

if status == "dns":
        print("<h1>Status do DNS...</h1>")
        print("<textarea rows='100' cols='100'>")
        os.system("systemctl status bind9 > dns.tmp")
        a=open("dns.tmp", "r")
        aberto=a.read()
        a.close
        print(aberto)

if status == "nagios3":
        print("<h1>Status do Nagios3...</h1>")
        print("<textarea rows='100' cols='100'>")
        os.system("systemctl status nagios3 > nagios3.tmp")
        a=open("nagios3.tmp", "r")
        aberto=a.read()
        a.close
        print(aberto)
if status == "todos":
        print("<h1>Todos os processos...</h1>")
        print("<textarea rows='100' cols='100'>")
        os.system("ps -aux > todos.tmp")
        a=open("todos.tmp", "r")
        aberto=a.read()
        a.close
        print(aberto)

