{\rtf1\ansi\ansicpg1251\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def fibonacci(n):\
    """Return a list containing the first n Fibonacci numbers."""\
    sequence = []\
    a, b = 0, 1\
    for _ in range(n):\
        sequence.append(a)\
        a, b = b, a + b\
    return sequence\
\
\
def main():\
    try:\
        count = int(input("How many Fibonacci numbers do you want? "))\
        if count <= 0:\
            print("Please enter a positive integer.")\
            return\
        result = fibonacci(count)\
        print(f"First \{count\} Fibonacci numbers: \{result\}")\
    except ValueError:\
        print("Invalid input. Please enter a valid integer.")\
\
\
if __name__ == "__main__":\
    main()}