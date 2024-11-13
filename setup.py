from setuptools import setup, find_packages


setup(
    name='Automatic Job Applier',
    version='1.0.0',
    description='Automate Job Applications: Automatically apply to prioritized job listings on LinkedIn using your credentials.',
    author='John Rana',
    author_email='anujrana89114@gmail.com',
    license='MIT',
    packages=find_packages(),
    
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10'
    ]
)