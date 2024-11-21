#!/usr/bin/env python3
from checkmate import checkmate

def main():
    # กระดานหมากรุกตัวอย่าง
    board = [
        "R...",
        ".K..",
        "..P.",
        "...."
    ]

    # เรียกใช้งานฟังก์ชัน checkmate
    result = checkmate(board)
    print(result)


if __name__ == "__main__":
    main()
