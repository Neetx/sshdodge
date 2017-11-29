SSHDODGE
Tool used to test weakness of some ssh password, thanks to a dictionary attack (bypassing fail2ban protection).

Copyright (C) 2017  Neetx

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

Tool developed to demonstrate the weakness of some ssh password.
It bypasses fail to ban protection changing ip with anonsurf, after some attempts defined in input by user.
Use these tool with consciousness.

Example:
	sudo ./sshdodge -u root -i 127.0.0.1 -p 22 wordlist.txt -a 3

DEPENDENCES: You need to install on your system:
	-tor
	-sshpass
	-proxychains

SYSTEM USED:
	- Debian 9.2

COLLABORATIONS:

davenull : dave-null@riseup.net
neb 	 :nebulasit@riseup.net
Website: https://www.freenixsecurity.net

giuseongit : giuseppe.pagano.p@gmail.com
Website	   : https://github.com/giuseongit 
