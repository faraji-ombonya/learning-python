if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scores = list(arr)

    winner_score = max(scores)
    new_scores = [score for score in scores if score != winner_score]
    runner_up_score = max(new_scores)

    print(runner_up_score)