#!/bin/bash

#Prompts user to enter commit message

read -p "Enter commit message: " message

#Add all changes

git add .

#Commits changes with a message

git commit -m "$message"

#Push changes to remote repository

git push
