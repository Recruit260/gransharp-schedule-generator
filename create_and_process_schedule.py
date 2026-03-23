import pandas as pd

# Function to create an initial Excel file with sample data

def create_initial_file(filename):
    # Sample data for demonstration
    data = {
        'Employee Name': ['John Doe', 'Jane Smith', 'Emily Johnson'],
        'March Deduction': [100, 150, 200],
        'April Deduction': [110, 160, 220],
        'May Deduction': [120, 170, 240],
        'June Deduction': [130, 180, 260],
        'July Deduction': [140, 190, 280],
        'August Deduction': [150, 200, 300],
        'September Deduction': [160, 210, 320],
    }
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Initial file '{filename}' created successfully.")

# Function to process the Excel file and add balance calculations

def process_excel_file(filename):
    df = pd.read_excel(filename)
    # Calculate balances and add to dataframe
    df['Total Deductions'] = df[['March Deduction', 'April Deduction', 'May Deduction', 'June Deduction', \
                                   'July Deduction', 'August Deduction', 'September Deduction']].sum(axis=1)
    df['Balance'] = 1000 - df['Total Deductions']  # Assuming an initial balance of 1000
    df.to_excel(filename, index=False)
    print(f"File '{filename}' processed successfully with calculations.")

# Main execution
if __name__ == '__main__':
    initial_filename = 'employee_deduction_schedule.xlsx'
    create_initial_file(initial_filename)
    process_excel_file(initial_filename)
