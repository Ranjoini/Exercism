"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""
    rounded = []
    for scores in student_scores:
        rounded.append(round(scores))
    return rounded



def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided."""
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold."""
    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    return best_scores



def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""
    step = (highest - 40) // 4
    return list(range(41 , highest , step))


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order."""
    results = []
    for index , (name , score) in enumerate(zip(student_names , student_scores), start = 1):
        results.append(f"{index}. {name}: {score}")
    return results


def perfect_score(student_info):
    """Find out the name of the student who scored 100."""
    for student in student_info:
        if student[1] == 100:
            return student
    return []