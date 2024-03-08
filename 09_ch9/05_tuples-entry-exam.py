def main(grade_exam):
    applicants = [("Ann", 30), ("Jack", 25), ("Jill", 40)]
    passed_applicants = grade_exam(applicants, 30)
    print("Entry exam passed")
    for name, points in passed_applicants:
        print(f"{name}, {points} points")

def grade_exam(applicants, passing_score):
    passed = []

    for name, points in applicants:
        if points >= passing_score:
            passed.append((name, points))

    return passed

if __name__ == "__main__":
    main(grade_exam)