# Yarn Commnad

## Installation

[ref](https://classic.yarnpkg.com/en/docs/install/#debian-stable)

```bash
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update
sudo apt install yarn
```

[Error Installation](https://stackoverflow.com/questions/53471063/yarn-error-there-are-no-scenarios-must-have-at-least-one)

## Init a new project

```bash
yarn init
```

## Add library

```bash
yarn add package
```

## Upgrade library

```bash
yarn upgrade package
```

## Remove library

```bash
yarn remove package
```

## Install all pacakges

```bash
yarn
or
yarn install
```

## Install ignore error from incompatible engines

```bash
yarn add <package> --ignore-engines
```
