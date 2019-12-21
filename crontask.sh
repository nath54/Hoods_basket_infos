#!/bin/bash

cd $HOME
source envsket/bin/activate
cd $HOME/basketgit
git pull
python scrap.py
git commit -am "ok"
git push

exit()

