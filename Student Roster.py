roster = []

def add_student():
    name = input("Name: ")
    email = input("Email: ")
    age = input("Age: ")
    grade = input("Grade: ")
    roster.append({"name": name, "email": email, "age": age, "grade": grade})
    print(f"Added {name}.")

def delete_student():
    view_students()
    try:
        idx = int(input("Enter student number to delete: ")) - 1
        removed = roster.pop(idx)
        print(f"Removed {removed['name']}.")
    except (ValueError, IndexError):
        print("Invalid selection.")

def view_students():
    if not roster:
        print("No students in roster.")
        return
    print(f"\n{'#':<4} {'Name':<20} {'Email':<25} {'Age':<5} {'Grade'}")
    print("-" * 65)
    for i, s in enumerate(roster, 1):
        print(f"{i:<4} {s['name']:<20} {s['email']:<25} {s['age']:<5} {s['grade']}")
    print()

def main():
    actions = {"1": add_student, "2": delete_student, "3": view_students}
    while True:
        print("\n1. Add student\n2. Delete student\n3. View roster\n4. Quit")
        choice = input("Choose: ").strip()
        if choice == "4":
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
