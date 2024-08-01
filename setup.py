from typing import List
from setuptools import setup , find_packages


def getting_dep_from_requirements(path:str)->List[str]:
    '''it return all the dependencies written in requirements.txt'''
    list_of_dep=[]
    with open(path,'r') as file_obj:
        list_of_dep=file_obj.readlines()
        list_of_dep=[dep.replace("\n","") for dep in list_of_dep]
        if '-e .' in list_of_dep:
            list_of_dep.remove('-e .')
    return list_of_dep


setup(
    name='mlproject',
    version='0.0.1',
    description='Learning machine learning algorithms',
    author='sunny',
    author_email='kgpian@gmail.com',
    packages=find_packages(),
    install_requires=getting_dep_from_requirements('requirements.txt'),
)