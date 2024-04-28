# SSH Bruteforcer

## Introduction
This script perform a simple brute force attack on SSH servers.

## Usage
`python3 sshbruteforcer.py <example.com> <22> <username> <passlist.txt>`
- `<hostname>`: IP address or domain name of the target SSH server.
- `<port>`: Port number on which the SSH server is listening. (Default is 22)
- `<username>`: Username to be used for connecting to the SSH server.
- `<passlist>`: Path to the file containing the list of passwords for the brute force attack.
