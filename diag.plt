@startuml

actor user
node OLKI {
    artifact fileJS
    artifact fileDATA
    artifact fileMSG
    (olki PHP) as (php)
    (olki PYTHON)
}
node LULLY {
(lully CRON)
(lully PYTHON)
}

user --> (github): show index.html
fileJS --> (github): get JS for checkboxes
(github) --> php: click checkbox
php --> fileMSG: save checkboxes

fileMSG --> (olki PYTHON): incrond
fileDATA --> (olki PYTHON): get DATA
(olki PYTHON) --> fileDATA: update DATA
(olki PYTHON) --> fileJS: update JS

(lully CRON) --> (lully PYTHON): every day
(lully PYTHON) --> (github): update index.html
(lully PYTHON) --> (FFBB): scrap matches

@enduml

