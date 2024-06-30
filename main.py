#####################################################################################
#EXTENDED EUCLIDIAN ALGORITHM
#   Author: Jack Ray
#   Date: 6/30/24
#
#CONTEXT:
#   A calculator which employs the extended euclidian algorithm to solve for
#   the Bezout Coefficients
#

from math import floor

def extended_gcd(a, b):
    #Initialize variables
    r_list = [a, b]
    q_list = [None]
    s_list = [1, 0]
    t_list = [0, 1]
    i = 2

    #Implementation and printing of extended euclidean algorithm
    print(f"Euclidean algorithm to find gcd({a}, {b}):")
    while r_list[-1] != 0:
        q_list.insert(i - 1, floor(r_list[i - 2] / r_list[i - 1]))
        r_list.insert(i, r_list[i - 2] - q_list[i - 1] * r_list[i - 1])
        s_list.insert(i, s_list[i - 2] - q_list[i - 1] * s_list[i - 1])
        t_list.insert(i, t_list[i - 2] - q_list[i - 1] * t_list[i - 1])
        print(f"{r_list[i - 2]} - {q_list[i - 1]} * {r_list[i - 1]} = {r_list[i]}")
        i += 1
    print(f"gcd({a}, {b}) = {r_list[-2]}\n")

    #Printing of Extended Euclidean Algorithm proof
    print("Extended Euclidean Algorithm:")
    for i in range(2, len(r_list) - 2):
        print(f"{r_list[i + 1]} = ({s_list[i - 1]}a + {t_list[i - 1]}b) - "+
        f"({s_list[i]}a + {t_list[i]}b) * {q_list[i]}")
        print(f"    {s_list[i + 1]}a + {t_list[i + 1]}b")
    print(f"Bezout Coefficients: {s_list[-2]}, {t_list[-2]}\n")

if __name__ == "__main__":
    while True:
        print("Enter a value for a: ")
        a = int(input())
        print("Enter a value for b: ")
        b = int(input())
        extended_gcd(a, b)
