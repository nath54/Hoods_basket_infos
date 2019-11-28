# import libraries
import requests
import urllib.request
import time
import io
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import makehtml

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
        lieu="A l'exterieur"
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
        print(g,ggg,gg)
        print(txt[ggg:gg])
        adv=txt[ggg:gg]
        lieu="Chez nous"
        exit()
    else:
        return "error"

    date=txt[pcod+1:pcfd]
    heure=txt[pcoh+1:pcfh]

    #print("date : "+date)
    #print("heure : "+heure)
    
    
    ts = datetime.strptime(d1, '%d/%m/%y')
    bs = datetime.strptime(date, '%d/%m/%y')
    print(ts)
    print(bs)
    """if ts>bs:
        ps[cat]+=1
        return "datetoup"
    """
    
    adv=""
    
    #return "Pour la catégorie "+cats[cat]+", le prochain match est a "+heure+" le "+date+" contre "+adv
    return [cats[cat],adv,lieu,heure,date] #0=nom categorie 1=l'adversaire 2=le lieu 3=l'heure 4=la date
    


for x in range(3):
    result=scrapage()
    while result=="datetoup":
        result=scrapage()
        makepage(result)
    cat+=1

    print(result)



