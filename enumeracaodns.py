import socket
dominio = input("Digite o dominio do site: ")
with open("enumname.txt")as arquivo:
	nomes = arquivo.readlines()
for nome in nomes:
	DNS = nome.strip("\n")+ "." + dominio
	try:
		print (DNS + ": " + socket.gethostbyname(DNS))
	except socket.gaierror:
		pass
