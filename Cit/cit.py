from Cit import extra_str
from tinydb import TinyDB, Query
<<<<<<< HEAD
=======
from termcolor import colored
>>>>>>> 3bd7df7f9885b28ce15e4b71f3138e103d720133

from datetime import datetime

class cit:
    def __init__(self, source_str: str) -> None:
        self.src = source_str
        
    def run(self):
        src = list(self.src)
        
        tokens = []
        
        while(len(src) > 0):
            if extra_str.is_alphebetic(src[0]):
                wrd = ''
                
                while len(src) > 0 and extra_str.is_alphebetic(src[0]):
                    wrd += src.pop(0)
                    
                tokens.append(wrd)
            elif extra_str.is_numeric(src[0]):
                number = None
<<<<<<< HEAD
                while len(src) > 0 and extra_str.is_alphebetic(src[0]):    
=======
                while len(src) > 0 and (extra_str.is_alphebetic(src[0]) or (len(tokens) > 1 and src[0] == ' ')):    
>>>>>>> 3bd7df7f9885b28ce15e4b71f3138e103d720133
                    number += src.pop(0)
                    
                tokens.append(number)
            else:
                src.pop(0)
                
        self.interpret(tokens)
                
    def interpret(self, src):
        db = TinyDB('db.json')
        
        if(src[0] == 'store'):
            if(len(src) > 1):
                with open(src[1]) as file:
<<<<<<< HEAD
=======
                    details = ''
                    
                    while len(src) > 2:
                        details += src.pop(2)

>>>>>>> 3bd7df7f9885b28ce15e4b71f3138e103d720133
                    db.insert(
                        {
                            'Path' : src[1], 
                            'Text' : file.read(),
                            'Date' : datetime.today().__str__(),
<<<<<<< HEAD
                            'Details' : src[2]
                        }
                    )
        elif(src[0] == 'commits'):
            for d in db.all():
                c = d
                print(c.keys())
                c.pop('Text')
                print(c)
=======
                            'Details' : details
                        }
                    )
            else:
                print("store " + colored("'filepath' 'extra details'", 'yellow'))
        elif(src[0] == 'commits'):
            if db.all():
                for d in db.all():
                    c = d
                    c.pop('Text')
                    print(c)
            else:
                print(colored('No Commits', 'yellow'))
        elif (src[0] == 'clear'):
            x = input(colored('Are you sure: Y/n?', 'red'))

            if x.upper() == 'Y':
                db.truncate()
                print('Cleared Commits')
>>>>>>> 3bd7df7f9885b28ce15e4b71f3138e103d720133
