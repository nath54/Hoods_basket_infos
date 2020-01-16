# coding:utf-8

#IMPORTATIONS DES LIBRAIRIES
import requests
import urllib.request
import time
import io
import os
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from makehtml import *

########################################### - INITIALISATION DES VARIABLES - ###########################################
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
nfs="save.nath"

dir_pages="downloaded_pages/"

cac="\n"
cacc="|"
ccac="@"

txs="1"+cac+"1"+cac+"1"

if not nfs in os.listdir("./"):
    f=open(nfs,'w')
    f.write( txs )
    f.close()

if not dir_pages[:-1] in os.listdir("./"):
    os.mkdir(dir_pages)

f=open(nfs,'r')
dataload=f.read().strip().split(cac)
f.close()

#print("aaaa",dataload)

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

#https://resultats.ffbb.com/championnat/b5e6211ed412.html?r=200000002779163&d=200000002859412&p=1
rs=[200000002779163,200000002775683,200000002775749]
ds=[200000002859412,200000002851801,200000002851984]
ps=[int(data.strip().split(cacc)[0]) for data in dataload if data!=""]
maxdays=[int(data.strip().split(cacc)[0]) for data in dataload if data!=""]
pg=["","",""]
print(ps)

cat=0

########################################### - FONCTIONS - ###########################################

def get_scrap_name(cat,day):
	return "https://resultats.ffbb.com/championnat/rencontres/"+str(hex(rs[cats.index(cat)])[2:])+str(hex(ds[cats.index(cat)])[2:])+str(hex(day)[2:])+".html"
    

def get_name_page(cat,day): return "page-"+str(cat)+"-"+str(day)+".html"

def verif_days():
    for cat in cats:
        for d in range(10):
            scrap_page(cat,d)

def get_info_pages(cat,day):
    #ON OUVRE LA PAGE
    infos={"titre":None,"etat":"none","categorie":cat,"day":day,"adversaire":"adversaire inconnu","lieu":"lieu inconnu","date":"date inconnue","heure":"heure inconnue","plan":"plan inconnu","site":"pas de lien"}
    
    name=get_name_page(cat,day)
    if name in os.listdir(dir_pages):
        f=io.open(dir_pages+name,"r",encoding="utf-8")
        txt=f.read().lower()
        f.close()
    else:
        infos["etat"]="pas match"
        return infos
    
    
    #ON CHERCHE LE TITRE :
    it1=txt.find("<title>")
    if it1>=0:
        it2=txt.find("</title>",it1)
        
        if it2>=it1: infos["titre"]=txt[it1+7:it2]
            
    #print("titre :",infos["titre"])
    
    #SI LA PAGE A ETE TROUVEE :
    if infos["titre"]!=None or infos["titre"]!="404 Not Found":
        ihoud=txt.find("houdemont")
        itr=txt.rfind("<tr",0,ihoud)
        nbtd=0
        et=itr
        itd=itr
        sec=0 #securite
        #print(txt[et:ihoud])
        while itd!=-1 and sec<100:
            itd=txt.find("<td",et,ihoud)
            if itd!=-1:
                nbtd+=1
            et=itd+1
            sec+=1
        #print("nbtd",nbtd)
        if sec>=100:
            infos["etat"]="error2"
            return infos
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
            lieu="Chez l'adversaire"
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
            infos["etat"]="error"
            return infos
        plan=""
        ip=txt.find("openhere('",ihoud)
        bd=-2
        if ip!=-1:
            bd=txt.find("')",ip)
            if bd!=-1 and ip+10<bd:
                plan=txt[ip+10:bd]
        #print("plan",plan,ip,bd)
        date=txt[pcod+1:pcfd]
        heure=txt[pcoh+1:pcfh]
        dd=d1.split("/")
        bd=date.split("/")
        jour_sur_ordi=int(dd[2]+dd[1]+dd[0])
        jour_sur_site=int(bd[2]+bd[1]+bd[0])
        
        infos["adversaire"]=adv
        infos["lieu"]=lieu
        infos["date"]=date
        infos["heure"]=heure
        infos["plan"]=plan
        infos["etat"]="good"
        
        #print("debugdate",jour_sur_ordi,jour_sur_site,cat,day) 
        if jour_sur_ordi>jour_sur_site:
            ps[cats.index(cat)]+=1
            infos["etat"]="datetoup"
            return infos
    else:
        infos["etat"]="not found"
    return infos
    
