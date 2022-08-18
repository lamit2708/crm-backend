# SSH Guideline

## Check SSH Status

ps aux | grep sshd

## Build Frontend

## Install PM2

    npm install pm2 -g

## Start an application

    pm2 start app.js
    pm2 start npm --start

## Listing all running processes

    pm2 list

## Stop pm2

    pm2 stop all
    sudo systemctl stop httpd
