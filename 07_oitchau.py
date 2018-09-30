#!/usr/bin/python3
# *- coding: utf-8 -*

def traduzir(mensagem):
    return mensagem + " ;)"

mensagem_ola = "Olá, Mundo!"
mensagem_tchau = "Obrigado por todos os peixes!"

tradução_ola = traduzir(mensagem_ola)
tradução_tchau = traduzir(mensagem_tchau)

print(tradução_ola)
print(tradução_tchau)
