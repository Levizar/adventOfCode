from tools import import_input_file
import pprint


lines = import_input_file(True)

# inputs are pairs of packets
# find out which packets are in the right order
# a packet is in a right order if the left is smaller than right
# a packet is a list that can contains both integers, list of intergers or list of list
# comparison are made that way:
# integers: left < right
# lists:
#   - element to element comparison: if any right > left -> bad order
#   - if not same size the smaller list should be left
# compare list vs lonely integer: cast integer to list: i -> [i] and perform a list to list comparison
def main():
    # each pair should be indexed starting from one
    # part 1: sum the index of the pair in the right order
    pass

main()

