#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                ____                     _ __                                 #
#     ___  __ __/ / /__ ___ ______ ______(_) /___ __                           #
#    / _ \/ // / / (_-</ -_) __/ // / __/ / __/ // /                           #
#   /_//_/\_,_/_/_/___/\__/\__/\_,_/_/ /_/\__/\_, /                            #
#                                            /___/ team                        #
#                                                                              #
# backup.py                                                                    #
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
    import pexpect
    import time
    import os
    import sys
    import shutil
except ImportError:
    pass
definepath = os.getcwd()
sys.path.append('%s/src/' % definepath)
import banner

try:
    banner.print_banner()
    choice = \
        raw_input('''\n   How many devices would you like to revert to original U3 software 1,2,4,6,: '''
                  )

    if choice == '':
        choice = '1'
    if choice == '1':
        device1 = \
            raw_input('''\n   Enter the device to change iso image on (example /dev/sde1): '''
                      )
        if device1 == '':
            print '''   [-]Device Missing'''
        else:
            print '''\n   Replacing Iso File Please Wait...'''
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device1)
            child1.sendline('y')
            time.sleep(5)

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device1, shell=True).wait()
            print '''   Backup Complete Returning To Menu...'''
            time.sleep(2)

    if choice == '2':
        device1 = \
            raw_input('''\n   Enter the device to change iso image on (example /dev/sde1): '''
                      )
        device2 = raw_input('''\n   Enter next device: ''')
        if device1 == '' or device2 == '':
            print 'Device Missing'
            time.sleep(2)
        else:
            print '''\n   Replacing Iso File Please Wait...'''
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device1)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device2)
            child1.sendline('y')
            time.sleep(5)

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device1, shell=True).wait()

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device2, shell=True).wait()
            print '''   Backup Complete Returning To Menu...'''
            time.sleep(2)

    if choice == '4':
        device1 = \
            raw_input('''\n   Enter the device to change iso image on (example /dev/sde1): '''
                      )
        device2 = raw_input('''\n   Enter next device: ''')
        device3 = raw_input('''\n   Enter next device: ''')
        device4 = raw_input('''\n   Enter next device: ''')
        if device1 == '' or device2 == '' or device3 == '' or device4 \
            == '':
            print '''   Device Missing'''
            time.sleep(2)
        else:
            print '''\n   Replacing Iso File Please Wait...'''
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device1)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device2)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device3)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device4)
            child1.sendline('y')
            time.sleep(5)

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device1, shell=True).wait()

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device2, shell=True).wait()

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device3, shell=True).wait()

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device4, shell=True).wait()
            print '''   Backup Complete Returning To Menu...'''
            time.sleep(2)

    if choice == '6':
        device1 = \
            raw_input('''\n   Enter the device to change iso image on (example /dev/sde1): '''
                      )
        device2 = raw_input('''\n   Enter next device: ''')
        device3 = raw_input('''\n   Enter next device: ''')
        device4 = raw_input('''\n   Enter next device: ''')
        device5 = raw_input('''\n   Enter next device: ''')
        device6 = raw_input('''\n   Enter next device: ''')

        if device1 == '' or device2 == '' or device3 == '' or device4 \
            == '' or device5 == '' or device5 == '':
            print '''   [-]Device Missing'''
            time.sleep(2)
        else:
            print '''\n   Replacing Iso File Please Wait...'''
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device1)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device2)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device3)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device4)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device5)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 8060928 ' + device6)
            child1.sendline('y')
            time.sleep(5)

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device1, shell=True).wait()

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device2, shell=True).wait()

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device3, shell=True).wait()

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device4, shell=True).wait()

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device5, shell=True).wait()

            subprocess.Popen('u3-tool -l backup/origU3/U3\ System.iso %s'
                              % device6, shell=True).wait()
            print '''   Backup Complete Returning To Menu...'''
            time.sleep(2)
except KeyboardInterrupt:

    print '''[-]Keyboard Interrupt Detected, Returning To Menu.'''
    time.sleep(2)
except Exception, error:
    print '[-]Something went wrong, printing error message..'
    print error
    time.sleep(2)
    sys.exit(0)
