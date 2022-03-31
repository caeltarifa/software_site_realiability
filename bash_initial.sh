#!/bin/bash
sudo apt update
sudo apt install --yes git 
sudo apt install --yes python3 
sudo apt install --yes python3-venv 
sudo apt install --yes python3-pip

python3 -m venv django-venv

var=`pwd`
#echo "$var"
#source "$var"/django-venv/bin/activate
