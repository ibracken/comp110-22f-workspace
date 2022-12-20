"""Dictionary related utility functions."""

__author__ = "730563276"


from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare tor ead the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV lin-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table_list: list[dict[str, str]], selected_column: str) -> list[str]:
    """Takes a data set and picks out a column."""
    storage: list[str] = []
    for row in table_list:
        storage.append(row[selected_column])
    return storage


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Takes a table of rows and turns it into columns."""
    final_dict: dict[str, list[str]] = {}
    for row in row_table:
        for column in row:
            final_dict[column] = column_values(row_table, column)
    return final_dict


def head(data_table: dict[str, list[str]], row_number: int) -> dict[str, list[str]]:
    """Picks out the first # of columns from the dataset."""
    final_dict: dict[str, list[str]] = {}
    for row in data_table:
        i: int = 0
        total_column: list[str] = data_table[row]
        row_number_list: list[str] = []
        while i < len(total_column) and i < row_number:
            row_number_list.append(total_column[i])
            i += 1
        final_dict[row] = row_number_list
    return final_dict


def select(constant_dict: dict[str, list[str]], moving_columns: list[str]) -> dict[str, list[str]]:
    """Picks out a certain number of columns from the dataset."""
    final_dict: dict[str, list[str]] = {}
    for column in moving_columns:
        final_dict[column] = constant_dict[column]
    return final_dict


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two columns into one."""
    final_dict: dict[str, list[str]] = {}
    for column in dict_1:
        final_dict[column] = dict_1[column]
    for column in dict_2:
        present: bool = False
        for new_column in final_dict:
            if new_column == column:
                present = True
                
        if present == True:        
            final_dict[column] += dict_2[column]
        else:
            final_dict[column] = dict_2[column]
    return final_dict


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list."""
    final_dict: dict[str, int] = {}
    for item in values:
        if item in final_dict:
            final_dict[item] += 1
        else:
            final_dict[item] = 0
    return final_dict