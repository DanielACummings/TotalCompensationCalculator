import json, os
from datetime import datetime

class Employee():
    def __init__(self, name):
        self.name = name
    regular = 0
    overtime = 0
    doubletime = 0
    wage_total = 0
    benefits_total = 0
    workweek_total_hours = 0


def calc_job_hours(punch_start, punch_end):
    # Incoming datetime example: 2022-02-18 12:29:33
    datetime_format = '%Y-%m-%d %H:%M:%S'
    start_time = datetime.strptime(punch_start, datetime_format)
    end_time = datetime.strptime(punch_end, datetime_format)

    # Get interval between two timstamps as timedelta object
    timedelta_diff = end_time - start_time
    total_hours = timedelta_diff.total_seconds() / 3600
    

    # test
    print(total_hours)
    # 

# def display_results():
# TODO: Output to a .jsonc file

def process_punch(job_data, punch, active_employee):
    REGULAR_PAY_MAX = 40
    OVERTIME_MAX = 48
    job_worked = punch['job']
    punch_start = punch['start']
    punch_end = punch['end']
    rate_total = 0
    benefits_total = 0

    # Get rate & benefits rate
    for job_object in job_data:
        if job_object['job'] == job_worked:
            rate = job_object['rate']
            benefits_rate = job_object['benefitsRate']
            break
    job_hours = calc_job_hours(punch_start, punch_end)


# Get directory that the script is running from (not always the CWD)
scriptDir = os.path.realpath(os.path.dirname(__file__))

# Load JSON data as objects
# TODO: load data from a .jsonc file
f = open(f'{scriptDir}\PunchLogicData.json')
data = json.load(f)
employee_data = data['employeeData']
job_data = data['jobMeta']

# Process employee data
employees = []
for employee_obj in employee_data:
    # Loop through single employee's data
    for key, value in employee_obj.items():
        if key == 'employee':
            employee_name = value
            active_employee = Employee(employee_name)
        elif key == 'timePunch':
            for punch in employee_obj[key]:
                process_punch(job_data, punch, active_employee)
# TODO: else handle bad data
# TODO: Handle when employee name already exists in employees
    employees.append(active_employee)


f.close()

# test
input('test complete')
# 
