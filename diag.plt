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

user --> (github): get and show index.html
(github) --> fileJS: get JS for checkboxes
(github) --> php: update checkboxes
php --> fileMSG: save checkboxes

fileMSG --> (olki PYTHON): incrond
(olki PYTHON) --> fileDATA: update DATA
(olki PYTHON) --> fileJS: update JS

(lully CRON) --> (lully PYTHON): every day
(lully PYTHON) --> (github): update index.html

@enduml

