import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from tkinter import messagebox, ttk, StringVar, Tk, Frame, Label, Entry, Button, END

# In-memory data storage
employee_data = []


# Utility functions
def clear_input_fields():
    """Clear all input fields and reset dropdown."""
    entry_name.delete(0, END)
    combo_education.set("")
    entry_salary.delete(0, END)


# Data operations
def add_employee():
    """Add employee data to the in-memory list."""
    name = entry_name.get()
    education = combo_education.get()
    salary = entry_salary.get()

    if not name or not education or not salary:
        messagebox.showerror("Input Error", "All fields must be filled!")
        return

    try:
        salary = float(salary)
    except ValueError:
        messagebox.showerror("Input Error", "Salary must be a number!")
        return

    new_employee = {"Name": name, "Education_Level": education, "Salary": salary}
    employee_data.append(new_employee)
    clear_input_fields()
    messagebox.showinfo("Data Added", f"Employee '{name}' has been added successfully!")
    display_employee_data()


def display_employee_data():
    """Display employee data in the table."""
    tree.delete(*tree.get_children())  # Clear existing data in the table
    for record in employee_data:
        tree.insert(
            "",
            "end",
            values=(record["Name"], record["Education_Level"], record["Salary"]),
        )


def update_employee():
    """Update selected employee data."""
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showerror("Update Error", "Please select an employee to update!")
        return

    item = tree.item(selected_item)
    selected_name = item["values"][0]
    selected_education = item["values"][1]
    selected_salary = item["values"][2]

    entry_name.insert(0, selected_name)
    combo_education.set(selected_education)
    entry_salary.insert(0, selected_salary)

    global employee_data
    employee_data = [
        record for record in employee_data if record["Name"] != selected_name
    ]


def delete_employee():
    """Delete selected employee data."""
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showerror("Delete Error", "Please select an employee to delete!")
        return

    item = tree.item(selected_item)
    selected_name = item["values"][0]

    global employee_data
    employee_data = [
        record for record in employee_data if record["Name"] != selected_name
    ]
    messagebox.showinfo(
        "Delete Success", f"Employee '{selected_name}' has been deleted!"
    )
    display_employee_data()


def perform_analysis():
    """Perform descriptive and ANOVA analysis on employee data."""
    if not employee_data:
        messagebox.showerror("Data Error", "No data available for analysis!")
        return

    df = pd.DataFrame(employee_data)
    avg_salary_by_education = df.groupby("Education_Level")["Salary"].mean()

    # Group data by Education Level
    grouped_data = [
        df[df["Education_Level"] == level]["Salary"]
        for level in df["Education_Level"].unique()
    ]

    # Validate if there are at least two groups for ANOVA
    if len(grouped_data) < 2:
        messagebox.showerror(
            "Analysis Error",
            "ANOVA requires at least two groups of data. Add more data with different education levels!",
        )
        return

    # Perform ANOVA
    f_stat, p_value = stats.f_oneway(*grouped_data)

    analysis_result = (
        "Significant differences in salary by education level."
        if p_value < 0.05
        else "No significant differences in salary by education level."
    )

    # Display analysis result
    result_text.set(
        f"Average Salary by Education Level:\n{avg_salary_by_education}\n\n"
        f"ANOVA Result:\nF-statistic: {f_stat:.2f}, p-value: {p_value:.4f}\n\n{analysis_result}"
    )

    # Plot Pie Chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        avg_salary_by_education,
        labels=avg_salary_by_education.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
    )
    plt.title("Average Salary by Education Level")
    plt.axis("equal")
    plt.show()


# GUI setup
root = Tk()
root.title("Employee Salary Analysis")

# Input form
frame_input = Frame(root)
frame_input.pack(pady=20)

Label(frame_input, text="Employee Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = Entry(frame_input)
entry_name.grid(row=0, column=1, padx=10, pady=5)

Label(frame_input, text="Education Level:").grid(row=1, column=0, padx=10, pady=5)
education_options = ["SD", "SMP", "SMA", "D3", "S1", "S2"]
combo_education = ttk.Combobox(frame_input, values=education_options, state="normal")
combo_education.grid(row=1, column=1, padx=10, pady=5)

Label(frame_input, text="Salary:").grid(row=2, column=0, padx=10, pady=5)
entry_salary = Entry(frame_input)
entry_salary.grid(row=2, column=1, padx=10, pady=5)

# Buttons
Button(root, text="Add Employee", command=add_employee).pack(pady=10)
Button(root, text="Update Employee", command=update_employee).pack(pady=10)
Button(root, text="Delete Employee", command=delete_employee).pack(pady=10)
Button(root, text="Analyze Data", command=perform_analysis).pack(pady=10)

# Analysis result display
result_text = StringVar()
Label(root, textvariable=result_text, justify="left").pack(pady=20)

# Data table
frame_table = Frame(root)
frame_table.pack(pady=20)

columns = ("Name", "Education Level", "Salary")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
tree.heading("Name", text="Name")
tree.heading("Education Level", text="Education Level")
tree.heading("Salary", text="Salary")
tree.pack()

# Run the application
root.mainloop()
