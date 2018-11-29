from hillClimbing import HillClimbing


def main():
    while True:
        n = int(input("Enter number of Queens: "))

        if n == 2 or n == 3 or n < 1:
            print("Solution does not exist. Please enter a valid integer")

        else:
            break

    hc = HillClimbing(n)
    hc.gen_solution()
    print('Number steps climbed : {}'.format(hc.stepsClimbed))
    print('Number of random restarts : {}'.format(hc.restarts))
    print('Number of steps climbed after last restart : {}'.format(hc.stepsClimbedRestart))
    print('Solution: ')
    hc.print_board()


if __name__ == "__main__":
    main()