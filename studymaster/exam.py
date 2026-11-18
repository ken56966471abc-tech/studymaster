from datetime import date

def exam_countdown(exam_date):
    exam = date.fromisoformat(exam_date)
    return (exam - date.today()).days
