class Visit:
    def __init__(self, reason, facility_type, facility_name, date, insurance_covered, out_of_pocket):
        self.reason = reason
        self.facility_type = facility_type
        self.facility_name = facility_name
        self.date = date
        self.insurance_covered = insurance_covered
        self.out_of_pocket = out_of_pocket

def medical_expense_visit_tracker(new_visit=None):
    visits = []
    if new_visit:
        visits.append(new_visit)
    visits.sort(key=lambda x: x.date, reverse=True)
    total_insurance_covered = sum(visit.insurance_covered for visit in visits)
    total_out_of_pocket = sum(visit.out_of_pocket for visit in visits)
    return visits, total_insurance_covered, total_out_of_pocket

# Example usage
visit1 = Visit("Cold", "Urgent Care", "Urgent Care Center", "2022-01-01", 100, 50)
visit2 = Visit("Flu", "Hospital", "Hospital Name", "2022-01-15", 200, 100)
visits, total_insurance_covered, total_out_of_pocket = medical_expense_visit_tracker(visit1)
print("Visits:", visits)
print("Total Insurance Covered:", total_insurance_covered)
print("Total Out of Pocket:", total_out_of_pocket)

visits, total_insurance_covered, total_out_of_pocket = medical_expense_visit_tracker(visit2)
print("Visits:", visits)
print("Total Insurance Covered:", total_insurance_covered)
print("Total Out of Pocket:", total_out_of_pocket)