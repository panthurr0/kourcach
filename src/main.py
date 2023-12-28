from utils import print_requisites, sorted_with_date, executed_files
from config import DATA


def main():
    operations_data = executed_files(DATA)
    sorted_operations = sorted_with_date(operations_data)
    print_requisites(sorted_operations)


main()
