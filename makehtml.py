#coding:utf-8
import io


def make_page(infs):
    for x in range(len(infs)):
        ii=infs[x] #0=nom categorie 1=l'adversaire 2=le lieu 3=l'heure 4=la date
        txt="""
<html>
    <head>
        <meta charset="utf-8">
        <title>Basket Info """+ii[0]+"""</title>
        <link href="page1.css" rel="stylesheet">
    </head>
    <body>
        <a href="main_mage.html">Retour</a>
        <h1>Catégorie """+ii[0]+"""</h1>
        <div>
            <table>
                <tr>
                    <th></th>
                    <th>Adversaire</th>
                    <th>Lieu</th>
                    <th>Heure</th>
                    <th>Date</th>
                </tr>
                <tr>
                    <td>
                        <h2>Prochain match : </h2>
                    </td>
                    <td>
                        <h3>Contre """+ii[1]+""" </h3>
                    </td>
                    <td>
                        <h3>"""+ii[2]+"""</h3>
                    </td>
                    <td>
                        <h3>À """+ii[3]+"""</h3>
                    </td>
                    <td>
                        <h3>Le """+ii[4]+"""</h3>
                    </td>
                </tr>
            </table>
        </div>
    </body>
</html>
"""
        f=open(ii[0]+".html","w")
        f.write(txt)
        f.close()

make_page([["u17","Bar le Duc","Chez Nous","18:00","29/11/2019"],["u13","Villers","À l'exterieur","17:00","2/12/2019","u9","Sluc Nancy Basket","Chez nous","15:00","12/12/2019"]])
