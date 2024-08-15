# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    t = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            t.append(i)

        elif next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            if are_matching(opening_brackets_stack[-1], next):
                opening_brackets_stack.pop()
                t.pop()
                
            else:
                return i + 1
    if len(opening_brackets_stack) == 0:
        return -1
    else:
        return t[-1] + 1

            



def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == -1:
        print("Success")
    else:
        print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
