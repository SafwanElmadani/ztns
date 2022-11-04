
## Zero Trust in Network Slicing (ZTNS)
This repo contains initial implementation of zero trust methodology in 5G network slicing.

## How run
I used [truffle](https://trufflesuite.com/) framework for the development process of the smart contracts. All of my npm packages are installed locally:
```zsh
mkdir working-dir 
cd working-dir
#install requited nmp packages
npm install truffle
npm install ganache
#clone the repo
git clone https://github.com/SafwanElmadani/ztns.git
cd ztns
#to create blockchain start ganache (please see truffle docs for details)
npx ganache
#to compile and migrate contract use truffle console (please see truffle docs for details)
npx truffle console
```
