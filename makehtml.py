#coding:utf-8
import io

def make_page(ii):
    #0=nom categorie 1=l'adversaire 2=le lieu 3=l'heure 4=la date #5=joueurs 6=la journée
    print('TOO',ii)
    if len(ii)==8:
        txt="""
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
"""

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
        return txt

def make_final_page(u9,u13,u17):
    txt="""
<!DOCTYPE html>
<html lang="en" >
    <head>
        <meta charset="UTF-8">
        <title>Expanding Column Layout</title>
        <link rel="stylesheet" href="fonts/font-awesome.min.css">
        <link href="fonts/lato.css" rel="stylesheet">
        <link rel="stylesheet" href="normalise.min.css">
        <link rel="stylesheet" href="./style.css">
         <script src="jquery.min.js"></script>
         <script src="https://resultats.ffbb.com/js/resultat.js?JSVersion=1.0" type="text/javascript"></script>
    </head>
    <body>

        <!-- 
        -->
        <script src="./script.js"></script>
  
        <!-- partial:index.partial.html -->
        <section class="strips">
            <article class="strips__strip" id="art1">
                <div class="strip__content" onclick='deto("art1");'>
                    <h1 class="strip__title" data-name="Lorem">U9</h1>
                        <div class="strip__inner-text" id="art1a">"""+u9+"""
        
      
                        </div>
                </div>
            </article>
            <article class="strips__strip" id="art2">
                <div class="strip__content" onclick='deto("art2");'>
                    <h1 class="strip__title" data-name="Ipsum">U13</h1>
                    <div class="strip__inner-text">"""+u13+"""
        
                    </div>
                </div>
            </article>
            <article class="strips__strip" id="art3">
                <div class="strip__content" onclick='deto("art3");'>
                    <h1 class="strip__title" data-name="Dolor">U17</h1>
                    <div class="strip__inner-text">"""+u17+"""

                    </div>
                </div>
            </article>
            <i class="fa fa-close strip__close"></i>
        </section>
        <!-- partial -->
    </body>
</html>"""
    f=open("index.html","w")
    f.write(txt)
    f.close()


