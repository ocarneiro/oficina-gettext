#!/usr/bin/python3
# *- coding: utf-8 -*

import gettext

_ = gettext.gettext  # lembre-se de usar pygettext3

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
# copie-o para a pasta /usr/share/locale/pt/LC_MESSAGES/
