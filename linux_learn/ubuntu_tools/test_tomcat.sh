#!/bin/bash

TOMCAT_HOME=/opt/tomcat8
STARTUP_SH=$TOMCAT_HOME/bin/startup.sh
SHUTDOWN_SH=$TOMCAT_HOME/bin/shutdown.sh

printf "%s\n" ========请输入========
printf "  %s %s\n" 1.start 2.shutdown
read input

case $input in
    1)  $STARTUP_SH
    ;;
    2)  $SHUTDOWN_SH
    ;;
    *)  echo "fail input"
    ;;
esac
