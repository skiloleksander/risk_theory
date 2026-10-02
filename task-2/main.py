from classes import Event, Investment
from functions import (
    delete_investment,
    save_investments,
    load_investments,
    check_investment_exists,
    add_investment,
    output_investment,
    list_investments,
    investment_analysis,
    compare_investments,
    compare_all_investments
)

available_commands = {
    "add": "Add new investment",
    "delete": "Delete an investment by ID",
    "output": "Output investment information by ID",
    "list": "List all investments",
    "analysis": "Perform analysis on investment by ID",
    "compare": "Compare two investments by their IDs",
    "compare_all": "Compare all investments",
    "save": "Save investments to a file",
    "load": "Load investments from a file",
    "help": "Show this help message",
    "exit": "Exit the program"
}

def main():
    print("=== Investment Analysis ===")
    while True:
        input_command = input("\n> ").strip().split()

        if not input_command:
            continue

        command = input_command[0]
        args = input_command[1:]

        if command not in available_commands:
            print("Invalid command. Type 'help' to see the list of available commands.")
            continue

        if command == "help":
            print("""List of available commands:
    help - Show this help message
    add - Add new investment
    delete [id] - Delete an investment by ID
    output [id] - Output investment information by ID
    list - List all investments
    analysis [id] - Perform analysis on investment by ID
    compare [id1] [id2] - Compare two investments by their IDs
    compare_all - Compare all investments
    save [filename] - Save investments to a file
    load [filename] - Load investments from a file
    exit - Exit the program""")

        if command == "add":
            if len(args) != 0:
                print("Usage: add")
                continue
            id = input("Enter investment ID: ").strip()
            if check_investment_exists(id):
                print(f"Investment with ID '{id}' already exists.")
                continue
            count_success = int(input("Enter number of success events: "))
            success_events = []
            for i in range(count_success):
                rate = float(input(f"Enter rate for success event {i + 1}: "))
                revenue = float(input(f"Enter revenue for success event {i + 1}: "))
                success_events.append(Event(rate, revenue))
            count_failure = int(input("Enter number of failure events: "))
            failure_events = []
            for i in range(count_failure):
                rate = float(input(f"Enter rate for failure event {i + 1}: "))
                revenue = float(input(f"Enter revenue for failure event {i + 1}: "))
                failure_events.append(Event(rate, revenue))
            add_investment(id, success_events, failure_events)

        if command == "delete":
            if len(args) != 1:
                print("Usage: delete [id]")
                continue
            id = args[0]
            if not check_investment_exists(id):
                print(f"Investment with ID '{id}' does not exist.")
                continue
            delete_investment(id)

        if command == "output":
            if len(args) != 1:
                print("Usage: output [id]")
                continue
            id = args[0]
            if not check_investment_exists(id):
                print(f"Investment with ID '{id}' does not exist.")
                continue
            output_investment(id)

        if command == "list":
            if len(args) != 0:
                print("Usage: list")
                continue
            list_investments()

        if command == "analysis":
            if len(args) != 1:
                print("Usage: analysis [id]")
                continue
            id = args[0]
            if not check_investment_exists(id):
                print(f"Investment with ID '{id}' does not exist.")
                continue
            investment_analysis(id)

        if command == "compare":
            if len(args) != 2:
                print("Usage: compare [id1] [id2]")
                continue
            id1, id2 = args
            if not check_investment_exists(id1):
                print(f"Investment with ID '{id1}' does not exist.")
                continue
            if not check_investment_exists(id2):
                print(f"Investment with ID '{id2}' does not exist.")
                continue
            compare_investments(id1, id2)

        if command == "compare_all":
            if len(args) != 0:
                print("Usage: compare_all")
                continue
            compare_all_investments()

        if command == "save":
            if len(args) != 1:
                print("Usage: save [filename]")
                continue
            filename = args[0]
            save_investments(filename)
            print(f"Investments saved to '{filename}'.")

        if command == "load":
            if len(args) != 1:
                print("Usage: load [filename]")
                continue
            filename = args[0]
            try:
                load_investments(filename)
                print(f"Investments loaded from '{filename}'.")
            except FileNotFoundError:
                print(f"File '{filename}' not found.")

        if command == "exit":
            if len(args) != 0:
                print("Usage: exit")
                continue
            print("Exiting the program.")
            break
        
if __name__ == "__main__":
    main()