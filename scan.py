#!/usr/bin/env python
# WebPwn3r Bir Web Sitesi Güvenlik Tarayıcısıdır
# By BinGoB3y - twitter.com/BinGoB3y
import re
import urllib
from headers import *
from vulnz import *

print ga.green+'''
	    __          __  _     _____                 ____       
	    \ \        / / | |   |  __ \               |___ \      
	     \ \  /\  / /__| |__ | |__) |_      ___ __   __) |_ __ 
	      \ \/  \/ / _ \ '_ \|  ___/\ \ /\ / / '_ \ |__ <| '__|
 	       \  /\  /  __/ |_) | |     \ V  V /| | | |___) | |   
 	        \/  \/ \___|_.__/|_|      \_/\_/ |_| |_|____/|_|   
                                                    
        ##############################################################
        #| "WebPwn3r" Bir Web Sitesi Güvenlik Tarayıcısıdır          #
        #|  By BinGoB3y - @realarchemist                             #
        #|  Bu Sürüm Destekler; Remote Code/Command Execution, XSS   #
        #|  Ve SQL Injection.                                        #
	#|  Taramak İçin Girilecek Url Örneği:                       #
	#|  http://www.sec-down.com/wordpress/?p=373                 # 
        ##############################################################
        '''+ga.end

def urls_or_list():
	url_or_list = raw_input(" [!] URL veya URL Listesi Taransın mı? [1/2]: ")
	if url_or_list == "1":
	 	 url = raw_input(" [!] URL Giriniz : ")
		 #if not url.startswith("http://"):
		     #Thanks to Nu11 for the HTTP checker
                     #print ga.red+'''\n Hatalır URL, Lütfen URL'nin Şununla Başladığından Emin Olun \"http://\" \n'''+ga.end
                     #exit()
		 if "?" in url:
		 	rce_func(url)
		 	xss_func(url)
		 	error_based_sqli_func(url)
		 else:
			print ga.red +"\n [Uyarı] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" geçerli bir URL değil"+ga.end			
			print ga.red +" [Uyarı] Tam bir UR yazmalısınız .e.g http://site.com/page.php?id=value \n"+ ga.end
			exit()
	if url_or_list =="2":
		 urls_list = raw_input( ga.green+" [!] Enter the list file name .e.g [list.txt]: "+ga.end)
		 open_list = open(urls_list).readlines()
		 for line in open_list:
			 if "?" in line:
			 	links = line.strip()
		  	 	url = links
		  	 	print ga.green+" \n [!] Now Scanning %s"%url +ga.end
		  	 	rce_func(url)
			 	xss_func(url)
			 	error_based_sqli_func(url)
			 else:
			 	links = line.strip()
		  	 	url = links
				print ga.red +"\n [Uyarı] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" geçerli bir URL değil"+ga.end				
				print ga.red +" [Uyarı] Tam bir UR yazmalısınız .e.g http://site.com/page.php?id=value \n"+ ga.end
		 exit()				

urls_or_list()


