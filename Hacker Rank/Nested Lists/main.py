if __name__ == '__main__':

    records = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])
        scores.append(score)

    minimum_score = min(scores)

    # create a new list of scores without prev min scores
    new_scores = [score for score in scores if score != float(minimum_score)]

    # get new minimum score and
    new_minimum_score = min(new_scores)

    # create a new list of students that match the new minimum score
    target_students = [record[0] for record in records if record[1] == new_minimum_score]

    # sort and display students
    target_students.sort()
    for student in target_students:
        print(student)
    