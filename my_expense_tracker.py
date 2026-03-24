import os
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt


FILE_NAME ="expenses.csv"

def initialize_file():
    # if file exists;
    if not os.path.exists(FILE_NAME):
        # if file doesn't exist, create it with headers.
        with open(FILE_NAME, "w", newline="")as file:
         writer = csv.writer(file)
         writer.writerow(["Date","Category","Amount","Description"])


def gui_add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    description = description_entry.get()
# Validate required fields
    if date == "" or category == "" or amount == "":
        messagebox.showerror("Error", "Date, Category, and Amount are required fields!")
        return
    # Validate amount is a number
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number!")
        return
    # Save to CSV File
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    messagebox.showinfo("Success", "Expense Added Successfully!")


    # Clear the input fields after adding the expense
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)


def show_chart():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)[1:]

        if len(rows) == 0:
            messagebox.showinfo("Info", "No Expenses Yet to Display!")
            return
        
        category_totals = {}

        for row in rows:
            category = row[1]
            amount = float(row[2])

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        plt.figure()
        plt.bar(categories, amounts)
        plt.xlabel("Categories")
        plt.ylabel("Amounts")
        plt.title("Expense By Category ")
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))



def view_expenses():

    window = tk.Toplevel()
    window.title("Expense History")
    window.geometry("700x400")

    # Search Box......................
    search_label = tk.Label(window, text="Search:")
    search_label.pack()

    search_entry = tk.Entry(window, width= 30)
    search_entry.pack()

    search_button = tk.Button(window, 
        text="Search",
        command=lambda:search_expenses(search_entry.get(), table))
    
    search_button.pack(pady=5)
    

    # Category filter

    categories = ["All", "Food","Transport", "Groceries", "Electricity"]

    category_var = tk.StringVar()
    category_var.set("All")

    category_menu = ttk.Combobox(window, textvariable=category_var)
    category_menu["values"] = categories
    category_menu.pack()

    # Filter Button
    filter_button = tk.Button(
        window,
        text="Filter",
        command=lambda: filter_category(category_var.get(), table)
    )

    filter_button.pack()

    



    table = ttk.Treeview(window)

    table["columns"] = ("Date", "Category", "Amount", "Description")

    # column width
    table.column("#0", width=0, stretch=tk.NO)
    table.column("Date", anchor=tk.W, width= 100)
    table.column("Category", anchor=tk.W, width=150)
    table.column("Amount", anchor=tk.CENTER, width=100)
    table.column("Description", anchor=tk.W, width=250)


    # headings
    table.heading("Date",text="Date", anchor=tk.W) 
    table.heading("Category", text="Category", anchor=tk.W)
    table.heading("Amount", text= "Amount", anchor=tk.CENTER)
    table.heading("Description", text = "Description", anchor=tk.W) 

   
    table.pack(fill="both", expand=True)

    try:
        with open(FILE_NAME, "r") as file:
            reader= csv.reader(file)

            next(reader, None) 

            for row in reader:
                table.insert("", tk.END, values=row)

    except FileNotFoundError:
        messagebox.showerror("Error", "expenses.csv file not found")



def search_expenses(keyword, table):

    for row in table.get_children():
        table.delete(row)


    with open(FILE_NAME, 'r') as file:
        reader= csv.reader(file)


        for row in reader:
            if keyword.lower() in str(row).lower():
                table.insert("", "end", values=row)



def filter_category(category, table):

    for row in table.get_children():
        table.delete(row)


    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)


        for row in reader:

            if category == "All":
                table.insert("","end", values=row)

            elif row[1].lower() == category.lower():
                table.insert("","end", values=row)


def show_pie_chart():

    data = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            category = row[1]
            amount = float(row[2])


            if category in data:
                data[category] += amount
            else:
                data[category] = amount


    categories = list(data.keys())
    amounts = list(data.values())


    plt.figure()
    plt.pie(amounts, labels=categories, autopct="% 1.1f% %")
    plt.title("Expense Distribution")
    plt.show()



def monthly_trend():

    data = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)


        for row in reader:
            month = row[0][:7]
            amount = float(row[2])


            if month in data:
                data[month] += amount
            else:
                data[month] = amount

    months = list(data.keys())
    amounts = list(data.values())


    plt.figure()
    plt.plot(months, amounts, marker="o")
    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()







    initialize_file()

    # Application Statement......................
    print("Lakes✨Personal Expense Tracker📉")
