#!/usr/bin/python3
# *- coding: utf-8 -*

traduções = {
           "Olá, Mundo!":"Hello, World!",
           "Obrigado por todos os peixes!":"42" 
         } 

def traduzir(mensagem):
    return traduções[mensagem]

mensagem_ola = "Olá, Mundo!"
mensagem_tchau = "Obrigado por todos os peixes!"

_ = traduzir  # sim, a variável é o sinal de sublinhado
tradução_ola = _(mensagem_ola)
tradução_tchau = _(mensagem_tchau)

print(tradução_ola)
print(tradução_tchau)
