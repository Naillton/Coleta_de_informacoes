import dns.query
import dns.zone
import dns.resolver
dominio = raw_input("Digite o dominio do site: ")
regNS = dns.resolver.query(dominio, "NS")
lista = []
for registro in regNS:
	lista.append( str(registro) )
for registro in lista:
	try:
		transferZona = dns.zone.from_xfr(dns.query.xfr(registro, dominio))
	except:
		print "Erro na transferencia"
	else:
regDNS = transferZona.nodes.keys()
regDNS.sort()
for n in regDNS:
	print transferZona[n].to_text(n)
