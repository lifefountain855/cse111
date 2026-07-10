import csv
ERCOL='\033[35m'
RES='\033[0m'
BOLD='\033[1m'

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    with open(filename, "rt") as csvfile:
        new_dict={}
        reader = csv.reader(csvfile)
        next(reader)
        for row_list in reader:
            if len(row_list) !=0:
                new_dict[row_list[0]]=row_list[1]
    return new_dict

def find_student(students_dict):
    """Get an I-Number from the user, verify the I-Number is
    valid, and find and print the student with that I-Number."""
    inumber=input("Enter an I-number: ")
    inumber.replace("-",'')
    ilength = len(inumber)
    if ilength > 9: 
        if ilength < 13:
            return print(f"{ERCOL}{BOLD}Invalid I-number{RES}: {ERCOL}{inumber} has too many digits.{RES}")
        else: return print(f"{ERCOL}{BOLD}Invalid I-number{RES}: {ERCOL}{inumber[:13]}... has too many digits.{RES}")
    if ilength < 9: return print(f"{ERCOL}{BOLD}Invalid I-number{RES}: {ERCOL}{inumber} has too few digits.{RES}")
    if inumber.isdigit() == False: return print(f"{ERCOL}{BOLD}Invalid I-number{RES}")
    try:
        print(f"The student with the I-number {inumber} is {students_dict[inumber]}")
    except KeyError:
        print(f"{ERCOL}{BOLD}KeyError{RES}:{ERCOL} I-number '{inumber}' is not in dictionary or was typed incorrectly.{RES}")

def main():
    students=read_dictionary("students.csv")
    find_student(students)
    
if __name__ == "__main__":
    main()
