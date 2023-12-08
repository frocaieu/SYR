import PySimpleGUI as sg
import datetime

sg.theme('DarkAmber')

class Receipt:
    def __init__(self, name, value, date, category):
        self.name = name
        self.value = value
        self.date = date
        self.category = category

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.receipts = []

    def add_receipt(self, receipt):
        self.receipts.append(receipt)

def main():
    layout_login = [
        [sg.Text('R-SCANN', font=('Comfortaa', 40), justification='center')],
        [sg.Text('Enter your username', font=('Comfortaa', 20))],
        [sg.Input(key='-USERNAME-', font=('Comfortaa', 20))],
        [sg.Text('Enter your password', font=('Comfortaa', 20))],
        [sg.Input(key='-PASSWORD-', password_char='*', font=('Comfortaa', 20))],
        [sg.Button('Login', font=('Comfortaa', 20))]
    ]

    window_login = sg.Window('Login', layout_login)

    user = None
    default_password = 'password'

    while True:
        event, values = window_login.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Login':
            username = values['-USERNAME-']
            password = values['-PASSWORD-']

            # Replace this check with your actual authentication logic
            if username and password == default_password:
                user = User(username, password)
                window_login.close()
                break
            else:
                sg.popup_error('Invalid username or password. Try again.')

    categories = ['Shopping', 'Groceries', 'Insurance', 'Rent', 'Restaurants', 'Transports', 'Leisure', 'Others']

    layout_receipt = [
        [sg.Text('WELCOME!', font=('Comfortaa', 30), justification='center')],
        [sg.Text('Receipt Name', font=('Comfortaa', 20)), sg.Input(key='-RECEIPT_NAME-', font=('Comfortaa', 20))],
        [sg.Text('Receipt Value', font=('Comfortaa', 20)), sg.Input(key='-RECEIPT_VALUE-', font=('Comfortaa', 20))],
        [sg.Text('Receipt Date', font=('Comfortaa', 20)), sg.Input(key='-RECEIPT_DATE-', tooltip='YYYY-MM-DD', font=('Comfortaa', 20)), sg.CalendarButton('Choose Date', target='-RECEIPT_DATE-', format='%Y-%m-%d', font=('Comfortaa', 20))],
        [sg.Text('Receipt Category', font=('Comfortaa', 20)), sg.Combo(categories, key='-RECEIPT_CATEGORY-', default_value='Shopping', font=('Comfortaa', 20))],
        [sg.Button('Add Receipt', font=('Comfortaa', 20)), sg.Button('View Last Receipt', font=('Comfortaa', 20)), sg.Button('View All Expenses', font=('Comfortaa', 20))]
    ]

    window_receipt = sg.Window('Add New Receipt', layout_receipt)

    layout_expenses = [
        [sg.Table(values=[['', '', '', '']], headings=['Category of Expense', 'Value in €', 'Name', 'Date'], auto_size_columns=False,
                  col_widths=[20, 10, 20, 12], justification='right', key='-EXPENSES_TABLE-', font=('Comfortaa', 15))],
        [sg.Text('Total Expenses by Category:', font=('Comfortaa', 20))],
        [sg.Multiline(size=(30, 8), key='-TOTAL_EXPENSES-', font=('Comfortaa', 15))],
        [sg.Button('Close', font=('Comfortaa', 20))]
    ]

    window_expenses = sg.Window('All Expenses', layout_expenses, finalize=True)
    expenses_table = window_expenses['-EXPENSES_TABLE-']
    total_expenses_text = window_expenses['-TOTAL_EXPENSES-']

    while True:
        event, values = window_receipt.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Add Receipt':
            name = values['-RECEIPT_NAME-']
            value = values['-RECEIPT_VALUE-']
            date = values['-RECEIPT_DATE-']
            category = values['-RECEIPT_CATEGORY-']

            if name and value and date and category:
                receipt = Receipt(name, value, date, category)
                user.add_receipt(receipt)
                sg.popup('Receipt added successfully!')

        if event == 'View Last Receipt':
            if user.receipts:
                last_receipt = user.receipts[-1]
                sg.popup(f'Last Receipt:\nName: {last_receipt.name}\nValue: {last_receipt.value}\nDate: {last_receipt.date}\nCategory: {last_receipt.category}')
            else:
                sg.popup('No receipts available.')

        if event == 'View All Expenses':
            if user.receipts:
                data = [[r.category, f"{r.value}€", r.name, r.date] for r in user.receipts]
                expenses_table.update(values=data)

                # Calculate total expenses by category
                total_expenses_by_category = {}
                for receipt in user.receipts:
                    if receipt.category in total_expenses_by_category:
                        total_expenses_by_category[receipt.category] += float(receipt.value)
                    else:
                        total_expenses_by_category[receipt.category] = float(receipt.value)

                # Display total expenses by category
                total_expenses_text.update(value='\n'.join([f'{category}: {total}€' for category, total in total_expenses_by_category.items()]))

    window_receipt.close()
    window_expenses.close()

if __name__ == '__main__':
    main()
