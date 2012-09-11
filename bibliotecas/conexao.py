# coding: utf-8

import paramiko

# Classe de conexão com SSH
class Conexao:
	endereco=None
	porta=None

	def setHost( self, endereco ):
		self.endereco = endereco

	def getHost( self ):
		return self.endereco

	def setPorta( self, porta ):
		self.porta = porta

	def getPorta( self ):
		return self.porta
		
	# Verifica o login, se conecta ou não.
	def verificarLogin( self, usuario, senha ):
		try:
			ssh = paramiko.SSHClient()
			ssh.load_system_host_keys()
			ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
			ssh.connect( self.getHost(), self.getPorta(), usuario, senha, look_for_keys=False )
			return True
		except:
			return False

