#!/usr/bin/python3
# *- coding: utf-8 -*

import gettext

tradutor = gettext.translation('ola', localedir='locale')
tradutor.install()
_ = tradutor.gettext

mensagem_ola = _("Ola, Mundo!")
mensagem_tchau = _("Obrigado por todos os peixes!")

print(mensagem_ola)
print(mensagem_tchau)

# após gerar este arquivo, execute:
# $ pygettext3 nome_arquivo.py
# será gerado um arquivo messages.pot
# copie-o para messages.po
# edite a mensagem traduzida msgstr
# execute msgfmt messages
# será gerado um arquivo messages.mo
# copie-o para a pasta ./locale/pt/LC_MESSAGES/
