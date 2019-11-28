# import libraries
import requests
import urllib.request
import time
import io
from bs4 import BeautifulSoup
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)


# 0=u17 1=u13 2=u9
cats=["u17","u13","u9"]
rs=[200000002774034,200000002775683,200000002775749]
ds=[200000002848356,200000002851801,200000002851984]
ps=[1,1,1]

cat=0

def scrapage():
    url="https://resultats.ffbb.com/championnat/rencontres/"+str(hex(rs[cat])[2:])+str(hex(ds[cat])[2:])+str(hex(ps[cat])[2:])+".html"
    #print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    txt=soup.decode()
    
    f=io.open("page.html","w",encoding="utf-8")
    f.write(txt)
    f.close()
    
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
    elif nbtd==4:
        j=txt.rfind("<td",0,ihoud)
        jj=txt.rfind("<td",0,j)
        jjj=txt.rfind("<td",0,jj)
        pcod=txt.find(">",jjj,jj)
        pcfd=txt.find("<",pcod,jj)
        pcoh=txt.find(">",jj,ihoud)
        pcfh=txt.find("<",pcoh,ihoud)
    else:
        return "error"

    date=txt[pcod+1:pcfd]
    heure=txt[pcoh+1:pcfh]

    #print("date : "+date)
    #print("heure : "+heure)
    
    tm=int(d1.split("/")[1])
    bm=int(date.split("/")[1])
    
    while tm>bm:
        ps[cat]+=1
        return "datetoup"
    
    tj=int(d1.split("/")[0])
    bj=int(date.split("/")[0])
    
    while tj>bj:
        ps[cat]+=1
        return "datetoup"
    
    adv=""
    
    return "Pour la catégorie "+cats[cat]+", le prochain match est a "+heure+" le "+date+" contre "+adv
    


for x in range(3):
    result=scrapage()
    while result=="datetoup":
        result=scrapage()
    cat+=1

print(result)


