from Cit.cit import cit
from termcolor import colored

inp = ''
while inp != 'EXIT':
    inp = input("Enter your command or type " + colored('EXIT: ', 'red'))
    citnotgit = cit(inp)
    citnotgit.run()