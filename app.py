from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "running"
    }

@app.get("/.well-known/agent.json")
def agent_card():
    return {
        "name": "employee-agent",
        "description": "Employee Information Agent",
        "version": "1.0",
        "skills": [
            {
                "id": "employee_lookup",
                "description": "Returns employee information"
            }
        ]
    }

@app.get("/employee/{empid}")
def employee(empid):
    return {
        "employeeId": empid,
        "name": "Mubashir",
        "department": "Apigee"
    }
