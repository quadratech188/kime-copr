#!/bin/bash

mock -r fedora-43-x86_64 --no-clean --buildsrpm --spec kime.spec --sources .
cp /var/lib/mock/fedora-43-x86_64/result/*.src.rpm .

mock -r fedora-43-x86_64 --no-clean *.src.rpm --enable-network
