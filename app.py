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
def get_employee(empid: str):
    employee_data = {
        "1001": {"name": "Mubashir", "department": "Apigee"},
        "1002": {"name": "John", "department": "DevOps"},
        "1003": {"name": "Sarah", "department": "Security"},
    }

    record = employee_data.get(
        empid,
        {"name": "Unknown", "department": "Unknown"}
    )

    return {
        "employeeId": empid,
        "name": record["name"],
        "department": record["department"]
    }
