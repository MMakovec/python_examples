#! /usr/bin/python2

import time



def main(): # Funkcija main za omejitev scope
    print("moje besedilo")
    print "test"    # primer delovanja print v python2
    time.sleep(1)
    print("Moje stevilo: %d" % 5)   # google print formats pythons


if __name__ == "__main__":
    main()
    