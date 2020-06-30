import socket
usuarios = ["root", "anonymous", "teste"]
for usuario in usuarios:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("ip do servidor smtp",25))
	sock.recv(1024)
	sock.send("VRFY" + usuario + "\n")
	resposta = sock.recv(1024)
	sock.close()
	if "252" in resposta:
		print usuario + "-> Válido!"
	elif "550" in resposta:
		print usuario + "-> Usuário não encontrado"
	elif "503" in resposta:
		print "Servidor requer autenticação"
		break
	elif "500" in reposta:
		print "Comando VRFY não suportado pelo servidor"
		break
	else
		print "Resposta do servidor:" , resposta
