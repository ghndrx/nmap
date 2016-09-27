#!/usr/bin/python
import os

#Global Elite(variables)
add_oa_valid="0"
oa_adder=""
# Functions
def fping_txt():
    #print "Set fping range for scan: (192.168.1.0/24 or 192.168.1.0-254)"
    fping_target = raw_input("Set fping range for scan: (192.168.1.0-254)")
    os.system("cd")#Make sure we are in root directory.
    os.system("rm ~/fping.txt") #It will only append to fping.txt this will make it have a fresh file to append to.
    print "%s has been selected" % fping_target
    print "fping is running, kickback and chill"
    print "when finished fping will spit out ~/fping.txt"
    os.system("fping -a -g %s >> fping.txt" % (fping_target))
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    print "fping should be finished now!"
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    
def menu():
        print "#############################"
        print "#                           #"
        print "#      CHOOSE ARGUMENTS     #"
        print "#         FOR NMAP          #"
        print "#                           #"
        print "#############################\n"
        print "This is a list of precompiled slightly modular cmds"
        print "By defualt all NMAP cmds are set to -T4"
        print "-T4 sends packets at an aggressive rate or 1.25p/s\n"
        print "#############################"
        print "0. HOST DISCOVERER - USES NMAP TO CHECK IF TARGET(s) ARE ALIVE"
        print "1. FULL SCAN - ALL PORTS (0-65,535)"
        print "2. TCP CONNECT, OS, DETAILED SERVICE SCAN FOR OPEN PORTS"
        print "3. VIOLATE TCP CONNECTION WITH XMAS"
        print "4. MASSCAN PORT 80 OF TARGET(s)"
        print "Anything else to exit."
        print "#############################\n"

def menu_selector():
    menu_choice = raw_input("Choose from above")
    if menu_choice == "0": print "0.Selected Host Discoverer..."
    elif menu_choice == "1": print "1.Selected Full Scan..."
    elif menu_choice == "2": print "2.Selected TCP Connect..."
    elif menu_choice == "3": print "3.Selected TCP Violation..."
    elif menu_choice == "4": print "4.Selected Masscan..."
    else: print "Exiting..."
    return menu_choice

def cmd_list(oa_adder):
    menu_choice = menu_selector()
    os.system("cd")
    if menu_choice == "0": print "nmap -T4 -sn -iL ~/fping.txt %s" % oa_adder;os.system("nmap -T4 -sn -iL ~/fping.txt %s" % oa_adder)
    elif menu_choice == "1": print "nmap -T4 -p- -iL ~/fping.txt %s" % oa_adder; os.system("nmap -T4 -p- -iL ~/fping.txt %s" % oa_adder)
    elif menu_choice == "2": print "nmap -T4 -O -sT -sV -iL ~/fping.txt %s" % oa_adder;os.system("nmap -T4 -O -sT -sV -iL ~/fping.txt %s" % oa_adder)
    elif menu_choice == "3": print "nmap -T4 -sX -iL ~/fping.txt %s" % oa_adder;os.system("nmap -T4 -sX -iL ~/fping.txt %s" % oa_adder)
    elif menu_choice == "4": print "masscan -p80 -iL ~/fping.txt";os.system("masscan -p80 -iL ~/fping.txt")
    else: print ""
###
#
#Main body of script
#
###

print "Start of script..."


#print "Generate a target list with fping? [y/n]"

valid_choice="0"
while valid_choice=="0":
        fping_creator = raw_input("Generate a target list with fping?[y/n]").lower()
        if fping_creator=="y" or fping_creator=="yes": 
                print "Starting fping" 
                fping_txt()
                valid_choice="1"
        elif fping_creator=="n" or fping_creator=="no": 
                print "We will not be generating a target list with fping"
                valid_choice="1"
        else: print "Enter a valid choice ('yes','y', 'n', 'no')"

valid_open="0"
while valid_open=="0":
        open_fping = raw_input("Would you like to edit ~/fping.txt?[y/n]").lower()
        if open_fping == "y" or open_fping=="yes": 
                raw_input("Opening Vim\nPress [ENTER]")
                os.system("vim ~/fping.txt")
                valid_open="1"
        elif open_fping == "n" or open_fping=="no": 
                print "We won't edit ~/fping.txt"
                valid_open="1"
        else: print "Enter valid choice ('yes', 'y', 'n', 'no')"
        
valid_oa="0"
while valid_oa=="0":
        add_oa = raw_input("Do you want to add NMAP output file?[y/n]").lower()
        
        if add_oa == "y" or add_oa=="yes": 
                name_oa = raw_input("What do you want to name the output file?")
                valid_oa="1"
                add_oa_valid="1" #checks later if we should actually add this to cmd
                oa_adder="-oA " + name_oa
        elif add_oa == "n" or add_oa=="no": 
                print "There will be no output file for NMAP"
                valid_oa="1"
        else: print "Enter a valid choice ('yes', 'y', 'n', 'no')"

menu()
cmd_list(oa_adder)

print "End of script..."
