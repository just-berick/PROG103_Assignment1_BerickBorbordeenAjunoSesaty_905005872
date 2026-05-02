# Clinic Queue Management System
# So here's my list of storing all patients in a queue for much ease
queue = []

def add_patient():
    print("\n--- Add Patient to Queue ---")

    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    condition = input("Enter condition/reason for visit: ")

    patient = {
        "name": name,
        "age": age,
        "condition": condition
    }

    queue.append(patient)
    print(name, "has been added to the queue.")

def view_queue():
    print("\n--- Current Queue ---")

    if len(queue) == 0:
        print("The queue is empty.")
    else:
        count = 1
        for patient in queue:
            print("Position :", count)
            print("Name     :", patient["name"])
            print("Age      :", patient["age"])
            print("Condition:", patient["condition"])
            print("-------------------")
            count = count + 1

def serve_patient():
    if len(queue) == 0:
        print("No patients in the queue.")
    else:
        served = queue.pop(0)
        print("\nNow serving:", served["name"])
        print("Condition  :", served["condition"])
        print("Remaining in queue:", len(queue))

def main_menu():
    print("=============================")
    print("  Clinic Queue Manager       ")
    print("  SDG 3: Good Health         ")
    print("=============================")

    while True:
        print("\n1. Add Patient")
        print("2. View Queue")
        print("3. Serve Next Patient")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_queue()
        elif choice == "3":
            serve_patient()
        elif choice == "4":
            print("Goodbye! Thank you for using the Clinic Queue Manager.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

main_menu()
