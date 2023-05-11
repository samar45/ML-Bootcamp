from setuptools import setup,find_packages
from typing import List



HYPEN_E_dOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will retuen the list of requiremnets 
    '''
  
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_dOT in requirements:
            requirements.remove(HYPEN_E_dOT)

    return requirements


setup(
    name="src",
    version=0.01,
    author="samar",
    author_email="samarmohanty360@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages= find_packages()
)