"""Quick script to read inputs.
"""

if __name__ == '__main__':
    # Read the number of inputs
    num_inputs = int(input("How many inputs? "))
    assert num_inputs > 3, "At least 3 please."
    print("Enter your {} inputs in the following form: inp1 inp2 ... inp{}".format(
        num_inputs, num_inputs))
    a = list(map(int, input().split()))
    assert(len(a) == num_inputs)
    print(a)
