import argparse
import whois

def main():
	parser = argparse.ArgumentParser(description='Extract Whois info about domains')
	parser.add_argument('domain', metavar='N', nargs='+', help='Domains for Whois')
	file = open('whois.txt', 'w')
	args = parser.parse_args()

	for domain in args.domain:
 		w = whois.whois(domain)
		max_date = max(w.updated_date)
		pos = w.updated_date.index(max_date)
		print "Dominio: %s" %domain
		file.write("Dominio: %s \n" %domain)
		if(isinstance(w.creation_date, list)):
			c_date = w.creation_date[pos]
		else:
			c_date = w.creation_date
                print "Fecha del registro del dominio: %s" %c_date
                file.write("Fecha del registro del dominio: %s \n" %c_date)
		if(isinstance(w.registrar, list)):
                        res = w.registrar[pos]
                else:
                        res = w.registrar
		print "Registrador: %s" %res
		file.write("Registrador: %s \n" %res)
		if(isinstance(w.expiration_date, list)):
                        e_date = w.expiration_date[pos]
                else:
                        e_date = w.expiration_date
		print "Fecha de expiracion del dominio: %s" %e_date
		file.write("Fecha de expiracion del dominio: %s \n" %e_date)
		if(isinstance(w.org, list)):
                        org = w.org[pos]
                else:
                        org = w.org
		print "Propietario: %s" %org
		file.write("Propietario: %s\n" %org)
		print "----------------------"
		file.write("---------------------- \n")
		print "Whois: "
		file.write("Whois: \n")
		print w.text
		file.write("%s \n" %w.text)
		print ("\n\n")
		file.write("\n\n")
	file.close()


if __name__ == "__main__":
	main()
