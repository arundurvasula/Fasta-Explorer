# Python FASTA explorer
# run with "python fasta_explorer.py [seq.fasta]"
#
#
# function TODO:
# nucleotide count: also include GC content %
# graphically explore sequence: bar graph of A, G, C, T [implement with matplotlib] + save to file
# convert to peptide sequence + save to file + multiple ORFs
# find genes


from sys import argv
from sys import exit

prompt = "> "

def repl():
    running = True
    while(running):
        command = raw_input(prompt)
        if command == "help":
            help()
        if command == "exit":
            running = False
            exit()
        if command == "print description":
            print file_description
        else:
            print "Command not found. Try again or type \"help\" for help."
            continue            
            
def help():
    print "List of commands:"
    print "help - prints this command." 
    print "exit - exit out of this program."
    print "print description - returns Fasta description"
   
if __name__ == "__main__":
    try:
        file = open(argv[1], 'r')   
    except IndexError:
        print "Fasta file not supplied. Please supply a path to a Fasta file."
        entered_file = raw_input(prompt)
        
        try:
            file = open(entered_file, 'r')   
        except:
            print "File not found."
            
    file_description = file.readline()
    print "File loaded. File description: " + file_description 
    print "Entering REPL. Type \"help\" for help."
    repl()

    