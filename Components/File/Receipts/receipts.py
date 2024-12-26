def new_receipt (check_out_data:dict):
    file_path = f"Receipts/{check_out_data["owner_name"]} _ {check_out_data["plate_number"]} _ {check_out_data["check_out_date"].replace(":", "-")}.txt"

    display_keys_array = [key.replace('_', ' ') for key in check_out_data.keys()]
    display_values_array = [value for value in check_out_data.values()]

    with open(file_path, "w") as file:
        file.write("--Receipt--\n")

        for i in range(len(check_out_data)):
            file.write(f"{display_keys_array[i]}: {display_values_array[i]}\n")



