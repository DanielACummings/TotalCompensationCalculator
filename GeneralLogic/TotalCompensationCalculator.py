import json, os
from datetime import datetime

class Employee():
    def __init__(self, employee_name):
        self.employee = employee_name
        self.regular = 0
        self.overtime = 0
        self.doubletime = 0
        self.wageTotal = 0
        self.benefitTotal = 0



def calc_job_hours(punch_start, punch_end):
    # Incoming datetime example: 2022-02-18 12:29:33
    datetime_format = '%Y-%m-%d %H:%M:%S'
    start_time = datetime.strptime(punch_start, datetime_format)
    end_time = datetime.strptime(punch_end, datetime_format)

    # Get interval between two timstamps as timedelta object
    timedelta_diff = end_time - start_time
    total_hours = timedelta_diff.total_seconds() / 3600

    return total_hours


def get_hours_and_pay(job_data, punch):
    job_worked = punch['job']
    punch_start = punch['start']
    punch_end = punch['end']

    # Get rate & benefits rate
    for job_object in job_data:
        if job_object['job'] == job_worked:
            rate = job_object['rate']
            benefits_rate = job_object['benefitsRate']
            break
    hours = calc_job_hours(punch_start, punch_end)

    return hours, rate, benefits_rate


def update_employee(punch_hours, rate, benefits_rate, employee):
    REGULAR_MAX = 40
    OT_MAX = 8
    OT_MULTIPLIER = 1.5
    DT_MULTIPLIER = 2

    # Calculate & apply regular hours
    regular_rollover = (employee.regular + punch_hours) - REGULAR_MAX
    if regular_rollover > 0:
        regular_to_apply = punch_hours - regular_rollover
    else:
        regular_to_apply = punch_hours
    if regular_to_apply > 0:
        employee.wageTotal += rate * regular_to_apply
        employee.regular += regular_to_apply
    # Calculate & apply overtime hours
    overtime_rollover = (employee.overtime + regular_rollover) - OT_MAX
    if overtime_rollover > 0:
        overtime_to_apply = regular_rollover - overtime_rollover
    else:
        overtime_to_apply = regular_rollover
    if overtime_to_apply > 0:
        employee.wageTotal += (rate * OT_MULTIPLIER) * overtime_to_apply
        employee.overtime += overtime_to_apply
    # Apply doubletime hours
    if overtime_rollover > 0:
        employee.wageTotal += (rate * DT_MULTIPLIER) * overtime_rollover
        employee.doubletime += overtime_rollover
  
    employee.benefitTotal += hours * benefits_rate



##### Program Start #####

# TODO: Add unit tests
# Get directory that the script is running from (not always the CWD)
scriptDir = os.path.realpath(os.path.dirname(__file__))

# Load JSON data as objects
# TODO: load data from a .jsonc file
f = open(f'{scriptDir}\PunchLogicData.json')
data = json.load(f)
employee_data = data['employeeData']
job_data = data['jobMeta']
f.close()

# Process employee data
employees = []
for employee_obj in employee_data:
    # Loop through single employee's data
    for key, value in employee_obj.items():
        if key == 'employee':
            employee_name = value
            active_employee = Employee(employee_name)
            continue
        punch_list = employee_obj[key]
        for punch in punch_list:
            hours, rate, benefits_rate = get_hours_and_pay(job_data, punch)
            update_employee(hours, rate, benefits_rate, active_employee)
# TODO: else handle files which contain bad data
# TODO: Handle when employee name already exists in employees
    employees.append(active_employee)

# TODO: Output to a .jsonc file


# test
for employee in employees:
    print(f'''\
Employee: {employee.employee}
    regular: {employee.regular}
    overtime: {employee.overtime}
    doubletime: {employee.doubletime}
    wageTotal: {employee.wageTotal}
    benefitTotal: {employee.benefitTotal}''')
input('\ntest complete')
# 
