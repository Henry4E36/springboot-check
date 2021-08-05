#By TeamsSix
#Blog: www.teamssix.com
import requests, sys
requests.packages.urllib3.disable_warnings()


def springboot_check():
	f = open('dir_springboot.txt')
	dir_list = f.readlines()
	f.close()
	for i in dir_list:
		if i != '':
			i = i.replace('\n','')
			url_new = url+i
			if i == '/shutdown':
				try:
					r = requests.post(url_new,headers=headers,verify=False,timeout=7)
					springboot_print(r,i)
				except KeyboardInterrupt:
					sys.exit()
				except:
					pass
			else:
				try:
					r = requests.get(url_new,headers=headers,verify=False,timeout=7)
					springboot_print(r,i)
				except KeyboardInterrupt:
					sys.exit()
				except:
					pass


def springboot_check_cookie():
	f = open('dir_springboot.txt')
	dir_list = f.readlines()
	f.close()
	for i in dir_list:
		if i != '':
			i = i.replace('\n','')
			url_new = url+i
			if i == '/shutdown':
				try:
					r = requests.post(url_new,headers=headers,verify=False,cookies=cookie,timeout=7)
					springboot_print(r,i)
				except KeyboardInterrupt:
					sys.exit()
				except:
					pass
			else:
				try:
					r = requests.get(url_new,headers=headers,verify=False,cookies=cookie,timeout=7)
					springboot_print(r,i)
				except KeyboardInterrupt:
					sys.exit()
				except:
					pass

def springboot_print(r,i):
	r_status = r.status_code
	if r_status == 200:
		print('{} {} {}'.format(r_status,len(r.text),i,))
	else:
		print('{} {}'.format(r_status,i))


if __name__ == '__main__':
	cookie = '20200416090640'
	try:
		url = sys.argv[1]
	except:
		print('''
python3 springboot_check.py url
python3 springboot_check.py url cookie

cookie format: {'parameter1':'value1','parameter2':'value2'}
			''')
		sys.exit()
	try:
		cookie = sys.argv[2]
	except:
		cookie = '20200416090640'
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
	if cookie == '20200416090640':
		springboot_check()
	else:
		springboot_check_cookie()
