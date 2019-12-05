#!/bin/bash

function makeproject() {
    cd
    python /Users/thanoschourlias/Documents/codingprojects/autoProjectMakerFor_vscode/create.py $1
    cd /Users/thanoschourlias/Documents/codingprojects
    git init
    git remote add origin git@github.com:Athanasioschourlias/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}







































# source /Users/thanoschourlias/Documents/codingprojects/autoProjectMakerFor_vscode/.my_custom_commands.sh