#coding:utf-8
import io


def make_page(ii):
    #0=nom categorie 1=l'adversaire 2=le lieu 3=l'heure 4=la date #5=joueurs 6=la journée
    print('TOO',ii)
    txt="""
<html>
    <head>
        <meta charset="utf-8">
        <title>Houds Info """+ii[0]+"""</title>
        <link rel="stylesheet" href="https://olki.loria.fr/platform/style.7524b05e.css">
        <link href="page1.css" rel="stylesheet">
    </head>
    <body>
<<<<<<< HEAD
        <p id="u1x" value='"""+inf[0]+"""'></p>
        <p id="journee" value='"""+str(inf[6])+"""'></p>
=======
        <p id="u1x" value='"""+ii[0]+"""'></p>
        <p id="journee" value='"""+str(ii[6])+"""'></p>
>>>>>>> 1e1941ad9707839e1107f8f8e31f2a2a60ad749a
        
        <div class="body-wrap boxed-container" style="background-color:rgb(200,250,200);">
            <main>
            <section class="hero">
                <div class="container">
                    <div class="hero-inner">
                        <div class="hero-copy">
                            <a href="index.html">Accueil</a>
                            <h1>Prochain match """+ii[0]+"""</h1>
                            <i>(Extrait quotidien du site FFBB)</i>
                            <ul style='text-align: left; margin-top: 20'>
                                <li>"""+ii[4]+""" ("""+ii[3]+""")</li>
                                <li><strong>Lieu: </strong>"""+ii[2]+"""</li>
                                <li><strong>Adv: </strong>"""+str(ii[1])+"""</li>
                            </ul>
                            <h2>Les joueurs :</h2>
                        </div>
                    </div>
                </div>
                <ul style='text-align: left; list-style-type: none;'>
        """
    for j in ii[5].keys():
        txt+="""
                <div class="joueur" id='"""+j+"""' style='color:black; border-radius:25px; padding-left:20px; padding-right:auto; background-color:rgb(40,120,60); border:2px solid black;'><li> """+j+""" : <span style='display: inline-block;'><input type="checkbox" id='"""+j+"""pr' name="present" onChange="onChangeBox('"""+j+"""pr')"><label for="present">Present</label></input></span> <input type="checkbox" id='"""+j+"""ab' name="absent" onChange="onChangeBox('"""+j+"""ab')><label for="absent">Absent</label></input> </li></div>"""
    txt+="""
                </ul>
            </section>
        </div>
        <script src="https://olki.loria.fr/n54hoods.js" type="text/javascript"></script>
        <script src="page.js" type="text/javascript"></script>
    </body>
</html>
"""
    # TODO: lancer un JS dans la page qui appele la fct "getUserState(u1X,journee,qui)" qui retourne "pr" ou "ab" ou "??" et qui met a jour les checkbox
    # d'abord charger avec script src=... cette fonction dans https://olki.loria.fr/n54hoods.js

    f=open(ii[0]+".html","w")
    f.write(txt)
    f.close()

