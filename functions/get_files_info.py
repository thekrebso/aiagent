import os


def get_files_info(working_directory, directory="."):
    try:
        absolute_path = os.path.realpath(os.path.join(working_directory, directory))
        working_directory = os.path.realpath(working_directory)

        if not absolute_path.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(absolute_path):
            return f'Error: "{directory}" is not a directory'

        files = os.listdir(absolute_path)
        output = ''

        for file in files:
            if len(output) != 0:
                output += "\n"

            fullpath = os.path.join(absolute_path, file)
            output += f'{file}: file_size={os.path.getsize(fullpath)} bytes, is_dir={os.path.isdir(fullpath)}' 

        return output

    except Exception as e:
        return f'Error: {e}'
