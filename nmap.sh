#!/bin/shell
#Gregory Hendrickson
#Should run NMAP CMDs for you, Select what you want, aswell as set target.

#Functions are here
fping()
{
    echo "Set fping range for scan: (192.168.1.0/24 or 192.168.1.0-254)"
    read fping_target 
    cd
    echo "fping is running, kickback and chill"
    echo "when finished fping will spit out~/fping.txt" 
    fping -a -g $fping_target > fping.txt  
    echo "fping should be done!"
}

choices()
{
    
    echo "We'll be using ~/fping.txt for targets. "
    echo "Press [Enter] to continue "
    read garbo


    echo "Do you want to create a NMAP output file?[y/n]"
    read out
    put_in=0
    if [ $out = "y" ] 
        then
            echo "Name the output file"
            read name
            echo "$name was chosen for name"
            put_in=1
            echo "Output will be in ~/"
    
        else
            echo "There will be no output file"
    fi

    echo "Do you want to open fping.txt to edit it?[y/n]"
    read open
    if [ $open = "y" ]
    then
            echo "Opening vim press [Enter] to continue"
            read garbo
            vim fping.txt
    else
            echo "We won't be editing fping.txt then"
    fi

    echo "###########################"
    echo "#    Choose Arguments     #"
    echo "#       for NMAP          #"
    echo "###########################"
    
    echo "List of precompiled NMAP commands,  choose from list"
    echo "By defualt i've set the timing options to -T4 for all commands."
    echo "-T4 sends packets at an aggresive rate of 1.25seconds"i
    echo "-iL is used to feed a list of IPs"
    echo "#####################################################################"
    echo "0. Host discoverer - Runs NMAP and checks for hosts that are alive. "
    echo "1. Full scan - All ports (65,535) " 
    echo "2. TCP CONNECT, OS, DETAILED SERVICE SCAN FOR OPEN PORTS "
    echo "3. Violate TCP, FeelsBadMan ;("
    echo "4. Non-NMAP command, portscanner"
    echo "5. Nothing"
    echo "6. Nothing" 
    echo "7. n0thing"
    echo "8. Still has nothing"
    echo "#####################################################################"



    read NUM


  
       case $NUM in 
               0)
                       echo "-sn is a ping sweep no scanning of ports" 
                       if [ $put_in=1 ] 
                       then
                               nmap -T4 -sn -iL ~/fping.txt -oA $name
                               echo "nmap -T4 -sn -iL ~/fping.txt -oA $name"
                       else
                               nmap -T4 -sn -iL ~/fping.txt
                               echo "nmap -T4 -sn -iL ~/fping.txt"
                       fi
         
                                                       ;;
               1)
                       echo "-p- scans all ports of the target (0-65,535)"
                       if [ $put_in=1 ]
                       then
                               nmap -T4 -p- -iL ~/fping.txt -oA $name
                               echo "nmap -T4 -p- -iL ~/fping.txt -oA $name"
                       else
                               nmap -T4 -p- -iL ~/fping.txt 
                               echo "nmap -T4 -p- -iL ~/fping.txt"
                       fi
                       
                       
                                                        ;;
               2)
                       echo "-O determines OS, -sT connects with TCP, -sV determines services open"
                       if [ $put_in=1 ]
                       then
                               nmap -T4 -O -sT -sV -iL ~/fping.txt -oA $name
                               echo "nmap -T4 -O -sT -sV -iL ~/fping.txt -oA $name"
                       else
                               nmap -T4 -O -sT -sV -iL ~/fping.txt
                               echo "nmap -T4 -O -sT -sV -iL ~/fping.txt"
                       fi
                                                        ;;
               3)
                       echo "-sX is a XMAS scan, sets the FIN, PSH, and URG flags"
                       echo "This will determine if a port is closed or open|filtered"

                       if [ $put_in=1 ]
                       then
                               nmap -T4 -sX -iL ~/fping.txt -oA $name
                               echo "nmap -T4 -sX -iL ~/fping.txt -oA $name"
                       else
                               nmap -T4 -sX -iL ~/fping.txt
                               echo "nmap -T4 -sX -iL ~/fping.txt"
                       fi
                       
                                                        ;;
               4)
                       echo "This is a masscan"
                       echo "comes on kali, it is a asynchronous TCP port scanner"
                       masscan -p80 -iL ~/fping.txt 
                       echo "masscan is similiar to nmap"
                       echo "masscan -p80 -iL ~/fping.txt"
                       echo "-p80 selects port 80 to scan"

                       
                       
                       
                       ;;
               5);;
               6);;
               7);;
               8);;
      esac

}





#####
#
# Main Body of Script
#
####

    echo "Start of script..."

    #echo "Generate target list with fping?[y/n]"

    #read list

     #   if [ $list = "y" ] 
      #  then
       #     fping 
        #else 
         #   echo "Awesome!\n"
       # fi
    choices

    echo "End of script..."
