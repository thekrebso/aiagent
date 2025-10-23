from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info

print("Result for 'main.py' file:")
print(get_file_content("calculator", "main.py"))

print("\nResult for 'pkg/calculator.py' file:")
print(get_file_content("calculator", "pkg/calculator.py"))

print("\nResult for listing files in 'pkg' directory:")
print(get_file_content("calculator", "/bin/cat"))

print("\nResult for non-existing file:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
