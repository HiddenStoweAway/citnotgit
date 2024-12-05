from Cit.cit import cit

inp = ''
while inp != 'EXIT':
    inp = input("Enter your command or type EXIT: ")
    citnotgit = cit(inp)
    citnotgit.run()