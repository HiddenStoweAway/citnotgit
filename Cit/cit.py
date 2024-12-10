from Cit import extra_str
from termcolor import colored

from google.cloud import firestore

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
                while len(src) > 0 and (extra_str.is_alphebetic(src[0]) or (len(tokens) > 1 and src[0] == ' ')):    
                    number += src.pop(0)
                    
                tokens.append(number)
            else:
                src.pop(0)
                
        self.interpret(tokens)
                
    def interpret(self, src):
        db = firestore.Client(project="gitbutkit")
        
        files = db.collection('files')
        
        if(src[0] == 'store'):
            if(len(src) > 1):
                with open(src[1]) as file:
                    details = ''
                    
                    while len(src) > 2:
                        details += src.pop(2)

                    files.add(
                        {
                            'Path' : src[1],
                            'Text' : file.read(),
                            'Details' : details,
                            'timestamp' : datetime.now()        
                        }
                    )
            else:
                print("store " + colored("'filepath' 'extra details'", 'yellow'))
        elif(src[0] == 'commits'):
            if files.stream():
                
            else:
                print(colored('No Commits', 'yellow'))
        elif (src[0] == 'clear'):
            x = input(colored('Are you sure: Y/n?', 'red'))

            if x.upper() == 'Y':
                db.truncate()
                print('Cleared Commits')
