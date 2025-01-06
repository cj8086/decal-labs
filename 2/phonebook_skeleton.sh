#!/bin/bash

PHONEBOOK_ENTRIES="bash_phonebook_entries"


if [ "$#" -lt 1 ]; then
    exit 1

elif [ "$1" = "new" ]; then
    touch ./$PHONEBOOK_ENTRIES
    echo "$2 $3" >> ./$PHONEBOOK_ENTRIES 
    exit 0

elif [ "$1" = "list" ]; then
    if [ ! -e $PHONEBOOK_ENTRIES ] || [ ! -s $PHONEBOOK_ENTRIES ]; then
        echo "phonebook is empty"
    else
        cat ./$PHONEBOOK_ENTRIES
    fi
    exit 0

elif [ "$1" = "lookup" ]; then
    cat $PHONEBOOK_ENTRIES | grep "$2"
    exit 0

elif [ "$1" = "remove" ]; then
    # sed -i "s/<old>/<new>/g" ./filename
    echo "remove $2"
    sed -i -E "/$2 [0-9]{3}-[0-9]{3}-[0-9]{4}/d" "./$PHONEBOOK_ENTRIES"

    # grep -E "Linus Torvalds [0-9]{3}-[0-9]{3}-[0-9]{4}"
    exit 0

elif [ "$1" = "clear" ]; then
    rm ./$PHONEBOOK_ENTRIES
    exit 0

else
     echo "Undefined Operation, try 'new', 'list', 'lookup', 'remove', 'clear'"
     exit 1
fi
