"""
SSHDODGE
Tool used to test weakness of some ssh passwords, thanks to a dictionary attack (bypassing fail to ban protection).

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

import socket, os

def ipValidator(ip):
	try:
		socket.inet_pton(socket.AF_INET, ip)
	except AttributeError:
		try:
			socket.inet_aton(ip)
		except socket.error:
			return False
		return ip.count('.') == 3
	except socket.error:
		return False

	return True

def portValidator(port):
	return   (port.isdigit()) and (0 < int(port) <= 65535)

def checkWordlist(wordlist):
	return os.path.isfile(wordlist)

def attemptsValidation(attempts):
	return (attempts.isdigit()) and (0 < int(attempts)) 

def userValidator(user):
	return len(user) < 32