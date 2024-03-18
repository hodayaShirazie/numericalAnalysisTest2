from GuessElimination import calcGussianElimination
from bisection_method import find_roots_np
from colors import bcolors


def printInput():
    print(bcolors.HEADER + "INPUT: " + bcolors.ENDC)
    print("matrix = A_b2 = np.array([[2, 3, 4, 5, 6],"
                     +"[-5, 3, 4, -2, 3],"
                     +"[4, -5, -2, 2, 6],"
                     +"[4, 5, -1, -2, -3],"
                     +"[5, 5, 3, -3, 5]])")
    print("b1 = ([70, 20, 26, -12, 37])")
    print("f(x): e*x**6 -c * x**5 - d* x** 2 - b")

def printDetails():
    print(bcolors.HEADER + "date: " + bcolors.ENDC +"18/3/24\n" + bcolors.HEADER + "group members:\n" + "(1)" + bcolors.ENDC + " name: Shulamit-mor-yossef. id: 206576977.\n" +
          bcolors.HEADER + "(2)" + bcolors.ENDC + " name: Zohar-monsonego. id: 214067662.\n" +
          bcolors.HEADER + "(3)" + bcolors.ENDC + " name: hodaya-shirazie. id: 213907785.\n" +
          bcolors.HEADER + "submitted by: " + bcolors.ENDC + "name: Hodaya-shirazie. id: 213907785.")
    printInput()


if __name__ == '__main__':
    printDetails()
    print(bcolors.HEADER + "OUTPUT: " + bcolors.ENDC)

    sJ = calcGussianElimination()




    find_roots_np(1, 2, 3, 4, 5)

