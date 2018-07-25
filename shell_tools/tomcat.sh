#!/bin/bash

TOMCAT_HOME=/opt/tomcat8
STARTUP_SH=$TOMCAT_HOME/bin/startup.sh
SHUTDOWN_SH=$TOMCAT_HOME/bin/shutdown.sh

printf "%s\n" ========请输入========
printf "  %s\n  %s\n  %s\n  %s\n" 1.start_server 2.shutdown_server 3.restart_server 4.exit
printf "\nplease input number:"
read input
printf "\n"

server_start(){
	echo "--------------starting...--------------"
	$STARTUP_SH
	echo "------------start success!--------------"
}

server_shutdown(){
	echo "--------------stoping...--------------"
	$SHUTDOWN_SH
	echo "------------stop success!--------------"
}

server_restart(){
	echo "--------------restarting...--------------"
	$SHUTDOWN_SH
	echo "server is stoped"
	sleep 5s
	$STARTUP_SH
	echo "server is started"
	echo "------------restart success!--------------"
}

case $input in
    1)  server_start
    ;;
    2)  server_shutdown
    ;;
    3)  server_restart
    ;;
    4)  echo -e "bye you asshole!\n"
    ;;
    *)  echo "fail input"
    ;;
esac