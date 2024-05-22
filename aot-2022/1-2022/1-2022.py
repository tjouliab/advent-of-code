import os


def max_calories(file) -> int:
    with open(file, 'r') as f:
        calories = []
        lines = f.readlines()

        calories_sum = 0
        for line in lines:
            if line != '\n':
                calories_sum += int(line)
            else:
                calories.append(calories_sum)
                calories_sum = 0
        calories.append(calories_sum)

    return max(calories)


def top_three_max_calories(file) -> int:
    with open(file, 'r') as f:
        calories = []
        lines = f.readlines()

        calories_sum = 0
        for line in lines:
            if line != '\n':
                calories_sum += int(line)
            else:
                calories.append(calories_sum)
                calories_sum = 0
        calories.append(calories_sum)

    return sum(sorted(calories, reverse=True)[:3])


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(__location__, 'input.txt')

    print(max_calories(file))
    print(top_three_max_calories(file))
