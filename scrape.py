import requests,os,sys

#Détection de l'OS
if "WINDOWS" in os.environ['SYSTEMROOT']:
    def cls():
        os.system("cls")
else:
    def cls():
        os.system("clear")
cls()
banner = """ 
 ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
||P |||r |||o |||x |||y |||F |||u |||c |||k |||e |||r ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

[+] By LordKynda
\n\n\n
"""
proxy_number = 0
print(banner)

#Choix du type de proxy
proxy_type = input("Proxy Type  ?\n\n[1] SOCKS4\n[2] SOCKS5\n[3] HTTP\n[4] TOUS \n\n[>] ")
if proxy_type == "1":
    proxy_type = "socks4"
elif proxy_type == "2":
    proxy_type = "socks5"
elif proxy_type == "3":
    proxy_type = "http"
elif proxy_type == "4":
    proxy_type = "all"
else:
    cls()
    print(banner)
    sys.exit("Votre choix est incorrect.")


cls()
print(banner)
print("Type de proxy: " + proxy_type+"\n\n")

#Choix du timeout
try:
    proxy_timeout = int(input("Timeout  ?\n\n[>] "))
except:
    cls()
    print(banner)
    sys.exit("Votre choix est incorrect.")

cls()
print(banner)
print("Type de proxy: " + proxy_type)
print("Timeout : " + str(proxy_timeout)+"\n\n")

#Choix de l'anonymat du proxy
proxy_anon = input("Proxy Anonimity  ?\n\n[1] ELITE\n[2] ANONYMOUS\n[3] TRANSPARENT\n[4] TOUS \n\n[>] ")
if proxy_anon == "1":
    proxy_anon = "elite"
elif proxy_anon == "2":
    proxy_anon = "anonymous"
elif proxy_anon == "3":
    proxy_anon = "transparent"
elif proxy_anon == "4":
    proxy_anon = "all"
else:
    cls()
    print(banner)
    sys.exit("Votre choix est incorrect.")

cls()
print(banner)
print("Type de proxy: " + proxy_type)
print("Timeout : " + str(proxy_timeout))
print("Proxy Anonimity : " + proxy_anon+"\n\n")

#URL de l'API avec les choix de l'user
req = "https://api.proxyscrape.com/?request=displayproxies&proxytype="+proxy_type+"&timeout="+str(proxy_timeout)+"&anonymity="+proxy_anon+"&ssl=yes"
#GET l'url
r = requests.get(req)
#Obtenir la liste de tous les proxys
proxies = r.text.split("\n")
#Ouvrir le fichier proxys.txt
file = open("proxys.txt","a")

#Pour chaque proxy
for prox in proxies:
    proxy_number+=1 #+1 proxy 
    file.write(prox) #enregistrer le proxy
file.close() #fermer le fichier
cls()
print(banner)
print("[+] Terminé !\nNombre de proxys trouvés : "+str(proxy_number))