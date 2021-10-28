#
# Example file for working with conditional statements
#


def main():
    x, y = 1000, 100

    # conditional flow uses if, elif, else
    if x < y: 
        st = "x is less than y"
    elif x == y: 
        st = "x is the same as Y"
    else:
        st = "x is greater than y"
    # conditional statements let you use "a if C else b"
    # print(st)
    
    ts = "x is less than y" if(x < y) else " x is greater than or the same as y" 
    print(ts)

if __name__ == "__main__":
    main()
