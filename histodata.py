import requests
import urllib3
import sys
urllib3.disable_warnings()

try:
	target_x = sys.argv[1]
	api_key = sys.argv[2]

	url = 'https://api.securitytrails.com/v1/history/' + target_x + '/dns/a'
	headers = {'APIKEY': f'{api_key}', 'accept': 'application/json'}

	resp = requests.get(url=url, headers = headers)


	ip_list = []
	new_l = resp.json()['records']

	for item in range(len(new_l)):
		new_l2 = new_l[item]['values']
		for stuff in range(len(new_l2)):
			if new_l2[stuff]['ip'] not in ip_list:
				ip_list.append(new_l2[stuff]['ip'])

	for i in range(len(ip_list)):
		print(ip_list[i])
		
except IndexError:
	print('Usage: python3 histodata.py <domain> <securitytrails API key>')
