def create_quiz(notes):

    questions = []

    for term, definition in notes.items():
        questions.append(
            f"Q: What is {term}?\nA: {definition}"
        )

    return questions
