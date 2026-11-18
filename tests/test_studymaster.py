from studymaster import calculate_gpa

def test_gpa():
    assert calculate_gpa(["A", "B"]) == 3.5
