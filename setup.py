from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        for line in f:
            if line.startswith(("#", HYPEN_E_DOT)):
                continue
            line = line.strip()
            if line.startswith(""):
                requirements.append(line.split())
            
        return requirements


setup(
    
    name='mlproject',
    version='0.0.1',
    author='Amit Maity',
    author_email='amit2maity@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)