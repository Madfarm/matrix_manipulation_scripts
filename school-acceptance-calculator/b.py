def check_acceptance(class_rank, SAT_score):
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

# Testing the function with various cases
print(check_acceptance(10, 700))  # Output: Accepted
print(check_acceptance(50, 750))  # Output: On the waitlist
print(check_acceptance(100, 300))  # Output: Rejected
print(check_acceptance(5, 600))  # Output: Accepted
print(check_acceptance(100, 900))  # Output: Rejected
print(check_acceptance(0, 600))  # Output: Rejected
print(check_acceptance(50, 100))  # Output: Rejected
print(check_acceptance(10, 850))  # Output: Accepted

