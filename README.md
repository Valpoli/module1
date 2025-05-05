cd module1
git submodule add https://github.com/TON_USER/moduleA.git modules/moduleA
git submodule add https://github.com/TON_USER/moduleB.git modules/moduleB
git commit -am "Ajout des submodules moduleA et moduleB"

git submodule update --init --recursive


git submodule update --remote --merge
