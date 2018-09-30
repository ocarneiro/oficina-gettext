#!/usr/bin/python3
# *- coding: utf-8 -*

import gettext

# tradutor = gettext.translation('', localedir='locale')
# tradutor.install()
# traduzir = tradutor.gettext
_ = gettext.gettext

mensagem_ola = _("Olá, Mundo!")
mensagem_tchau = _("Obrigado por todos os peixes!")

print(mensagem_ola)
print(mensagem_tchau)
