class Visit:
    def __init__(self, reason, facility_type, facility_name, date, insurance_covered, out_of_pocket):
        self.reason = reason
        self.facility_type = facility_type
        self.facility_name = facility_name
        self.date = date
        self.insurance_covered = insurance_covered
        self.out_of_pocket = out_of_pocket

class MedicalExpenseVisitTracker:
    def __init__(self):
        self.visits = []

    def add_visit(self, reason, facility_type, facility_name, date, insurance_covered, out_of_pocket):
        self.visits.append(Visit(reason, facility_type, facility_name, date, insurance_covered, out_of_pocket))

    def get_visits(self):
        return self.visits

    def get_total_insurance_covered(self):
        return sum(visit.insurance_covered for visit in self.visits)

    def get_total_out_of_pocket(self):
        return sum(visit.out_of_pocket for visit in self.visits)

def medical_expense_visit_tracker(new_visit=None):
    tracker = MedicalExpenseVisitTracker()
    if new_visit:
        tracker.add_visit(new_visit['reason'], new_visit['facility_type'], new_visit['facility_name'], new_visit['date'], new_visit['insurance_covered'], new_visit['out_of_pocket'])
    visits = tracker.get_visits()
    visits.sort(key=lambda x: x.date, reverse=True)
    total_insurance_covered = tracker.get_total_insurance_covered()
    total_out_of_pocket = tracker.get_total_out_of_pocket()
    return visits, total_insurance_covered, total_out_of_pocket

# Example usage:
new_visit = {
    'reason': 'Headache',
    'facility_type': 'Urgent Care',
    'facility_name': 'MinuteClinic',
    'date': '2022-01-01',
    'insurance_covered': 50,
    'out_of_pocket': 20
}

visits, total_insurance_covered, total_out_of_pocket = medical_expense_visit_tracker(new_visit)

for visit in visits:
    print(f"Reason: {visit.reason}, Facility Type: {visit.facility_type}, Facility Name: {visit.facility_name}, Date: {visit.date}, Insurance Covered: {visit.insurance_covered}, Out of Pocket: {visit.out_of_pocket}")

print(f"Total Insurance Covered: {total_insurance_covered}")
print(f"Total Out of Pocket: {total_out_of_pocket}")