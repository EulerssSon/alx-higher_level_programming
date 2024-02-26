#!/usr/bin/env bash
#this scirpt is for fast adding files and commitng
read -p "Enter the commit msg plz: " msg
git add .
git commit -m "${msg}"
git push
