#!/bin/sh

for dir in `ls boxes`
do
    cd ./boxes/$dir
    sh ./build.sh
    cd -
done
