import os


def calculate_first_score(file) -> int:
    score_dict = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    result_dict = {
        "A": {
            "X": 3,
            "Y": 6,
            "Z": 0,
        },
        "B": {
            "X": 0,
            "Y": 3,
            "Z": 6,
        },
        "C": {
            "X": 6,
            "Y": 0,
            "Z": 3,
        },
    }

    with open(file, 'r') as f:
        score = 0

        lines = f.readlines()
        for line in lines:
            [opp, you] = line.split()
            score += score_dict[you]
            score += result_dict[opp][you]
    return score


def calculate_second_score(file) -> int:
    score_dict = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }


    result_dict = {
        "A": {
            "X": 3,
            "Y": 1,
            "Z": 2,
        },
        "B": {
            "X": 1,
            "Y": 2,
            "Z": 3,
        },
        "C": {
            "X": 2,
            "Y": 3,
            "Z": 1,
        },
    }
    
    with open(file, 'r') as f:
        score = 0

        lines = f.readlines()
        for line in lines:
            [opp, you] = line.split()
            score += score_dict[you]
            score += result_dict[opp][you]
    return score


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(__location__, 'input.txt')

    print(calculate_first_score(file))
    print(calculate_second_score(file))
