from tools import import_input_file
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
    # part 2: 
    # - add divider packets into the packets list 
    # - sort the list using the comparison function
    # - locate divider index (starting at 1) and multiply them to get the decoder key
    raw_packets = import_input_file()
    packets = [eval(raw_packet) for raw_packet in raw_packets if raw_packet]
    dividers = [[[2]], [[6]]]
    packets.extend(dividers)
    ordered_packets = merge_sort(packets)
    
    div_index = []
    for i, packet in enumerate(ordered_packets, start=1):
        if str(packet) in (str(dividers[0]), str(dividers[1])):
            div_index.append(i)

    print(div_index[0] * div_index[1])

def is_order_correct(left, right, space=""):
    space += "   "
    for l, r in zip(left, right):
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
        return True
    elif left_len > right_len:
        return False

def merge_sort(to_sort):
    length = len(to_sort)
    if length <= 1:
        return to_sort

    middle_index = length // 2
    l = merge_sort(to_sort[:middle_index])
    r = merge_sort(to_sort[middle_index:])

    merged = []
    while l and r:
        if is_order_correct(l[0], r[0]):
            merged.append(l.pop(0))
        else:
            merged.append(r.pop(0))
    merged.extend(l)
    merged.extend(r)

    return merged


main()

