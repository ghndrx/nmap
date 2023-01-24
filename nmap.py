#!/usr/bin/python
import os

# Functions
def fpingTxt():
    fpingTarget = input("Set fping range for scan: (192.168.1.0-254)")
    os.system("cd && rm ~/fping.txt") # Combine multiple commands into one line
    os.system(f"fping -a -g {fpingTarget} >> fping.txt")
    print("fping should be finished now!")

def menu():
    print("""
#############################
#                           #
#      CHOOSE ARGUMENTS     #
#         FOR NMAP          #
#                           #
#############################

This is a list of precompiled slightly modular cmds
By default all NMAP cmds are set to -T4
-T4 sends packets at an aggressive rate or 1.25p/s

#############################
0. HOST DISCOVERER - USES NMAP TO CHECK IF TARGET(s) ARE ALIVE
1. FULL SCAN - ALL PORTS (0-65,535)
2. TCP CONNECT, OS, DETAILED SERVICE SCAN FOR OPEN PORTS
3. VIOLATE TCP CONNECTION WITH XMAS
4. MASSCAN PORT 80 OF TARGET(s)
Anything else to exit.
#############################
""")

def menuSelector():
    menuChoice = input("Choose from above")
    switch = {
        "0": "0.Selected Host Discoverer...",
        "1": "1.Selected Full Scan...",
        "2": "2.Selected TCP Connect...",
        "3": "3.Selected TCP Violation...",
        "4": "4.Selected Masscan..."
    }
    print(switch.get(menuChoice, "Exiting..."))
    return menuChoice

def cmdList():
    addOaValid = "0" 
    oaAdder = ""
    menuChoice = menuSelector()
    os.system("cd")
    switch = {
        "0": "nmap -T4 -sn -iL ~/fping.txt %s" % oaAdder,
        "1": "nmap -T4 -p- -iL ~/fping.txt %s" % oaAdder,
        "2": "nmap -T4 -O -sT -sV -iL ~/fping.txt %s" % oaAdder,
        "3": "nmap -T4 -sX -iL ~/fping.txt %s" % oaAdder,
        "4": "masscan -p80 -iL ~/fping.txt %s" % oaAdder
    }
    os.system(switch.get(menuChoice, ""))
