def count_bases(file):
    """ Returns a base count in this (alphabetical) order: A, C, G, T. """
    #assume that it is a valid fasta file
    num_a = 0
    num_c = 0
    num_g = 0
    num_t = 0
    gc_content = 0.0
    
    for line in file:
        if line.startswith(">"):
            continue
        else:
            for i in line:
                i.lower()
                if i == "a": num_a = num_a + 1
                elif i == "c": num_c = num_c + 1
                elif i == "g": num_g = num_g + 1
                elif i == "t": num_t = num_t + 1
    temp1 = num_c + num_g + 0.0
    temp2 = num_a + num_c + num_g + num_t + 0.0
    gc_content = (temp1 / temp2) * 100 #because python2.7 is awful at dividing
    return (num_a, num_c, num_g, num_t, gc_content)