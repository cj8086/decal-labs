#!/bin/bash
PACKDOCSPATH="packocfdocs/usr/bin"
if [ $1 = "install" ]; then
    mkdir -p ./$PACKDOCSPATH
    gcc ./ocfdocs.c -o "./$PACKDOCSPATH/ocfdocs"
    fpm -s dir -t deb -n ocfdocs -v 1.0~ocf1 -C packocfdocs
    # echo "Now manually install the packages: ocfdocs and ocfspy"
    sudo dpkg -i ocfdocs_1.0~ocf1_amd64.deb
    sudo dpkg -i ocfspy_1.0~ocf1_amd64.deb
elif [ "$1" = "remove" ]; then
    sudo apt purge ocfdocs ocfspy
else
    echo "Usage: ./solu.sh <remove>/<install>"
fi


    
