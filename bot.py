#!/usr/bin/python 
import urllib2
import urllib
import sys
import time
import random
import re
import os
import string
from sys import platform

proxylisttext = "proxylist.txt" #nama list proxy

useragent = ["Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)",
            "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Googlebot/2.1 (+http://www.google.com/bot.html) Mozilla/5.0 (compatible); Googlebot/2.1; (+http://www.google.com/bot.html) Googlebot-Image/1.0",
            "Googlebot-Video/1.0",
            "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
            "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
            "DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)",
            "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
            "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
            "facebot",
            "facebookexternalhit/1.0 (+http://www.facebook.com/externalhit_uatext.php)",
            "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
            "admantx-sap/2.4 (+http://www.admantx.com/service-fetcher.html)",
            "Twitterbot",
            "facebookexternalhit/1.1;line-poker/1.0",
            "Twitterbot/1.0",
            "Mozilla/5.0 (compatible; Twitterbot/1.0)",
            "Twitterbot/1.0 Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.12.3 Chrome/69.0.3497.128 Safari/537.36",
            "TelegramBot+(like+TwitterBot)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.11.1 Facebot Twitterbot/1.0",
            "NetResearchServer/2.5(loopimprovements.com/robot.html)",
            "facebookexternalhit"]
 
referer = ['http://google.com','http://bing.com','http://facebook.com','http://twitter.com']
link    = 'https://mobile.twitter.com/h4j3s' #input link
 
def Autoclicker(proxy1):
    try:
        proxy = proxy1.split(":")
        print 'Proxy :',proxy1
        proxy_set = urllib2.ProxyHandler({"http" : "%s:%d" % (proxy[0], int(proxy[1]))})
        opener = urllib2.build_opener(proxy_set, urllib2.HTTPHandler)
        opener.addheaders = [('User-agent', random.choice(useragent)),
                                                ('Referer', random.choice(referer))]
        urllib2.install_opener(opener)
        f = urllib2.urlopen(link)
        if "https://mobile.twitter.com/h4j3s" in f.read(): #input link
           print "[X] Link Berhasil Di Kunjungi ..."
        else:
           print "[X] Link gagal di kunjungi !"
           print "[X] Proxy failed"
 
    except:
           print "[X] Running ~ "
           pass
 
def loadproxy():
    try:
        get_file = open(proxylisttext, "r")
        proxylist = get_file.readlines()
        count = 0
        proxy = []
        while count < len(proxylist):
              proxy.append(proxylist[count].strip())
              count += 1
        for i in proxy:
            Autoclicker(i)
    except IOError:
        print "\n[-] Error: Check your proxylist path\n"
        sys.exit(1)
 
def main():
   print """

 /$$   /$$             /$$      /$$$$$$  /$$       /$$$$$$$   /$$$$$$  /$$$$$$$$
| $$$ | $$            | $$     /$$__  $$| $$      | $$__  $$ /$$__  $$|__  $$__/
| $$$$| $$  /$$$$$$  /$$$$$$  | $$  \ $$| $$$$$$$ | $$  \ $$| $$  \ $$   | $$   
| $$ $$ $$ |____  $$|_  $$_/  |  $$$$$$$| $$__  $$| $$$$$$$ | $$  | $$   | $$   
| $$  $$$$  /$$$$$$$  | $$     \____  $$| $$  \ $$| $$__  $$| $$  | $$   | $$   
| $$\  $$$ /$$__  $$  | $$ /$$ /$$  \ $$| $$  | $$| $$  \ $$| $$  | $$   | $$   
| $$ \  $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$  | $$| $$$$$$$/|  $$$$$$/   | $$   
|__/  \__/ \_______/   \___/   \______/ |__/  |__/|_______/  \______/    |__/   
                       Website Visitor w/Proxy
               Created by NathX - Suryanjana | @nat9h                                                                            

"""
   loadproxy()
if __name__ == '__main__':
        main()
