import subprocess

JSDIR = '/var/www/html/website/n54hoods.js'
LOCDIR = '/home/xtof/n54.dat'

def metajour(u1X,journee,qui,etat):
    with open(LOCDIR,"r") as f: lines=f.readlines
    # on a 1 ligne dans le fichier par (u1X,journee) qui contient "nomjoueur"+etat separes par un TAB
    for l in lines:
        s = l.split('\t')
        lfound=False
        if s[0]==u1X and s[1]==journee:
            ufound=False
            for i range(2,len(s)):
                if s[i][:-1]==joueur:
                    s[i][-1]=etat
                    break
            if not ufound: s.append('\t'+joueur+etat)
            break
    if not lfound:
        s = u1X+"\t"+journee+"\t"+joueur+"\t"+etat+"\n"
        lines.append(s)
    with open(LOCDIR,"w") as f:
        f.write(''.join(lines))

    etats = {}
    for l in lines:
        s = l.split('\t')
        for i range(2,len(s)):
            etats[(s[0],s[1],s[i][:-1])]=s[i][-1]

    # cree la fct JS qui est telechargee et retourne l'etat des boutons
    with open(JSDIR,"w") as f:
        f.write("function getUserState(u1X,journee,qui) {\n")
        first=True
        for u,j,q in etats:
            s=etats[(u,j,q)]
            if first:
                f.write("if (u1X=='"+u+"' && journee=='"+j+"' && qui=='"+q+"') {return '"+s+"';}\n")
                first=False
            else: f.write("else if (u1X=='"+u+"' && journee=='"+j+"' && qui=='"+q+"') {return '"+s+"';}\n")
        if first: f.write("return '??';\n")
        else: f.write("else {return '??';}\n")
        f.write("}\n")
 
def updateOnUserInput():
    # récupérer la dernière ligne du fichier de log
    with open("/home/xtof/fromPython4nlp/message.txt","r") as f:
        # format du string: from pthon4nlpsite: 1575197365 89.87.123.92 olki.loria.fr/python4nlp.php?nom=homme%20inconnu&email=unkn%40where.iam&msg=
        # l'analyser pour extraire le message
        for l in f: continue
        i = l.find('hoodsdeb')
        if i>=0:
            msg=l[i+8:]
            if len(smg)>=4:
                u1X=msg[0]
                journee=msg[1]
                qui=msg[2]
                etat=msg[3]
                # sauver les infos dans un fichier
                metajour(u1X,journee,qui,etat)

