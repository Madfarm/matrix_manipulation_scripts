class JobApplications:
    def __init__(self):
        self.applied_jobs = []
        self.rejections = []
        self.interviews = []

    def add_applied_job(self, job_title, date_applied, salary, location):
        self.applied_jobs.append({'job_title': job_title, 'date_applied': date_applied, 'salary': salary, 'location': location})

    def add_rejection(self, job_title, date_applied, salary, location):
        self.rejections.append({'job_title': job_title, 'date_applied': date_applied, 'salary': salary, 'location': location})

    def add_interview(self, job_title, date_applied, salary, location):
        self.interviews.append({'job_title': job_title, 'date_applied': date_applied, 'salary': salary, 'location': location})

    def sort_applied_jobs(self, sort_by):
        if sort_by == 'salary':
            self.applied_jobs.sort(key=lambda x: x['salary'])
        elif sort_by == 'location':
            self.applied_jobs.sort(key=lambda x: x['location'])
        elif sort_by == 'date_applied':
            self.applied_jobs.sort(key=lambda x: x['date_applied'])

    def sort_rejections(self, sort_by):
        if sort_by == 'salary':
            self.rejections.sort(key=lambda x: x['salary'])
        elif sort_by == 'location':
            self.rejections.sort(key=lambda x: x['location'])
        elif sort_by == 'date_applied':
            self.rejections.sort(key=lambda x: x['date_applied'])

    def get_total_applications(self):
        return len(self.applied_jobs)

    def get_total_rejections(self):
        return len(self.rejections)

    def get_total_interviews(self):
        return len(self.interviews)

# Create an instance of the class
job_applications = JobApplications()

# Add some jobs
job_applications.add_applied_job('Software Engineer', '2022-01-01', 100000, 'New York')
job_applications.add_applied_job('Data Scientist', '2022-01-02', 150000, 'San Francisco')
job_applications.add_applied_job('Product Manager', '2022-01-03', 120000, 'Los Angeles')
job_applications.add_rejection('Software Engineer', '2022-01-01', 100000, 'New York')
job_applications.add_rejection('Data Scientist', '2022-01-02', 150000, 'San Francisco')
job_applications.add_rejection('Product Manager', '2022-01-03', 120000, 'Los Angeles')
job_applications.add_interview('Software Engineer', '2022-01-01', 100000, 'New York')
job_applications.add_interview('Data Scientist', '2022-01-02', 150000, 'San Francisco')
job_applications.add_interview('Product Manager', '2022-01-03', 120000, 'Los Angeles')

# Sort the applied jobs by salary
job_applications.sort_applied_jobs('salary')

# Sort the rejections by location
job_applications.sort_rejections('location')

# Print the total number of applications, rejections, and interviews
print('Total Applications:', job_applications.get_total_applications())
print('Total Rejections:', job_applications.get_total_rejections())
print('Total Interviews:', job_applications.get_total_interviews())

# Print the applied jobs, rejections, and interviews
print('Applied Jobs:')
for job in job_applications.applied_jobs:
    print(job)

print('Rejections:')
for rejection in job_applications.rejections:
    print(rejection)

print('Interviews:')
for interview in job_applications.interviews:
    print(interview)