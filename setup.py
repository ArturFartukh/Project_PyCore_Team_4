from setuptools import setup, find_packages

setup(
    name='dzvina_assist',
    version='0.0.1',
    description='Personal assistant',
    url='https://github.com/ArturFartukh/dzvina_assist',
    author='Go_IT Team-4',
    author_email='ar4ik.8933@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['dzvina=dzvina_assist.main:start']},
    # include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ]
)
