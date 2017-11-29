SshFailToBanBypass
Tool used to test weakness of some ssh password, thanks to a dictionary attack (bypassing fail to ban protection).

Copyright (C) 2017  Neetx

SshFailToBanBypass is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

SshFailToBanBypass is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

CONTACTS:
	- neetx@protonmail.com

SSH FAIL TO BAN BYPASS powered by Neetx with collaboration of Freenix Security.

Tool developed to demonstrate the weakness of some ssh password.
It bypasses fail to ban protection changing ip with anonsurf, after some attempts defined in input by user.
Use these tool with consciousness.

Usage:
	SshFailToBanBypass.py <usr> <ip> <port> <wordlist> <attempts>
Example:
	sudo ./SshFailToBanBypass root 127.0.0.1 22 wordlist.txt 3

DEPENDENCES: You need to install on your system:
	-tor
	-anonsurf
	-sshpass
	-ssh
