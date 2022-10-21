"""Dictionary related utility functions."""

__author__ = "730563276"


from csv import DictReader
from tabulate import tabulate


# Define your functions below

def read_csv_rows(filename: str) -> list[dict[str, str,]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str,str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare tor ead the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    #Read each row of the CSV lin-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table_list:list[dict[str, str]], selected_column: str) -> list[str]:
    storage: list[str] = []
    for row in table_list:
        storage.append(row[selected_column])
    return storage


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    final_dict: dict[str, list[str]] = {}
    for row in row_table:
        for column in row:
            final_dict[column] = column_values(row_table, column)
    return final_dict


def head(data_table: dict[str, list[str]], row_number: int) -> dict[str, list[str]]:
    i = 0
    final_dict: dict[str, list[str]] = {}
    for row in data_table:
        for column in row:
            row_number_list: list[str] = []
            while i < row_number:
                row_number_list.append(column[i])
                i += 1
            final_dict[column] = row_number_list
    return final_dict