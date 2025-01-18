import csv
from fpdf import FPDF

# Step 1: Read and Analyze Data
def read_and_analyze_data(file_path):
    data = []
    total = 0
    count = 0

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            value = float(row[1])  # Assuming the second column contains numerical data
            data.append((row[0], value))  # First column: Name, Second column: Value
            total += value
            count += 1

    average = total / count if count > 0 else 0
    return header, data, total, average

# Step 2: Generate PDF Report
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Automated Report', align='C', ln=True)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def generate_pdf(header, data, total, average, output_file):
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    # Write Header
    pdf.cell(0, 10, "Data Analysis Report", ln=True, align='C')
    pdf.ln(10)  # Line break

    # Write Table Header
    for col in header:
        pdf.cell(40, 10, col, border=1, align='C')
    pdf.ln()

    # Write Data Rows
    for name, value in data:
        pdf.cell(40, 10, name, border=1)
        pdf.cell(40, 10, f'{value:.2f}', border=1, ln=True)

    pdf.ln(10)  # Line break

    # Write Summary
    pdf.cell(0, 10, f'Total: {total:.2f}', ln=True)
    pdf.cell(0, 10, f'Average: {average:.2f}', ln=True)

    # Save PDF
    pdf.output(output_file)
    print(f"PDF report generated: {output_file}")

# Main Function
if __name__ == "__main__":
    input_file = 'data.csv'  # Replace with your CSV file path
    output_file = 'report.pdf'

    # Read and analyze data
    header, data, total, average = read_and_analyze_data(input_file)

    # Generate PDF report
    generate_pdf(header, data, total, average, output_file)
