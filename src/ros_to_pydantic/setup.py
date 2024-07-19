from setuptools import find_packages, setup

package_name = 'ros_to_pydantic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ben Sembira',
    maintainer_email='ben.sembira.dev@gmail.com',
    description='Library for converting between ros and pydantic types',
    license='Apache License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ["test_script = ros_to_pydantic:main"],
    },
)
