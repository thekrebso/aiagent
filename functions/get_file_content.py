import os
from functions.config import FILE_CHAR_LIMIT


def get_file_content(working_directory, file_path):
    try:
        absolute_path = os.path.realpath(
            os.path.join(working_directory, file_path))
        working_directory = os.path.realpath(working_directory)

        if not absolute_path.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(absolute_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(absolute_path, 'r') as file:
            content = file.read()

            if len(content) > FILE_CHAR_LIMIT:
                content = content[:FILE_CHAR_LIMIT]
                content += f'[...File "{file_path}" truncated at {FILE_CHAR_LIMIT} characters]'

            return content

    except Exception as e:
        return f'Error: {e}'
