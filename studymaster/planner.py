tasks = []

def add_task(name, days_left, difficulty):

    priority_score = difficulty * 10 + (30 - days_left)

    tasks.append(
        {
            "name": name,
            "score": priority_score
        }
    )

def recommend_tasks():

    ordered = sorted(
        tasks,
        key=lambda x: x["score"],
        reverse=True
    )

    return ordered
