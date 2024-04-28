import requests
import sys

def get_employee_todo_progress(employee_id):
    # API endpoint
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    
    try:
        # Send GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Extract JSON data
        todos = response.json()
        
        # Filter completed tasks
        completed_tasks = [task for task in todos if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos)
        
        # Get employee name
        employee_name = todos[0]['username']
        
        # Print employee's TODO list progress
        print("Employee {} is done with tasks ({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
        
        # Print titles of completed tasks
        for task in completed_tasks:
            print("\t{} {}".format("\u2022", task['title']))
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
        
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