def scrap_page(cat,day):
    url=get_scrap_page(cat,day)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    txt=soup.decode()
    f=io.open(dir_pages+get_name_page(cat,day),"w",encoding="utf-8")
    f.write(txt)
    f.close()
    print("page scrapée ",cat,day)

def an_page(cat):
    day=ps[cats.index(cat)]
    print("Catégorie : ",cat," journée : ",ps[cats.index(cat)])
    retel=False
    if get_name_page(cat,ps[cats.index(cat)]) in os.listdir(dir_pages):
        retel=False
    if retel:
        scrap_page(cat,ps[cats.index(cat)])
    
    
    infos_page=get_info_pages(cat,day)
    categorie=infos_page["categorie"]
    adversaire=infos_page["adversaire"]
    lieu=infos_page["lieu"]
    heure=infos_page["heure"]
    date=infos_page["date"]
    plan=infos_page["plan"]
    jrs=joueurs[cats.index(cat)]
    day=ps[cats.index(cat)]
    lien=get_scrap_name(cat,day)
    
    etat=infos_page["etat"]
    if etat=="error": return [categorie,"error"]
    elif etat=="error2": return [categorie,"error2"]
    elif etat=="datetoup": return [categorie,"datetoup"]
    elif etat=="not found": return [categorie,"not found"]
    elif etat=="pas match": return [categorie,"pas match"]
    
    #return "Pour la catégorie "+cats[cat]+", le prochain match est a "+heure+" le "+date+" contre "+adv
    #result=[cats[cat],adv,lieu,heure,date,joueurs[cat],ps[cat],plan]
    result=[categorie,adversaire,lieu,heure,date,jrs,day,plan,lien]
    return result #0=nom categorie 1=l'adversaire 2=le lieu 3=l'heure 4=la date #5=les joueurs de l'équipe 6=le plan #7=le site off

def scrap_all_pages_of_cat(cat):
    sec=0
    etat=""
    day=1
    #print("\ncat : ",cat)
    while etat!="404 not found" and sec<50:
        scrap_page(cat,day)
        infos=get_info_pages(cat,day)
        etat=infos["titre"]
        day+=1
        sec+=1
        print("aaaa",etat,sec)
        #print("infos : ",infos," day : ",day)
    day-=1
    #print("cat : ",cat," day max : ",day," sec : ",sec)

def todt(dt):
	d=dt.split("/")
	return int(d[2]+d[1]+d[0])

def scrap_all():
    for cat in cats:
        scrap_all_pages_of_cat(cat)

def get_all_dates_cat(cat):
    ad=todt(d1)
    dts={}
    fs=os.listdir(dir_pages)
    for f in fs:
        print(f)
        c=f.split("-")[1]
        d=int(f.split("-")[2].split(".")[0])
        if c==cat:
            infos=get_info_pages(c,d)
            dt=infos["date"]
            if infos["etat"]=="good":
                dts[d]=todt(dt)
    dts=sorted(dts.items(), key=lambda t:t[1])
    print( dts )
    pm=0
    for d in dts:
        if ad<d[1]:
            pm=d[0]
            break
    ps[cats.index(cat)]=pm
	
def verif_match(cat):
    day=ps[cats.index(cat)]
    infospg1=get_info_pages(cat,day)
    scrap_page(cat,day)
    infospg2=get_info_pages(cat,day)
    if infospg1!=infospg2:
        print(infospg1,"bbbbbbbb",infospg2)
        #les dates sont différentes
        scrap_all_pages_of_cat(cat)
        get_all_dates_cat(cat)

def makepage():
    pg=[]
    for cat in cats:
	    pg.append( make_page( an_page(cat) ) )
    make_final_page(pg[2],pg[1],pg[0])

def main():
    #TODO : a debloquer une fois que j'aurais tout fait sur le server
    #scrap_all()
    for cat in cats:
        get_all_dates_cat(cat)
        #verif_match(cat)
    makepage()
        
########################################### - MAIN CODE - ###########################################

main()


"""
txs=""
for p in ps:
    txs+=str(p)+cac
txs=txs[:-1]

f=open(nfs,"w")
f.write(txs)
f.close()
"""

