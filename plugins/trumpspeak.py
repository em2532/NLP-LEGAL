####################
# Trumpspeak loads a pickle of phrrases from the phrase extraction
# it then generates sentences off of this pickle. The results are quite comical
###################

import sys
import os
import nltk
import re
import pickle
from random import randint

def main():
    if(len(sys.argv)==1):
        print("[USAGE]: python Trumpspeak.py <pickle>")
        print("\t Note: In no way does this endorse or represent the views of the candidate")
        print("\t This is a purely educational program that demonstrates natural language processing in the field of politics")

    #loads phrases extracted from a trump speech
    trump_nouns = pickle.load(sys.argv[1],"rb")
    randNum = randint(0,len(trump_nouns))
    print(randNum)





if __name__ == '__main__':
    main()
