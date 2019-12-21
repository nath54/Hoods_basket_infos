#coding:utf-8
import io


def make_page(ii):
    #0=nom categorie 1=l'adversaire 2=le lieu 3=l'heure 4=la date #5=joueurs 6=la journée
    print('TOO',ii)
    if len(ii)==8:
        txt="""
<html>
    <head>
        <meta charset="utf-8">
        <title>Houds Info """+ii[0]+"""</title>
        <link rel="stylesheet" href="https://olki.loria.fr/platform/style.7524b05e.css">
        <link href="page1.css" rel="stylesheet">
        <script src="https://resultats.ffbb.com/js/resultat.js?JSVersion=1.0" type="text/javascript"></script>
    </head>
    <body>
        <p id="u1x" value='"""+ii[0]+"""'></p>
        <p id="journee" value='"""+str(ii[6])+"""'></p>
        
        <div class="body-wrap boxed-container" style="background-color:rgb(200,250,200);">
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
                                <li><strong>Plan: </strong><a href='https://resultats.ffbb.com/here/here_popup.php?id="""+ii[7]+"""'>Lien</a></li>
                                <li><strong>Adv: </strong>"""+str(ii[1])+"""</li>
                            </ul>
                        </div>
                    </div>
                </div>
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
    else:
        print(ii)
        txt="""
<html>
    <head>
        <meta charset="utf-8">
        <title>Houds Info """+ii[0]+"""</title>
        <link rel="stylesheet" href="https://olki.loria.fr/platform/style.7524b05e.css">
        <link href="page1.css" rel="stylesheet">
    </head>
    <body>
        <h1>Error : </h1>
        <p>Pas de match trouvé</p>
        <p>Désolé :(</p>
    </body>
</html>
        """
        f=open(ii[0]+".html","w")
        f.write(txt)
        f.close()

