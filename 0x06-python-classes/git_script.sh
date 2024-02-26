#!/usr/bin/bash

read -p "Enter the ocmmit msg" msg
git add .
git commit -m "${msg}"
git push
