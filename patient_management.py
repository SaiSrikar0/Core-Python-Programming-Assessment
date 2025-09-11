'''5. Hospital Patient Management

Scenario:

A hospital needs a system to manage patient records. Write a program to store patient data, including **name, age, and disease**, and allow the admin to search for patients by disease.

Requirements:

- Store patient records in a list of dictionaries.

- Allow searching for patients based on disease.

- Optional: Use a `Patient` class to manage records.

Input Example:

patients = [

    {"Name": "Alice", "Age": 30, "Disease": "Flu"},

    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},

    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}

]

search_disease = "Flu"

Expected Output:

Patients with Flu: ["Alice", "Charlie"]'''

class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

def search_by_disease(patients, disease):
    return [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]

if __name__ == "__main__":
    patients = [
        {"Name": "Alice", "Age": 30, "Disease": "Flu"},
        {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
        {"Name": "Charlie", "Age": 35, "Disease": "Flu"},
    ]

    search_disease = "Flu"
    result = search_by_disease(patients, search_disease)
    print(f"Patients with {search_disease}: {result}")
