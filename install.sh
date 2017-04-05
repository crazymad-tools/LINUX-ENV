#!/bin/bash

yum install git
yum install gcc
yum install gcc-c++
yum install python
yum install httpd
yum install php
yum install php-mysql

cp -R userbin ~/.bin
touch ~/.bashrc
sed -i '$a export PATH="$PATH:~/root/.bin"' ~/.bashrc

