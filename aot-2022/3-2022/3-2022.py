import os

# Lower char
keys = [chr(ord('a') + i) for i in range(26)]
values = [i + 1 for i in range(26)]
# Upper char
keys += [chr(ord('A') + i) for i in range(26)]
values += [i + 27 for i in range(26)]

item_priorities = dict(zip(keys, values))


def rucksack_reorganization(file) -> int:
    with open(file, 'r') as f:
        priority_sum = 0

        lines = f.readlines()
        for line in lines:
            half_capacity = len(line) // 2
            first_compartiment = line[:half_capacity]
            second_compartiment = line[half_capacity:]
            
            for char in first_compartiment:
                index = second_compartiment.find(char)
                if index >= 0:
                    priority_sum += item_priorities[char]
                    break
    return priority_sum


def elves_groups_reorganization(file) -> int:
    with open(file, 'r') as f:
        priority_sum = 0

        elves_group = []
        lines = f.readlines()
        for line in lines:
            elves_group.append(line)
            if len(elves_group) < 3:
                continue
            
            for char in elves_group[0][:-1]:
                index1 = elves_group[1].find(char)
                index2 = elves_group[2].find(char)
                if index1 >= 0 and index2 >= 0:
                    priority_sum += item_priorities[char]
                    elves_group = []
                    break
    return priority_sum


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(__location__, 'input.txt')

    print(rucksack_reorganization(file))
    print(elves_groups_reorganization(file))
