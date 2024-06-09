from setuptools import setup, find_packages

setup(
    name='imageRenamer',
    version='0.1',
    packages=find_packages(),
    description='A script to rename image files based on predefined names and directory name.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jon Bachrach',
    author_email='jbny1@me.com',
    url='https://github.com/yourusername/imageRenamer',  # Replace with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
