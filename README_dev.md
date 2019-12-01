# Principe

- un CRON sur lully execute 1x/jour crontask.sh
- crontask.sh pull le repo, lance le scrapping + makehtml, puis push les pages generees

- sur github: le client charge une page JS depuis OLKIHOST qui indique l'etat des boutons
- si le user click sur un bouton, le client envoie un message a un script PHP sur OLKIHOST qui sauve le message dans fichier XX

- sur OLKIHOST: avec INCRON, un prog python est execute des que le fichier XX est modifie (par le script PHP)
- le prog python analyze alors le message, rajoute la nouvelle checkbox dans un fichier local d'etat, et recree le fichier JS qui indique l'etat des boutons

