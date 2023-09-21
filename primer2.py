#! /usr/bin/python2
import time
from collections import deque

def main():
    for i in range(15,1,-3):
        print(str(i))

    spisek = [i**2 for i in range(5) if i!=3]
    for el in spisek:
        print(str(el))

    for i,  el in enumerate(spisek):
        print("ind %d: %d" % (i, el))

    dict1 = {"k1":1, "k2":7}
    
    for key, el in dict1.items():
        print(str(el) + " " + key)

    try:
        while True:
            print("Beseda")
            time.sleep(1)
    except KeyboardInterrupt:
        print(KeyboardInterrupt)
    except Exception as e:
        print(e)
    finally:
        print("Exiting")

    inp = raw_input("Vpisi svoje ime:") # python2 posebnost, navaden input vzame ime spremenljivk
    print(inp)

    d = deque(maxlen = 10)

    for o in range(1,35):
        d.append(str(o))

    print(repr(d))

if __name__ == "__main__":
    main()