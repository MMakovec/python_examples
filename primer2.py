#! /usr/bin/python2


def main():
    for i in range(15,1,-3):
        print(str(i))

    spisek = [i**2 for i in range(5) if i!=3]
    for el in spisek:
        print(str(el))

    for i,  el in enumerate(spisek):
        print("ind %d: %d" % (i, el))

    dict1 = {"k1":1, "k2":7}
    print(dict1)

if __name__ == "__main__":
    main()