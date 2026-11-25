#!/usr/bin/env python3
"""Write one office-life joke to /output/entry.txt.

Competition: Make the AI Judge Laugh (u-rama-melon-make-the-ai-judge-laugh-302d0825)
"""

import os

JOKE = "I built a pivot table so beautiful my manager promoted the spreadsheet and forgot I exist."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
