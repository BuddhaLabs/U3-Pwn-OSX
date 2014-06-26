################################################################################
#                ____                     _ __                                 #
#     ___  __ __/ / /__ ___ ______ ______(_) /___ __                           #
#    / _ \/ // / / (_-</ -_) __/ // / __/ / __/ // /                           #
#   /_//_/\_,_/_/_/___/\__/\__/\_,_/_/ /_/\__/\_, /                            #
#                                            /___/ team                        #
#                                                                              #
# U3-Pwn                                                                       #
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


Ubuntu: 

apt-get install u3-tool

x32
wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-installer.run

chmod 755 metasploit-latest-linux-installer.run

./metasploit-latest-linux-installer.run

x64
wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run

chmod 755 metasploit-latest-linux-x64-installer.run

./metasploit-latest-linux-x64-installer.run


Then cd U3-Pwn && python U3-pwn.py 

