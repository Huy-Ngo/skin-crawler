import os
import json
from pathlib import Path


def validate():
    '''
    Abilities:
        This function check for the existence of
        package kaggle and api token file.

        Api token file is expected to have this path ~/.kaggle/kaggle.json
        Package kaggle is expected to install with pip

        This also prints what is missing to stdout.
    Returns:
        True : if package kaggle and api token file exits
        False : else
    '''
    found = True
    try:
        import kaggle  # noqa: F401
    except ModuleNotFoundError:
        found = False
        print('Kaggle is not found')

    token_fpath = os.path.join(Path().home(), Path('.kaggle/kaggle.json'))

    if os.path.isfile(token_fpath):
        token = json.load(open(token_fpath, 'r'))
        if 'username' in token and 'key' in token:
            pass
        else:
            found = False
            print('Kaggle API Token format is invalid')
    else:
        found = False
        print('Kaggle API Token file is not found')

    return found


if __name__ == '__main__':
    print(validate())
