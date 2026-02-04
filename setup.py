from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:
    """
    This function will return list of requirements

    :return:
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines= file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("my requirement.txt file not found" )

    return  requirement_lst
setup(
    name="NetworkSecurity",
    version='0.0.1',
    author='Damini Gupta',
    author_email="damini.gupta1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)



