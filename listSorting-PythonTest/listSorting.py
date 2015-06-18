#!/usr/bin/env python

if __name__ == '__main__':
    import re, string, sys
    order = dict()

    # create a dictionary that keys track of the order. In alphabetic order order[a] = order[A];
    for i in range(len(string.lowercase)):
        order[string.lowercase[i]] = i
        order[string.uppercase[i]] = i

    in_file = open(sys.argv[1], 'r')
    read_string= in_file.read()
    in_file.close()

    # unclear as to whether solution should be writen to "result.txt" or specified output-file
    # program will write to output-file if the user specifies it, otherwise writes to result.txt
    try:
        outfile = open(sys.argv[2], 'w')
    except:
        outfile = open('result.txt','w')

    clean_string = re.sub('[^a-zA-Z\d\s]','', read_string).split()
    # create blank lists
    final_ls = [0]*len(clean_string)
    numbs= []
    words= []
    numb_idx = []
    word_idx = []
    for i in range(len(final_ls)):
        try:
            # handles numbers, converts to int for easy sorting
            number = int(clean_string[i])
            numbs.append(number)
            numb_idx.append(i)
        except:
            # handles words
            words.append(clean_string[i])
            word_idx.append(i)
    # sort number lsit and convert back to string
    numbs = map(str, sorted(numbs))
    # sort word list
    words = sorted(words, key=lambda word: [order[c] for c in word])
    # place elements in proper order in final ls.
    for element, idx in zip(numbs, numb_idx)+ zip(words, word_idx):
        final_ls[idx] = element
    # write to file
    outfile.write(string.join(final_ls," ")+"\n")
    outfile.close()
    exit()
