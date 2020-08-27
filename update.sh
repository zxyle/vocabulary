#!/bin/bash

python generate.py

if [ -z $(git status README.md --porcelain) ];
then
    echo "README.md IS NOT MODIFIED"
else
    echo "PLEASE COMMIT YOUR CHANGE FIRST!!!"
    echo git status
    git config --global user.email "zxyful@gmail.com"
    git config --global user.name "zxyle"
    git add README.md
    git commit -m "Update README.md"
    git push
fi