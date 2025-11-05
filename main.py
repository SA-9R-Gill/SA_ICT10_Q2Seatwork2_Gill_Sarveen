from pyscript import display, document

def general_weighted_average(e):
    # Clear previous results
    document.getElementById('student_info').innerHTML = ''
    document.getElementById('summary').innerHTML = ''
    document.getElementById('output').innerHTML = ''
    
    # Subject names and corresponding weights (units)
    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE', 'SS', 'VE', 'TLE', 'Music']
    units_subject = [5, 5, 5, 3, 2, 1, 3, 1, 2, 1]  
    
    try:
        # Get student name
        first_name = document.getElementById('first_name').value.strip()
        last_name = document.getElementById('last_name').value.strip()

        # Get grades
        grades = [
            float(document.getElementById('science').value),
            float(document.getElementById('math').value),
            float(document.getElementById('english').value),
            float(document.getElementById('filipino').value),
            float(document.getElementById('ict').value),
            float(document.getElementById('pe').value),
            float(document.getElementById('ss').value),
            float(document.getElementById('ve').value),
            float(document.getElementById('tle').value),
            float(document.getElementById('music').value)
        ]

        # Calculate GWA
        weighted_sum = sum(grade * unit for grade, unit in zip(grades, units_subject))
        total_units = sum(units_subject)
        gwa = weighted_sum / total_units


        summary = "\n".join(f"{subject}: {grade:.0f}" for subject, grade in zip(subjects, grades))
        
        display(f"Name: {first_name} {last_name}", target="student_info")
        display(summary, target="summary")
        display(f"Your General Weighted Average is {gwa:.2f}", target="output")

    except ValueError:
        display("⚠️ Please enter valid numbers for all grade fields.", target="output")