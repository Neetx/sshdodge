"""
SSHDODGE
Tool used to test weakness of some ssh password, thanks to a dictionary attack (bypassing fail to ban protection).

Copyright (C) 2017  Neetx

This file is part of sshdodge.

Sshdodge is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Sshdodge is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

CONTACTS:
	- neetx@protonmail.com
"""

import os, subprocess

def find_packet_manager():
	pm = [ "apt", "yum", "pacman"]
	out = None
	for item in pm:
		if os.system("which " + item) == 0:
			out = item
			break
	return out

def install_dependences():
	try:
		"""pm = find_packet_manager()
		syntax = None
		if pm == "apt":
			syntax = pm + " install"
		if pm == "pacman" """

		print "\n[*] Installing dependences..\n"
		os.system("apt install pluma")
		print "\n[*] Dependences installed..\n"
	except OSError as e:
		print "[!] Error!\n"
		print e
		print "\n[*] Closing..\n"

def check_tool(tool):
    try:
        devnull = open(os.devnull)
        subprocess.Popen([tool], stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True

def check_dependences():
	dependences = True
	print "[*] Checking dependences.."
	if not check_tool("ssh"):
		print "\tSsh not found!"
		dependences = False
	if not check_tool("anonsurf"):
		print "\tAnonsurf not found!"
		dependences = False
	if not check_tool("sshpass"):
		print "\tSshpass not found!"
		dependences = False
	if not check_tool("tor"):
		print "\tTor not found!"
		dependences = False
	if dependences:
		print "[*]Dependences was already installed: OK"

	return dependences

def manage_dependences():
	if check_dependences():
				pass
	else:
		while 1:
			response = raw_input("Do you want to install dependences?(Y/n)")
			if response == "Y" or response == "y":
				install_dependences()
				break
			elif response == "N" or response == "n":
				print "[*] Closing.."
				exit()
			else:
				print "[!] Wrong response!"