#!/usr/bin/bash

echo "Etner your commit msg Plz:"
read msg
git add .
git commit -m $msg
git push
