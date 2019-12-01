import sys


def print_res(blocks_sizes, process_sizes, selected_blocks):
    print("Blocks: ", blocks_sizes, "\nProcesses", process_sizes)
    print("\nProcess No.\tProcess Size\tBlock No.")

    for i in range(len(process_sizes)):
        selected = selected_blocks[i] if selected_blocks[i] != 0 else "Not Allocated"
        print(str((i+1)), "\t\t", process_sizes[i], "\t\t", selected)


def first_fit(blocks_sizes, process_sizes):
    selected_blocks = []
    for process in process_sizes:
        for i in range(len(blocks_sizes)):
            if(process < blocks_sizes[i]):
                selected_blocks.append(i + 1)
                blocks_sizes[i] -= process
                break
            if(i == len(blocks_sizes) - 1):
                selected_blocks.append(0)
    return selected_blocks


def best_fit(blocks_sizes, process_sizes):
    selected_blocks = []
    for process in process_sizes:
        best_diff = sys.maxsize
        best_pos = 0
        for i in range(len(blocks_sizes)):
            if(process <= blocks_sizes[i] and blocks_sizes[i] - process < best_diff):
                best_diff = blocks_sizes[i] - process
                best_pos = i + 1
        if (best_pos != 0):
            blocks_sizes[best_pos - 1] -= process
        selected_blocks.append(best_pos)

    return selected_blocks


if (len(sys.argv) != 2):
    print("invalid number of arguments!")
    exit(2)

file_name = sys.argv[1]

try:
    file = open(file_name, "r")
except:
    print("Not found")
    exit(2)
content = file.read()

arr = content.split('\n')

if (len(arr) != 2):
    print("Invalid format!")
    exit(2)

blocks_sizes = arr[0].split(";")
process_sizes = arr[1].split(" ")

try:
    blocks_sizes = [int(block) for block in blocks_sizes]
    process_sizes = [int(block) for block in process_sizes]
except:
    print("Invalid format!")
    exit(2)

blocks_sizes_best = blocks_sizes.copy()

first_selected_blocks = first_fit(blocks_sizes.copy(), process_sizes)
best_selected_blocks = best_fit(blocks_sizes.copy(), process_sizes)

print_res(blocks_sizes, process_sizes, first_selected_blocks)

print_res(blocks_sizes, process_sizes, best_selected_blocks)
