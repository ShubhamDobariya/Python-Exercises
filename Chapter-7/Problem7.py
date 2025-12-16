"""
    *
   ***
  *****
 *******
*********
"""


def pattern(n):

    for i in range(n):
        # inner loop print space 'N-1' space
        for j in range(n - i - 1):
            print(" ", end="")

        for j in range(2 * i + 1):
            print("*", end="")

        for j in range(n - i - 1):
            print(" ", end="")

        print("")


"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""


def pattern1(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")

        for j in range(i + 1):
            print("*", end=" ")

        print("")


"""
    *
   **
  ***
 ****
*****
"""


def pattern2(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        print("")


if __name__ == "__main__":
    n = int(input("Enter Number : "))

    pattern2(n)
