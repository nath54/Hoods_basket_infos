#coding:utf-8
import io


def make_page(inf):
    ii=inf #0=nom categorie 1=l'adversaire 2=le lieu 3=l'heure 4=la date #5=joueurs
    txt="""
<html>
    <head>
        <meta charset="utf-8">
        <title>Houds Info """+ii[0]+"""</title>
        <link rel="stylesheet" href="https://olki.loria.fr/platform/style.7524b05e.css">
        <link href="page1.css" rel="stylesheet">
    </head>
    <body>
        <div class="body-wrap boxed-container">
            <main>
            <section class="hero">
                <div class="container">
                    <div class="hero-inner">
                        <div class="hero-copy">
                            <a href="main_page.html">Retour</a>
                            <h1>Prochain match """+ii[0]+"""</h1>
                            <ul>
                                <li>"""+ii[4]+""" ("""+ii[3]+""")</li>
                                <li><strong>Lieu: </strong>"""+ii[2]+"""</li>
                                <li><strong>Adv: </strong>"""+ii[1]+"""</li>
                            </ul>
                            <h2>Les joueurs :</h2>
                        </div>
                    </div>
                </div>
                <ul>
        """
    for j in ii[5].keys():
        txt+="""
                <div style='color:black; border-radius:25px; padding-left:auto; padding-right:auto; background-color:rgb(40,120,60); border:2px solid black;'><li> """+j+""" : <input type="checkbox" name="present"><label for="present">Present</label></input> <input type="checkbox" name="absent"><label for="absent">Absent</label></input> </li></div>"""
    txt+="""
                </ul>
            </section>
        </div>
    </body>
</html>
"""
    f=open(ii[0]+".html","w")
    f.write(txt)
    f.close()

