from setuptools import setup, find_packages
from typing import List

#Declearing variables for setup function
PROJECT_NAME = 'store-sales-predictor'
VERSION = '0.0.1'
AUTHOR = 'Sourav Mandal'
DESCRIPTION = 'This web app will be used to predict the sales of big-mart-store'
#PACKAGES = ['salespred']
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirements_list()
)

if __name__ == '__main__':
    print(get_requirements_list())

