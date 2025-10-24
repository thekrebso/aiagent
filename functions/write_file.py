import os


def write_file(working_directory, file_path, content):
    try:
        absolute_path = os.path.realpath(
            os.path.join(working_directory, file_path))
        working_directory = os.path.realpath(working_directory)

        if not absolute_path.startswith(working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        with open(absolute_path, 'w') as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'
