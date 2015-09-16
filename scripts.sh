#/bin/bash
#Author mirona 14.04.2015
#Modified 15.0.4.2015
#This script is used only on Centos
################################################VARIABLES##############################################################################################################################################
########################################################################################DEFINE COLORS##################################################################################################

BLACK="\033[30m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
PINK="\033[35m"
CYAN="\033[36m"
WHITE="\033[37m"
NORMAL="\033[0;39m"


################################################################################LOADING BAR##########################################################################################################

clear
echo -e $YELLOW "Please wait...."
echo -e $GREEN "[#        ] -loading 10%"
sleep 1
clear
echo -e $YELLOW "Please wait...."
echo -e $GREEN "[##       ] -loading 20%"
sleep 1
clear
echo -e $YELLOW "Please wait...."
echo -e $GREEN "[###      ] -loading 30%"
sleep 1
clear
echo -e $YELLOW "Please wait...."
echo -e $GREEN "[####     ] -loading 40%"
sleep 1
clear
echo -e $YELLOW "Please wait...."
echo -e $GREEN "[#####    ] -loading 50%"
sleep 1
clear
echo -e $YELLOW "Please wait...."
echo -e $GREEN "[######   ] -loading 60%"
sleep 1
clear
echo -e $YELLOW "Please wait...."
echo -e $GREEN  "[#######  ] -loading 70%"
sleep 1
clear
echo -e $YELLOW "Please wait...."
echo -e $GREEN "[#######  ] -loading 80%"
sleep 1
clear
echo -e $YELLOW "Please wait...."
echo -e $GREEN "[######## ] -loading 90%"
sleep 1
clear
echo -e $YELLOW "Please wait...."
echo -e $GREEN "[#########] -loading 100%"
sleep 1
clear


##########################################################################Check Linux DISTRO ##################################################################################################################

cat /etc/redhat-release | awk '{print $1,$3}' | while read distro;
do

echo -e "\n"
echo -e $CYAB "This vm is a $YELLOW $distro"
done

##########################################################################CHECK DISK SPACE ON THE SERVER######################################################################################################"

df -H | awk '{print $5}' | tail -n 1 | cut -c1,2 |  while read space;

do

if [ $space -eq 90 ]; then
       echo -e "The filesystem is altmost full"
              mail -s "Alert. The space is used $space%" user@domain.com
	      else
	          echo -e "\n"
		      echo -e $CYAN "Space used is $space%"
		      fi
		      done

##########################################################################CHECK MEMORY ON THE SERVER##########################################################################################################

free -m | awk 'NR==2{printf "Memory Usage: %s/%sMB (%.2f%)\n", $3,$2,$3*100/$2 }' | while read memory;do
echo -e "\n"
echo -e $CYAN "$memory"
echo -e "\n"
done
