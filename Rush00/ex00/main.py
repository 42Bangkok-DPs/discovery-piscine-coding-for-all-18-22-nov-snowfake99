#!/usr/bin/env python3
from checkmate import checkmate

def main():
    
    board = [
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........"
    ]

    
    result = checkmate(board)
    print(result)


if __name__ == "__main__":
    main()
