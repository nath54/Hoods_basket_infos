#coding:utf-8
import io


def make_page(inf):
    ii=inf #0=nom categorie 1=l'adversaire 2=le lieu 3=l'heure 4=la date
    txt="""
<html>
    <head>
        <meta charset="utf-8">
        <title>Basket Info """+ii[0]+"""</title>
        <link href="page1.css" rel="stylesheet">
    </head>
    <body>
        <a href="main_page.html">Retour</a>
        <h1>Categorie """+ii[0]+"""</h1>
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
                        <h3>"""+ii[1]+""" </h3>
                    </td>
                    <td>
                        <h3>"""+ii[2]+"""</h3>
                    </td>
                    <td>
                        <h3>A """+ii[3]+"""</h3>
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

