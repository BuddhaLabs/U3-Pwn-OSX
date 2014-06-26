#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                ____                     _ __                                 #
#     ___  __ __/ / /__ ___ ______ ______(_) /___ __                           #
#    / _ \/ // / / (_-</ -_) __/ // / __/ / __/ // /                           #
#   /_//_/\_,_/_/_/___/\__/\__/\_,_/_/ /_/\__/\_, /                            #
#                                            /___/ team                        #
#                                                                              #
# about.py                                                                     #
#                                                                              #
# DATE                                                                         #
# 06/27/2012                                                                   #
#                                                                              #
# DESCRIPTION                                                                  #
# U3-Pwn is a tool designed to automate injecting executables to Sandisk       #
# smart usb devices with default U3 software install. This is performed by     # 
# removing the original iso file from the device and creating a new iso        #
# with autorun features.                                                       #
#                                                                              #
# REQUREMENTS                                                                  #
# - Metasploit                                                                 #
# - U3-Tool                                                                    #
# - Python-2.6                                                                 #
#                                                                              #
# AUTHOR                                                                       #
# Zy0d0x - http://www.nullsecurity.net/                                        #
#                                                                              #
################################################################################

import os
import sys
import banner
definepath = os.getcwd()
sys.path.append('%s/src/' % definepath)
banner.print_banner()

print '''
    U3-Pwn is a tool designed to automate injecting executerbles to Sandisk 
    smart usb devices with default U3 software install.  This is performed by 
    removing the original iso file from the device and creating a new iso 
    with autorun features.

    Written by: Michael Johnson (Zy0d0x) @ http://www.nullsecurity.net

    Submit Bugs:zy0d0x at nullsecurity.net

    DISCLAIMER: This is only for testing purposes and can only be used where,
    strict consent has been given. Do not use this for illegal purposes period.

'''

raw_input('''    Press any key to return to menu: ''')
