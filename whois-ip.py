from pprint import pprint
from ipwhois import IPWhois
#read file containing ips
g = open('unique_ips.txt','r')

filename = 'results.txt'
f = open(filename, 'w')

#read lines into array
a = g.readlines()
a = [x.strip('\n') for x in a]

#print(a)
for x in a:
	print(x)
	obj = IPWhois(str(x))
	try:
		results = obj.lookup()
		pprint(results)
	#f.write(str(results))
		print(results['query'])
		f.write('IP: ')
		f.write(results['query'])
		f.write('\n')
		try:
			f.write('Name1: ')
			f.write(results['nets'][0]['name'])
			f.write('\n')
		except:
			f.write('\n')
		try:
			f.write('Description1: ')
			f.write(results['nets'][0]['description'])
			f.write('\n')	
		except:
			f.write('\n')
		try:
			f.write('Country1: ')
			f.write(results['nets'][0]['country'])
			f.write('\n')
		except:
			f.write('\n')
		try:
			f.write('Tech Emails1: ')
			f.write(results['nets'][0]['tech_emails'])
			f.write('\n')
		except:
			f.write('\n')	
		try:
			f.write('Updated1: ')
			f.write(results['nets'][0]['updated'])
			f.write('\n')
		except:
			f.write('\n')
			
		try:
			f.write('Name2: ')
			f.write(results['nets'][1]['name'])
			f.write('\n')
		except:
			f.write('\n')
		try:
			f.write('Description2: ')
			f.write(results['nets'][1]['description'])
			f.write('\n')	
		except:
			f.write('\n')
		try:
			f.write('Country2: ')
			f.write(results['nets'][1]['country'])
			f.write('\n')
		except:
			f.write('\n')
		try:
			f.write('Tech Emails2: ')
			f.write(results['nets'][1]['tech_emails'])
			f.write('\n')
		except:
			f.write('\n')	
		try:
			f.write('Updated2: ')
			f.write(results['nets'][1]['updated'])
			f.write('\n')
		except:
			f.write('\n')
	except:
		f.write('IP: ')
		f.write(results['query'])
		f.write('\n')
		print('LOOKUP FAILED')
		print('\n')
		f.write('LOOKUP FAILED')
		f.write('\n')
	f.write('\n')
	f.write('*************')
	f.write('\n')
	f.write('\n')
		
