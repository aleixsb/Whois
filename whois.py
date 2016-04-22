import whois
import argparse

def main():
	parser = argparse.ArgumentParser(description='Extract Whois info about domains')
	parser.add_argument('domain', metavar='N', nargs='+', help='Domains for Whois')
	file = open('whois.txt', 'w')
	args = parser.parse_args()
	#print args
	for domain in args.domain:
		w = whois.whois(domain)
		print "Dominio: %s" %domain
		file.write("Dominio: %s \n" %domain)
		print "Fecha del registro del dominio: %s" %w.creation_date
		file.write("Fecha del registro del dominio: %s \n" %w.creation_date)
		print "Registrador: %s" % w.registrar
		file.write("Registrador: %s \n" % w.registrar)
		print "Fecha de expiracion del dominio: %s" %w.expiration_date
		file.write("Fecha de expiracion del dominio: %s \n" %w.expiration_date)
		print "Propietario: %s" %w.org
		file.write("Propietario: %s\n" %w.org)
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
