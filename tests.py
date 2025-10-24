from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file


print("Write to 'lorem.txt':")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("Write to 'pkg/morelorem.txt':")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print("Write to '/tmp/temp.txt':")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
