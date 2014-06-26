#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                ____                     _ __                                 #
#     ___  __ __/ / /__ ___ ______ ______(_) /___ __                           #
#    / _ \/ // / / (_-</ -_) __/ // / __/ / __/ // /                           #
#   /_//_/\_,_/_/_/___/\__/\__/\_,_/_/ /_/\__/\_, /                            #
#                                            /___/ team                        #
#                                                                              #
# deviceinfo.py                                                                #
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


try:
    import subprocess
    import time
    import sys
    import os
except ImportError:
    pass
definepath = os.getcwd()
sys.path.append('%s/src/' % definepath)
import banner

try:
    banner.print_banner()
    device = \
        raw_input('''\nEnter the device to find information about (example /dev/sde1): '''
                  )
    if device == '':
        print '''[-]Error No Device Found'''
        time.sleep(2)
    else:
        subprocess.Popen('u3-tool -D ' + device, shell=True).wait()
        sys.exit(0)
except KeyboardInterrupt:

    print '''[-]Keyboard Interrupt Detected, Returning To Menu....'''
    time.sleep(2)
except Exception, error:
    print '''[-]Something went wrong, printing error message....'''
    print error
    time.sleep(2)
    sys.exit(0)
