# Document Categorization Algorithm. This algorithm is a simple categorization based on the type of document. It utilizes a dictionary to categorize documents by their types. Time Complexity: O(n), where n is the number of documents.

from PIL import Image
import pytesseract

class Document: 
    def _init_(self, document_type, content):
        self.document_type = document_type
        self.content = content

class DocumentManager: 
    def _init_(self):
        self.documents = []

    def upload_document(self, document_type, content):
        document = Document(document_type, content)
        self.documents.append(document)

    def categorized_documents(self):
        categorized_documents = {}
        for document in self.documents:
            if document.document_type not in categorized_documents:
                categorized_documents[document.document_type] = []
            categorized_documents[document.document_type].append(document)
        return categorized_documents


# Expense Tracking Algorithm: This algorithm involves tracking expenses and generating report. The tracking algorithm appends expenses to a list, and the report generation sums up the total expenses. Time Complexity: O(n), where n is the number of expense.

class Expense:
    def _init_(self, date, vendor, amount, payment_method):
        self.date = date
        self.vendor = vendor
        self.amount = amount
        self.payment_method = payment_method

class ExpenseTracker:
    def _init_(self):
        self.expenses = []

    def track_expense(self, date, vendor, amount, payment_method):
        expense = Expense(date, vendor, amount, payment_method)
        self.expenses.append(expense)

    def generate_expense_report(self):
        total_expenses = sum(expense.amount for expense in self.expenses) 
        return {
            "Total_expenses": total_expenses,
            "Expenses": self.expenses
        }


# Receipt Scanning Algorithm (ReceiptApp): The receipt scanning algorithm uses Tesseract OCR to extract text from an image. It involves opening an image, performing OCR, and handling exceptions. The receipt processing algorithm extracts information from the receipt text. Time Complexity: Depends on the OCR library, but it can be considered as O(m), where m is the size of the image or text.

class Syr:
    def _init_(self):
        self.document_manager = DocumentManager()
        self.expense_tracker = ExpenseTracker()

    def scan_receipt(self, image_path):
        try:
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img)
            return text
        except Exception as e:
            print(f"Error scanning receipt: {e}") 
            return None

    def process_receipt(self, receipt_text):
        date, vendor, amount, payment_method = self.extract_info_from_receipt(receipt_text)

        # track the expense
        self.expense_tracker.track_expense(date, vendor, amount, payment_method)

        # upload and categorize the document
        self.document_manager.upload_document("Receipt", receipt_text)
        categorized_documents = self.document_manager.categorized_documents()

        return categorized_documents

    def extract_info_from_receipt(self, receipt_text):
        lines = receipt_text.split('\n')
        date = None
        vendor = None
        amount = None
        payment_method = None

        for line in lines:
            if "Date" in line:
                date = line.split(":")[1].strip()
            elif "Vendor" in line:
                vendor = line.split(":")[1].strip()
            elif "Amount" in line:
                amount = float(line.split(":")[1].strip())
            elif "Payment Method" in line:
                payment_method = line.split(":")[1].strip()

        if date is None or vendor is None or amount is None or payment_method is None:
            raise ValueError("Missing information in receipt")

        return date, vendor, amount, payment_method

# EXAMPLE:
syr_app = Syr()
receipt_path = "your_receipt_image.jpg"
receipt_text = syr_app.scan_receipt(receipt_path) 
if receipt_text:
    categorized_documents = syr_app.process_receipt(receipt_text)
    expense_report = syr_app.expense_tracker.generate_expense_report()
    print("Categorized documents: ")
    print(categorized_documents)
  
    print("\nExpense report:")
    print(expense_report)
else: 
    print("Error scanning receipt. Please check the image path.")
