import dns.resolver
dominio = raw_input("Digite o dominio do site: ")
with open("enumname.txt") as arquivo:
	nomes = arquivo.readlines()
for nome in nomes:
	resposta = dns.resolver.query(dominio, registro, raise_on_no_answer=false)
	if resposta.rrset is not None:
		print resposta.rrset
