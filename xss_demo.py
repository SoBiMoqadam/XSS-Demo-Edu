import os
import time
import webbrowser
from termcolor import colored


print(colored('XSS DEMO', 'red'))


while True:
choice = input(colored('Press a key (i/g/v/s/q): ', 'green')).lower()
if choice == 'i':
print(colored('[INFO] XSS lets attackers inject JS into a victim browser.', 'magenta'))
elif choice == 'g':
print(colored('[GOALS] Learn and secure against XSS attacks.', 'blue'))
elif choice == 'v':
print(colored('Starting Vulnerable Flask App...', 'red'))
elif choice == 's':
print(colored('Starting Secure Flask App...', 'cyan'))
elif choice == 'q':
print(colored('Exiting program...', 'red'))
break
else:
print(colored('Invalid choice!', 'yellow'))
