from hillClimbing import HillClimbing


def main():
    # Loop to accept a valid integer for n queens problem
    while True:
        n = int(input("Enter number of Queens: "))

        if n == 2 or n == 3 or n < 1:
            print("Solution does not exist. Please enter a valid integer")

        else:
            break

    # create a HillClimbing object to generate solution
    hc = HillClimbing(n)
    hc.gen_solution()

    # Solution statistics
    print('Number steps climbed : {}'.format(hc.stepsClimbed))
    print('Number of random restarts : {}'.format(hc.restarts))
    print('Number of steps climbed after last restart : {}'.format(hc.stepsClimbedRestart))

    # Solution board 
    print('Solution: ')
    hc.print_solution()


if __name__ == "__main__":
    main()