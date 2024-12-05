from Cit import extra_str
from tinydb import TinyDB, Query

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
                while len(src) > 0 and extra_str.is_alphebetic(src[0]):    
                    number += src.pop(0)
                    
                tokens.append(number)
            else:
                src.pop(0)
                
        self.interpret(tokens)
                
    def interpret(self, src):
        db = TinyDB('db.json')
        
        print(src)
        
        if(src[0] == 'store'):
            if(len(src) > 1):
                with open(src[1]) as file:
                    db.insert(
                        {
                            'Path' : src[1], 
                            'Text:' : file.read(),
                            'Date' : datetime.today().__str__(),
                            'Details' : src[2]
                        }
                    )
        elif(src[0] == 'commits'):
            for d in db.all():
                print(d)