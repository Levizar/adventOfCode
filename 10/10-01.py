from tools import import_input_file
import pprint

instructions = import_input_file()

COMMANDS = {
    "noop": 1,
    "addx": 2,
}

def main():
# signal strength = cycle * value of X register
# consider signal strenght during cycles 20th (before end of execution) and every 40th cycles after that
# 20, 60, 100, 140, ...
# compute sume of signal strength
    cycle = 0
    X = 1
    sum_signal_strengths = 0
    for instruction in instructions:
        command, *args = instruction.split()
        operation_duration = COMMANDS.get(command)
        for operation_cycle in range(1, operation_duration + 1):
            # start cycle
            cycle += 1

            # during cycle
            if (cycle - 20) % 40 == 0:
                signal_strength = cycle * X
                sum_signal_strengths += signal_strength

            # end of cycle
            if command == "addx" and operation_cycle == operation_duration:
                X += int(args[0])

    print(sum_signal_strengths)


main()

