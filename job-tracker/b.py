class JobApplications:
    def __init__(self):
        self.applied_jobs = []
        self.rejections = []
        self.interviews = []

    def apply_job(self, title, date_applied, salary, location):
        job = {
            'title': title,
            'date_applied': date_applied,
            'salary': salary,
            'location': location
        }
        self.applied_jobs.append(job)

    def reject_job(self, title):
        for job in self.applied_jobs:
            if job['title'] == title:
                self.rejections.append(job)
                self.applied_jobs.remove(job)

    def interview_job(self, title):
        for job in self.applied_jobs:
            if job['title'] == title:
                self.interviews.append(job)
                self.applied_jobs.remove(job)

    def sort_jobs(self, sort_by):
        if sort_by == 'salary':
            return sorted(self.applied_jobs, key = lambda i: i['salary'])
        elif sort_by == 'location':
            return sorted(self.applied_jobs, key = lambda i: i['location'])
        elif sort_by == 'date_applied':
            return sorted(self.applied_jobs, key = lambda i: i['date_applied'])

    def total_applications(self):
        return len(self.applied_jobs)

    def total_rejections(self):
        return len(self.rejections)

    def total_interviews(self):
        return len(self.interviews)


# Create an instance of JobApplications
tracker = JobApplications()

# Apply for jobs
tracker.apply_job('Software Developer', '2024-03-10', 80000, 'New York')
tracker.apply_job('Data Analyst', '2024-03-12', 70000, 'San Francisco')
tracker.apply_job('Product Manager', '2024-03-15', 90000, 'Chicago')

for job in tracker.applied_jobs:
    print(job)

print("\n")
# Sort applied jobs by salary
sorted_jobs = tracker.sort_jobs('salary')
for job in sorted_jobs:
    print(job)

# Reject a job
tracker.reject_job('Data Analyst')

# Interview for a job
tracker.interview_job('Product Manager')


# Total number of applications
print("Total Applications: ", tracker.total_applications())

# Total number of rejections
print("Total Rejections: ", tracker.total_rejections())

# Total number of interviews
print("Total Interviews: ", tracker.total_interviews())