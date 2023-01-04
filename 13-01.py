from tools import import_input_file_raw
import pprint
import pudb


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
    raw_lines = import_input_file_raw()
    packet_pairs_raw = tuple(l.splitlines() for l in raw_lines.split("\n\n"))
    packet_pairs = tuple((eval(a), eval(b))for a, b in packet_pairs_raw)
    a = 0
    for i, (left, right) in enumerate(packet_pairs, start=1):
        print("")
        title = f" packets pair: {i} "
        print(f"{title:=^40}")
        print(left)
        print(right)
        ioc = is_order_correct(left, right)
        print(("Correct order" if ioc else "Wrong order") + " " + str(ioc))
        if ioc:
            a += i
        print(a)
    print("")
    print(f"The answer is {a}")


def is_order_correct(left, right, space=""):
    space += "   "
    for l, r in zip(left, right):
        print(space + str(l) + " VS " + str(r))
        if not isinstance(l, type(r)):
            if isinstance(l, int):
                # cast l to list
                l = [l]
            else:
                # cast r to list
                r = [r]

        if isinstance(l, list):
            res = is_order_correct(l, r, space)
            if res is not None:
                return res

        # base case: both are integer
        elif l < r:
            return True
        elif l > r:
            return False

    left_len, right_len = len(left), len(right)
    if left_len < right_len:
        print("left ran out of item")
        return True
    elif left_len > right_len:
        print("right ran out of item")
        return False

main()

