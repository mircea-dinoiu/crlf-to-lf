import os
import traceback


def __replace_in_file(file_path):
    try:
        file_in = open(file_path, 'r')
        file_contents = file_in.read()
        file_in.close()

        file_out = open(file_path, 'w', newline='\n')
        file_out.write(file_contents)
        file_out.close()
    except:
        traceback.print_exc()


def file_conversion(path):
    if os.path.isdir(path):
        for root, dirnames, filenames in os.walk(path):
            for filename in filenames:
                __replace_in_file(os.path.join(root, filename))
    else:
        __replace_in_file(path)
