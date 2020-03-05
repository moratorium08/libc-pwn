#!/bin/sh
set -eu

for dir in `ls boxes`
do
    cd ./boxes/$dir
    sh $0
    cd -
done
