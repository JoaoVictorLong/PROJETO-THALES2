#!/usr/bin/python
#-*- coding: utf8 -*-
import os

var=raw_input()

def cabecalho():
        print("content-type: text/html")
        print("")

tipo=var.split("=")[0]
acao=var.split("=")[1]

if tipo == "firewall":
        if acao == "INICIAR":
                os.system("bash /var/www/html/cgi-bin/firewall/iniciar.sh")
                cabecalho()
                print("<h1>Iniciado</h1>")
        elif acao == "PARAR":
                os.system("bash /var/www/html/cgi-bin/firewall/parar.sh")
                cabecalho()
                print("<h1>Parado</h1>")
        elif acao == "REINICIAR":
                os.system("bash /var/www/html/cgi-bin/firewall/reiniciar")
                cabecalho()
                print("<h1>Reiniciado</h1>")

if tipo == "dns":
        if acao == "INICIAR":
                os.system("sudo /usr/lib/cgi-bin/script.sh bind9 start")
                cabecalho()
                print("<h1>Iniciado</h1>")
        elif acao == "PARAR":
                os.system("sudo /usr/lib/cgi-bin/script.sh bind9 stop")
                cabecalho()
                print("<h1>Parado</h1>")
        elif acao == "REINICIAR":
                os.system("sudo /usr/lib/cgi-bin/script.sh bind9 restart")
                cabecalho()
                print("<h1>Reiniciado</h1>")

if tipo == "nagios3":
        if acao == "INICIAR":
                os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 start")
                cabecalho()
                print("<h1>Iniciado</h1>")
        elif acao == "PARAR":
                os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 stop")
                cabecalho()
                print("<h1>Parado</h1>")
        elif acao == "REINICIAR":
                os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 restart")
                cabecalho()
                print("<h1>Reiniciado</h1>")