# ........................................

expenses = []



root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("400x500")

# Date
tk.Label(root, text="Date (YYYY-MM-DD):").pack()
date_entry = tk.Entry(root)
date_entry.pack()

# Category
tk.Label(root, text="Category:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

# Amount
tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# Description
tk.Label(root, text="Description:").pack()
description_entry = tk.Entry(root)
description_entry.pack()


add_btn = tk.Button(root, text="Add Expense", command=gui_add_expense)
add_btn.pack(pady=15)

chart_btn = tk.Button(root, text="Show Expense Chart", command=show_chart)
chart_btn.pack(pady=10)

view_btn = tk.Button(root, text="View",
command=view_expenses)
view_btn.pack(pady=10)

# Chart Button
chart_button = tk.Button(
        root,
        text="Show Pie Chart",
        command= show_pie_chart
    )

chart_button.pack()


    # Monthly Summary Button

trend_button = tk.Button(
        root,
        text="Monthly Trend",
        command=monthly_trend
    )
trend_button.pack()

exit_btn = tk.Button(root, text="Exit", command=root.quit)
exit_btn.pack(pady=10)

root.mainloop()





# ..Main Menu.....................................
# .................................................
while True:
    print("\n Personal Expense Tracker")
    print("1. Add Current Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Filter by Category")
    print("5. Monthly Summary")
    print("6. Delete Expense")
    print("7. Show Expense Chart")
    print("8. Expense Edit ")
    print("9. Expense Report ")
    print("10. Exit")

    option = input("Select an option: ")

# .Adding Expenses.....................
# ................................................
    if option == "1":
       print("Add Current Expense")
       date = input("Enter Date (YYYY-MM-DD): ")
       category = input("Enter Item Category: ")
       amount = float(input("Enter Amount: "))
       description = input("Description: ")


       expense = [date, category, amount, description]
       expenses.append(expense)

       
       
       with open(FILE_NAME,"a",newline="") as file:
          writer = csv.writer(file)
          writer.writerow([date, category, amount, description])

       print("Expense Added Successfully")
    

# Viewing the expenses................................
# ....................................................
    elif option == "2":
      try:
           with open(FILE_NAME,"r")as file:
            reader = csv.reader(file)

            rows = list(reader)[1:] 
            # skip header row...

            if len(rows) == 0:
               print("No Expenses Recorded Yet!.")
            else:
                print("View Expenses")
                print("\n Date| Category | Amount | Description")
                print("-" * 50)

           for row in rows:
                print(f"{row[0]} | {row[1]} |{row[2]} |{row[3]} ")

      except FileNotFoundError:
        print("No Expenses found yet")

# Total Expenses.....................................
# ...................................................
    elif option == "3":
        print("Total Expenses")
        total = 0
        try:
            with open(FILE_NAME,"r") as file:
                reader = csv.reader(file)
                rows = list(reader)

            if len(rows) == 0:
                print("No Expenses Recorded Yet!.")
            else:
                for row in rows:
                    total += float(row[2])
                print(f"\nTotal Expenses: N{total}")

        except FileNotFoundError:
            print("No Expenses found yet")
    
# Categorizing Expenses...........
# ..........................................................
    elif option == "4":
        category_search = input("Enter Category to Filter! ")

        try:
            with open(FILE_NAME,"r") as file:
                reader = csv.reader(file)
                rows = list(reader)

                found = False
                print("\nDate | Category | Amount | Description")
                print("-" * 40)

                for row in rows:
                    if row[1].lower() == category_search.lower():
                        print(f"{row[0]}|{row[1]}|{row[2]}|{row[3]}")
                        found = True

                if not found:
                    print("No Expense Found in this Category")        

        except FileNotFoundError:
            print("No Expenses found yet")


# Monthly Summary............................................
# ...........................................................

    elif option == "5":
        month = input("Enter Specified Month!(YYYY-MM): ").strip()

        total = 0
        found = False

        try:
            with open(FILE_NAME,"r") as file:
                reader = csv.reader(file)
                
                for row in reader:
                    
                    if len(row)< 3:
                        continue

                    date = row[0].strip()

                    if date.lower() == "date":
                        continue

                

                    if date[:7] == month:
                        try:
                            total += float(row[2])
                            found = True
                        except ValueError:
                            pass


            if found:
                print(f"\n{month} Total Expenses: N{total}")
            else:
                print(f"No Expense Found for {month}!")


        except FileNotFoundError:
            print("No Expenses found yet")

# Deleting Expenses............................................

    elif option == "6":
        try:
            with open(FILE_NAME, "r") as file:
                reader = csv.reader(file)
                rows = list(reader) 

                if len(rows) == 0:
                    print("No Expenses to delete")
                else:
                    print("\n Expenses: ")
                    print("No | Date | Category | Amount | Description")
                    print("-" * 90)


                    for index, row in enumerate(rows):
                        print(f"{index + 1} | {row[0]} | {row[1]} | {row[2]} | {row[3]}")

                    delete_option = int(input("Enter a number: "))
                    if 1 <= delete_option <= len(rows):
                        removed = rows.pop(delete_option - 1)


                        with open(FILE_NAME, "w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerows(rows)

                            print("Expense Deleted Successfully!")
      
        except FileNotFoundError:
            print("No Expenses found yet")

# Show Expense Chart............................................

    elif option == "7":
        try:
            with open(FILE_NAME, "r") as file:
                reader = csv.reader(file)
                rows = list(reader)[1:]

            if len(rows) == 0:
                print("No Expenses Yet to Display!")
                continue

            print("Data loaded for charting...")

        except FileNotFoundError:
            print("No Expenses found yet")
        category_totals = {}


        for row in rows:
                category = row[1]
                amount = float(row[2])

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

        print(category_totals)
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        print(categories)
        print(amounts)

        plt.bar(categories, amounts)
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.title("Expenses by Category")
        plt.show()


# Editting Expenses
    elif option == "8":
        try:
            with open(FILE_NAME, "r") as file:
                reader = csv.reader(file)
                rows = list(reader) 

                if len(rows) == 0:
                    print("No Expenses to edit")
                else:
                    print("\n Expenses: ")
                    print("No | Date | Category | Amount | Description")
                    print("-" * 90)


                    for index, row in enumerate(rows):
                        print(f"{index + 1} | {row[0]} | {row[1]} | {row[2]} | {row[3]}")

                    edit_option = int(input("Enter a number: "))
                    if 1 <= edit_option <= len(rows):
                        expense = rows[edit_option - 1]
                        
                        new_date = input(f"Enter new date [{expense[0]}]:") or expense[0]
                        new_category = input(f"Enter new category[{expense[1]}]") or expense[1]
                        new_amoount = input(f"Enter a new Amount[{expense[2]}]") or expense[2]
                        new_description = input(f"Enter a new Description[{expense[3]}]") or expense[3]

                        rows[edit_option - 1] = [new_date, new_category,new_amoount, new_description]

                        with open(FILE_NAME, "w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerows(rows)

                            print("Expense Edit  Successful!")


                       
        except FileNotFoundError:
            print("No Expenses found yet")


# Reports
    elif option == "9":
        try:
            with open(FILE_NAME, "r") as file:
                reader = csv.reader(file)
                rows = list(reader)[1:]

                if len(rows) == 0:
                    print("No Expenses available for reports")
                else:
                    total_expense = 0

                    for row in rows:
                        try:
                            total_expense += float(row[2])
                        except ValueError:
                            pass

                        print(f"\n Total Expenses: N{total_expense}")

# Calculating Totals per Category..........................
                        category_totals = {}

                        for row in rows:
                            category = row[1]
                            try:
                                amount = float(row[2])
                            except ValueError:
                                continue


                            if category in category_totals:
                                category_totals[category] += amount
                            else:
                                category_totals[category] = amount

                    # Print Category Summary

                                print("\n Expenses by Category:")
                                for category, amount in category_totals.items():
                                    print(f"Category:  N{amount}")

# Highest Category..............................................................
# ...............................................................
                        highest_category = max(category_totals,
                         key=category_totals.get)
                        highest_amount = category_totals[highest_category]

                        print(f"\n Highest Spent Category: {highest_category} (N{highest_amount})")

        except FileNotFoundError:
            print("No Expenses found yet")

# Exit the Tracker......................................................
# ......................................................................
    elif option == "10":
        print("Exited Tracker")
        break

    
