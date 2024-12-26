import pandas as pd
from Components.Gui import gui  
def read_data(data_name):
    df = pd.read_csv(f"Data/{data_name}.csv")
    return df.to_dict(orient='records')


def add_row(data_name, new_row):
    # Load the current CSV
    df = pd.read_csv(f"Data/{data_name}.csv")
    
    # Ensure new_row matches DataFrame columns
    new_row_df = pd.DataFrame([new_row])
    
    # Concatenate the new row
    df = pd.concat([df, new_row_df], ignore_index=True)
    
    # Save the updated DataFrame to the file
    df.to_csv(f"Data/{data_name}.csv", index=False)
    gui.print(f"Row added to {data_name} successfully!")

    
def delete_row(data_name, plate_number):
    # Load the current CSV
    df = pd.read_csv(f"Data/{data_name}.csv")

    # Check if the plate_number exists
    if plate_number not in df['plate_number'].values:
        gui.print(f"No record found with plate_number: {plate_number}")
        return

    # Filter out the row with the given plate_number
    df = df[df['plate_number'] != plate_number]

    # Save the updated DataFrame back to the file
    df.to_csv(f"Data/{data_name}.csv", index=False)
    gui.print(f"Row with plate_number {plate_number} deleted from {data_name} successfully!")