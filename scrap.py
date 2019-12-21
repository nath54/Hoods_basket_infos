# import libraries
import requests
import urllib.request
import time
import io
import os
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from makehtml import *

today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
nfs="save.nath"

cac="\n"
cacc="|"
ccac="@"

txs="1"+cac+"1"+cac+"1"

if not nfs in os.listdir("./"):
    f=open(nfs,'w')
    f.write( txs )
    f.close()

f=open(nfs,'r')
dataload=f.read().strip().split(cac)
f.close()

print("aaaa",dataload)

# 0=u17 1=u13 2=u9
cats=["u17","u13","u9"]

joueurs=[ {
    "Nathan CERISARA":0,
    "Louis COLNAT":0,
    "Pascal ETOUMBI":0,
    "Paul MITSLER":0,
    "Maxime PAULY":0,
    "Louison PDEVIN":0,
    "Leon PERRY":0,
    "Yassine ROUANE":0,
    "Nathan TOMASSONI":0,
    "Adam TROTZIER":0,
    },

          {
              "Antoine ALFONSI":0,
              "Liam CAILLET":0,
              "Paul CERISARA":0,
              "Adil CHERGUI":0,
              "Loham GAILLAT":0,
              "Gabin GROBSHEISER":0,
              "Pierre UNTEREINER":0,
              },
          {
              "":0,
              }
]

rs=[200000002774034,200000002775683,200000002775749]
ds=[200000002848356,200000002851801,200000002851984]
ps=[int(data.strip().split(cacc)[0]) for data in dataload if data!=""]
print(ps)

cat=0

def scrapage():
    print(cat,ps[cat])
    retel=True
    if "page"+str(cat)+".html" in os.listdir():
        retel=True
    
    if retel:
        url="https://resultats.ffbb.com/championnat/rencontres/"+str(hex(rs[cat])[2:])+str(hex(ds[cat])[2:])+str(hex(ps[cat])[2:])+".html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        txt=soup.decode()
        f=io.open("page"+str(cat)+".html","w",encoding="utf-8")
        f.write(txt)
        f.close()
    
    f=io.open("page"+str(cat)+".html","r",encoding="utf-8")
    txt=f.read().lower()
    f.close()
    
    ihoud=txt.find("houdemont")
    itr=txt.rfind("<tr",0,ihoud)
    nbtd=0
    et=itr
    itd=itr
    sec=0
    while itd!=-1 and sec<100:
        itd=txt.find("<td",et,ihoud)
        if itd!=-1:
            nbtd+=1
        et=itd+1
        sec+=1
    print(nbtd)
    print(url)
    if sec>=100: return [cats[cat],"error2"]
    if nbtd==5:
        j=txt.rfind("<td",0,ihoud)
        jj=txt.rfind("<td",0,j)
        jjj=txt.rfind("<td",0,jj)
        g=txt.rfind("<td",0,jjj)
        pcod=txt.find(">",g,jjj)
        pcfd=txt.find("<",pcod,jjj)
        pcoh=txt.find(">",jjj,ihoud)
        pcfh=txt.find("<",pcoh,ihoud)
        gg=txt.rfind("</td",0,ihoud)
        ggg=txt.rfind("</a",0,gg)
        h=txt.rfind(">",0,ggg)
        adv=txt[h+1:ggg]
        lieu="A l'exterieur"
        plan=""
        
    elif nbtd==4:
        j=txt.rfind("<td",0,ihoud)
        jj=txt.rfind("<td",0,j)
        jjj=txt.rfind("<td",0,jj)    
        pcod=txt.find(">",jjj,jj)
        pcfd=txt.find("<",pcod,jj)
        pcoh=txt.find(">",jj,ihoud)
        pcfh=txt.find("<",pcoh,ihoud)
        g=txt.find("<td",ihoud)
        gg=txt.find("</td",g+1)
        ggg=txt.find(">",g+1,gg-1)
        h=txt.find("<a",ggg)
        hh=txt.find(">",h)
        hhh=txt.rfind("<",hh,gg)
        adv=txt[hh+1:hhh]
        lieu="Chez nous"
    else:
        return [cats[cat],"error"]
    
    plan=""
    ip=txt.find("openhere('",ihoud)
    bd=-2
    if ip!=-1:
        bd=txt.find("')",ip)
        if bd!=-1 and ip+10<bd:
            plan=txt[ip+10:bd]
    
    print("plan",plan,ip,bd)
    
    date=txt[pcod+1:pcfd]
    heure=txt[pcoh+1:pcfh]

    #print("date : "+date)
    #print("heure : "+heure)
    
    dd=d1.split("/")
    bd=date.split("/")
    
    jour_sur_ordi=int(dd[2]+dd[1]+dd[0])
    jour_sur_site=int(bd[2]+bd[1]+bd[0])
    
    if jour_sur_ordi>jour_sur_site:
        ps[cat]+=1
        return [cats[cat],"datetoup"]
    
    
    #return "Pour la catégorie "+cats[cat]+", le prochain match est a "+heure+" le "+date+" contre "+adv
    result=[cats[cat],adv,lieu,heure,date,joueurs[cat],ps[cat],plan]
    return result #0=nom categorie 1=l'adversaire 2=le lieu 3=l'heure 4=la date #5=les joueurs de l'équipe 6=le plan
    


for x in range(3):
    result=scrapage()
    sec=0
    while result[1]=="datetoup" and sec<50:
        result=scrapage()
        sec+=1
    make_page(result)
    cat+=1
    print(result)

txs=""
for p in ps:
    txs+=str(p)+cac
txs=txs[:-1]

f=open(nfs,"w")
f.write(txs)
f.close()


