import json, os

# Get directory that the script is running from (not always the CWD)
scriptDir = os.path.realpath(os.path.dirname(__file__))

# Load JSON data as objects
# TODO: load data from a .jsonc file
f = open(f'{scriptDir}\PunchLogicData.json')
data = json.load(f)
employee_data = data['employeeData']
job_data = data['jobMeta']

f.close()

# test
print(employee_data)
print()
input(job_data)
# 
