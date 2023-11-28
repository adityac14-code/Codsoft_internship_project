from setuptools import setup, find_packages

setup(
    name='titanic-survival-predictor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn'
        
    ],
    author='Chitte Aditya',
    author_email='chitteaditya1@gmail.com',
    description='Predicting Titanic Passenger Survival',
    url='https://github.com/adityac14-code/Titanic-Prediction',
    
)