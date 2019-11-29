# import libraries
#import requests
import urllib.request
import time
import io
import os
#from bs4 import BeautifulSoup
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

txs="1"+cac
txs+="1"+cac
txs+="1"

if not nfs in os.listdir("./") or True:
    f=open(nfs,'w')
    f.write( txs )
    f.close()

f=open(nfs,'r')
dataload=f.read().split(cac)
f.close()

# 0=u17 1=u13 2=u9
cats=["u17","u13","u9"]
joueurs=[ {"Nathan T":0,"Leon":0,"Adam":0,"Pierre":0,"Louison":9,"Maxime":0,"Nathan C":0,"Paul":0,"Yassine":0,"Louis":0,"Pascal":0},
                  [{"Paul":0}],
                  [{"Leo":0}]
]
rs=[200000002774034,200000002775683,200000002775749]
ds=[200000002848356,200000002851801,200000002851984]
ps=[int(data.split(cacc)[0]) for data in dataload]
print(ps)

cat=0

def scrapage():
    """
    url="https://resultats.ffbb.com/championnat/rencontres/"+str(hex(rs[cat])[2:])+str(hex(ds[cat])[2:])+str(hex(ps[cat])[2:])+".html"
    #print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    txt=soup.decode()
    
    f=io.open("page.html","w",encoding="utf-8")
    f.write(txt)
    f.close()
    """
    
    f=io.open("page.html","r",encoding="utf-8")
    txt=f.read().lower()
    f.close()
    
    ihoud=txt.find("houdemont")
    itr=txt.rfind("<tr",0,ihoud)
    nbtd=0
    et=itr
    itd=itr
    while itd!=-1:
        itd=txt.find("<td",et,ihoud)
        if itd!=-1:
            nbtd+=1
        et=itd+1
    #print(nbtd)
    if nbtd==5:
        j=txt.rfind("<td",0,ihoud)
        jj=txt.rfind("<td",0,j)
        jjj=txt.rfind("<td",0,jj)
        g=txt.rfind("<td",0,jjj)
        pcod=txt.find(">",g,jjj)
        pcfd=txt.find("<",pcod,jjj)
        pcoh=txt.find(">",jjj,ihoud)
        pcfh=txt.find("<",pcoh,ihoud)
        lieu="A l'exterieur"
        adv="Exterieur"
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
        return "error"

    date=txt[pcod+1:pcfd]
    heure=txt[pcoh+1:pcfh]

    #print("date : "+date)
    #print("heure : "+heure)
    
    dd=d1.split("/")
    bd=date.split("/")
    
    if int(dd[2])>int(bd[2]):
        ps[cat]+=1
        return "datetoup"
    elif int(dd[1])>int(bd[1]):
        ps[cat]+=1
        return "datetoup"
    elif int(dd[0])>int(bd[0]):
        ps[cat]+=1
        return "datetoup"
    
    
    #return "Pour la catégorie "+cats[cat]+", le prochain match est a "+heure+" le "+date+" contre "+adv
    return [cats[cat],adv,lieu,heure,date] #0=nom categorie 1=l'adversaire 2=le lieu 3=l'heure 4=la date
    


for x in range(3):
    result=scrapage()
    while result=="datetoup":
        result=scrapage()
        make_page(result)
    cat+=1
    print(result)



