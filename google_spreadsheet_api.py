import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('apidrive.json', scope)
gc = gspread.authorize(credentials)


def update_in_sheet(work_book_name, sheet_index, row, column, value):
    wks = gc.open(work_book_name)
    sheet = wks.worksheets()[sheet_index]
    sheet.update_acell(row + str(column), value)

def read_from_sheet(work_book_name, sheet_index, row_start_index, row_end_index):
    wks = gc.open(work_book_name)
    sheet = wks.worksheets()[sheet_index]
    no_of_rows = row_end_index - row_start_index
    required_values = []
    for i in range(no_of_products):
        row_number = i+product_list_start_row_index
        values = sheet.row_values(row_number)
        required_values.append(values)
    return required_values

