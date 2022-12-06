## Advent of Code 2022: Day 6 ##
# https://adventofcode.com/2022/day/6 #
#

# read day 6 data
# signal is a string
with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2022\day6\day6-input.txt") as data:
    signal = data.readlines()[0]
    #section_ids = [(pair.strip("\n")).split(",") for pair in data]

# function to detect first marker in signal string
# det_option is option of packet or message
def DetectPacketOrMessage(signal_string, det_option):
    if det_option.lower() == "p":
            uniq_length = 4
        
    elif det_option.lower() == "m":
            uniq_length = 14
        
    else:
        raise Exception("Sorry, no other options are available.")
    
    for i in range(len(signal_string)-uniq_length):
        section = signal_string[i: i + uniq_length]
        if len(set(section)) == uniq_length:
            return i + uniq_length




# main
def main():
    # Part one
    first_packet_marker = DetectPacketOrMessage(signal, 'p')
    print(f"Chars processed before first start-of-packet marker is detected: {first_packet_marker}")

    # Part two
    first_message_marker = DetectPacketOrMessage(signal, "m")
    print(f"Chars processed before first start-of-message marker is detected: {first_message_marker}")

# run program
if __name__ == "__main__":
    main()



