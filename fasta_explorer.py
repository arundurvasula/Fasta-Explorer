# Python FASTA explorer
# run with "python fasta_explorer.py [seq.fasta]"
#
#
# function TODO:
# [done] nucleotide count: also include GC content % 
# graphically explore sequence: bar graph of A, G, C, T [implement with matplotlib] + save to file
# convert to peptide sequence + save to file + multiple ORFs
# find genes(?)
# implement splitting of large fasta files
# create a settings file


from sys import argv
from sys import exit

from count_bases import count_bases
from graph_base_count import graph_base_count

prompt = "> "

def repl():
    running = True
    while(running):
        command = raw_input(prompt)
        if command == "count bases":
            base_tuple = count_bases(file)
            print "A: " + str(base_tuple[0]) + " C: " + str(base_tuple[1]) + " G: " + str(base_tuple[2]) + " T: " + str(base_tuple[3])
            print "GC%: " + str(base_tuple[4])
        
        elif command == "exit":
            running = False
            exit()
            
        elif command == "graph base count":
            print "Counting bases...",
            base_tuple = count_bases(file)
            print "Done."
            graph_base_count(base_tuple[0], base_tuple[1], base_tuple[2], base_tuple[3])
            
        elif command == "help":
            help()
        
        elif command == "print description":
            print file_description
        
        else:
            print "Command not found. Try again or type \"help\" for help."           
            
def help():
    print "List of commands in (hopefully) alphabetic order:"
    print "count bases - returns number of a, c, g, t found in file."
    print "exit - exit out of this program."
    print "graph base count - returns a bar graph of the base counts"
    print "help - prints this command." 
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
            # Make this error nicer => be able to try other files
            
    file_description = file.readline()
    print "File loaded. File description: " + file_description 
    print "Entering REPL. Type \"help\" for help."
    repl()

