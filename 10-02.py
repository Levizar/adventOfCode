from tools import import_input_file
import pprint

instructions = import_input_file()

COMMANDS = {
    "noop": 1,
    "addx": 2,
}


def main():
# PART 1:
# signal strength = cycle * value of X register
# consider signal strenght during cycles 20th (before end of execution) and every 40th cycles after that
# 20, 60, 100, 140, ...
# compute sume of signal strength
# PART 2:
# a sprite is 3 pixels wide
# X control horizontal position of middle of a sprite
# CRT is 40 pixel wide and 6 high
# CRT draws a pixel by cycle
# pixel are represented by `#`

    cycle = 0
    X = 1
    CRT_lines = []
    CRT_line = ""
    for instruction in instructions:
        command, *args = instruction.split()
        operation_duration = COMMANDS.get(command)
        for operation_cycle in range(1, operation_duration + 1):
            # start cycle
            cycle += 1

            # during cycle
            is_drawing = abs(X - ((cycle - 1) % 40)) <= 1
            CRT_line += "#" if is_drawing else "."

            # end of line
            if cycle % 40 == 0:
                CRT_lines.append(CRT_line)
                CRT_line = ""

            # end of cycle
            if command == "addx" and operation_cycle == operation_duration:
                X += int(args[0])
    
    for line in CRT_lines:
       print(line)


main()

