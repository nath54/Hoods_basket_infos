import subprocess

GITDIR = '/home/xtof/basketgit'

def metajour(u1X,journee,qui,etat):
    with open(GITDIR+"/data.nath","r") as f: lines=f.readlines
    # on a 1 ligne dans le fichier par (u1X,journee) qui contient "nomjoueur"+etat separes par un TAB
    for l in lines:
        s = l.split('\t')
        if s[0]==u1x and s[1]==journee:
            for i range(2,len(s)):
                if s[i][:-1]==joueur:
                    s[i][-1]=etat
                    break
            break
    with open(GITDIR+"/data.nath","w") as f:
        f.write(''.join(lines))

def gitpull():
    p = subprocess.Popen('git pull', cwd=GITDIR, shell=True, stdout=subprocess.PIPE)
    # stdout, stderr = p.communicate()
    exitcode = p.wait()
    print("exitcode",exitcode)


def fonction():
    # faire un pull du git repo pour avoir la derniere version
    
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
                # modifier les fichiers du repo en consequence
                metajour(u1X,journee,qui,etat)
                


    # faire un commit et un push
    
    
gitpull()

