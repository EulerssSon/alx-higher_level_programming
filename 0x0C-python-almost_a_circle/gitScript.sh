#!/usr/bin/env bash
#this Script is to do simple git push commands
read -rp "Plz Enter The Commmit Msg: " msg
git add .
git commit -m "${msg}"
git push
