# Update node js

## Link to update node

[Ref](https://phoenixnap.com/kb/update-node-js-version)

## Uninstall nodejs

sudo rm -rf /usr/local/bin/npm /usr/local/share/man/man1/node* ~/.npm
sudo rm -rf /usr/local/lib/node*
sudo rm -rf /usr/local/bin/node*
sudo rm -rf /usr/local/include/node*
sudo apt-get purge nodejs npm
sudo apt autoremove
sudo npm cache clean -f
npm uninstall npm -g

## Install nodejs

sudo apt-get install nodejs
sudo apt-get install npm

## Steps to update nodejs (option 2)

npm cache clean -f
sudo npm install -g n
sudo n stable
sudo n latest

## Yarn install

yarn install --lastest ----ignore-engines
