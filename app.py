from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

employees = {
"1001": {
"name": "Mubashir",
"department": "Apigee",
"manager": "Surya",
"location": "Mumbai",
"employmentType": "Permanent",
"grade": "L4",
"status": "Active"
},
"1002": {
"name": "John",
"department": "DevOps",
"manager": "Rahul",
"location": "Pune",
"employmentType": "Contractor",
"grade": "L2",
"status": "Active"
},
"1003": {
"name": "Sarah",
"department": "Security",
"manager": "Anita",
"location": "Bangalore",
"employmentType": "Permanent",
"grade": "L5",
"status": "Inactive"
}
}

@app.get("/")
def home():
return {
"status": "running",
"agent": "employee-agent"
}

@app.get("/.well-known/agent.json")
def agent_card():
return {
"name": "employee-agent",
"description": "Employee Information Agent",
"version": "2.0",
"skills": [
{
"id": "employee_lookup",
"description": "Retrieve employee information"
}
]
}

@app.get("/employee/{empid}")
def get_employee(empid: str):

employee = employees.get(empid)

if not employee:
    return {
        "error": "Employee not found"
    }

return {
    "employeeId": empid,
    **employee,
    "servedBy": "employee-agent",
    "timestamp": str(datetime.now())
}
