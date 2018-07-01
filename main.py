import traceback
import os
import utils
from history import History


def hr():
    print('________________________________________________________________\n')


def run(history):
    hr()
    if history.length() > 0:
        history.print()
        read = input('\nEnter dir/file path or history index: ')

        try:
            index = int(read)
            if index in range(1, history.length() + 1):
                path = history.get(index - 1)
            else:
                print('The entered history index is invalid, please try again')
                return
        except ValueError:
            path = read
    else:
        path = input('\nEnter dir/file path: ')

    if os.path.exists(path):
        history.add(path)
        utils.file_conversion(path)
    else:
        print('The specified path doesn\'t exist, please try again')


try:
    historyInstance = History('.history')
    while True:
        run(historyInstance)
except KeyboardInterrupt:
    pass
except:
    traceback.print_exc()