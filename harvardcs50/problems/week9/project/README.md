# Personal Finance Tracker

#### Video Demo: <https://youtu.be/mImGgV_zq3k?si=GMZsH64bUsXN9BfZ>

#### Description:

This project is a command-line Personal Finance Tracker implemented in Python. The purpose of this application is to help users manage their daily expenses efficiently by allowing them to record, view, and analyze their spending habits.

The program provides a simple and user-friendly interface where users can input their expenses along with a category such as food, transportation, or entertainment. This allows users to better understand where their money is being spent.

The main features of the program include:
- Adding expenses with an amount and category
- Viewing all recorded expenses
- Generating a summary report of total spending by category
- Exiting the program safely

The program is implemented in a file called project.py. It is structured using multiple functions to ensure modularity and readability. The main() function serves as the entry point of the program and handles the menu system, allowing users to choose different actions.

The add_expense() function is responsible for collecting user input and storing each expense. The view_expenses() function displays all previously entered expenses in a clear format. The summary_report() function presents a breakdown of total spending by category, which is calculated using the calculate_summary() function. This function uses dictionaries to aggregate values efficiently.

In addition to the main program, unit tests are implemented in a separate file called test_project.py. These tests use pytest to verify that the summary calculations are correct and that the program behaves as expected under different conditions.

This project demonstrates my understanding of core Python concepts such as functions, loops, lists, dictionaries, and input validation. It also highlights the importance of writing clean, modular code and testing functionality to ensure reliability.

Overall, this project provides a practical tool for tracking personal finances while showcasing fundamental programming skills learned throughout the course.
