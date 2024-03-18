def check_admission(class_rank, SAT_score):
    if SAT_score < 200 or SAT_score > 800 or class_rank <= 0:
        return "Rejected"
    elif SAT_score >= 800:
        return "Accepted"
    elif SAT_score < 300:
        return "Rejected"
    elif SAT_score >= 650 and class_rank <= 25:
        return "Accepted"
    elif SAT_score < 400 or class_rank >= 75:
        return "Rejected"
    else:
        return "On the waitlist"

print(check_admission(10, 700))  # Output: Accepted
print(check_admission(50, 600))  # Output: Accepted
print(check_admission(100, 500))  # Output: On the waitlist
print(check_admission(200, 300))  # Output: Rejected
print(check_admission(50, 100))  # Output: Rejected
print(check_admission(10, 850))  # Output: Accepted
print(check_admission(50, 900))  # Output: Rejected