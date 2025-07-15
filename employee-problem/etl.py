import csv
import argparse
import os

def load_csv(file_path):
    with open(file_path, newline='') as csvfile:
        return list(csv.DictReader(csvfile))

def clean_and_filter(employees, department_filter):
    cleaned = []
    for emp in employees:
        salary = emp['Salary'].strip()
        if salary:
            try:
                emp['Salary'] = int(salary)
                if emp['Department'].strip().lower() == department_filter.lower():
                    cleaned.append(emp)
            except ValueError:
                continue
    return cleaned

def save_csv(employees, output_path):
    if not employees:
        print("No data to save.")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=employees[0].keys())
        writer.writeheader()
        writer.writerows(employees)
    print(f"Saved {len(employees)} rows to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="ETL for employee data.")
    parser.add_argument('--department', type=str, default='Engineering', help='Department to filter (default: Engineering)')
    args = parser.parse_args()

    data_path = 'data/employees.csv'
    output_path = f'output/{args.department.lower()}_employees.csv'

    employees = load_csv(data_path)
    filtered = clean_and_filter(employees, args.department)
    save_csv(filtered, output_path)

if __name__ == "__main__":
    main()
