from setuptools import setup, find_packages
import EntropyAnalysis as package

setup(
    name='EntropyAnalysis',
    version=package.__version__,
    py_modules=['EntropyAnalysis'],
    packages=find_packages(include=[]),
    install_requires=[],
    scripts=[],
    author="Maurice Lambert",
    author_email="mauricelambert434@gmail.com",
    maintainer="Maurice Lambert",
    maintainer_email="mauricelambert434@gmail.com",
    description='This package analyzes file entropy (shannon entropy) for forensic or malware analysis',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mauricelambert/EntropyAnalysis",
    project_urls={
        "Github": "https://github.com/mauricelambert/EntropyAnalysis",
        "Documentation": "https://mauricelambert.github.io/info/python/security/EntropyAnalysis.html",
        "Python Executable": "https://mauricelambert.github.io/info/python/security/EntropyAnalysis.pyz",
        "Windows Executable": "https://mauricelambert.github.io/info/python/security/EntropyAnalysis.exe",
    },
    download_url="https://mauricelambert.github.io/info/python/security/EntropyAnalysis.pyz",
    include_package_data=True,
    classifiers=[
        "Topic :: System",
        "Topic :: Security",
        "Environment :: Console",
        "Topic :: System :: Shells",
        'Operating System :: POSIX',
        "Natural Language :: English",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Topic :: System :: System Shells",
        'Operating System :: MacOS :: MacOS X',
        "Programming Language :: Python :: 3.8",
        'Operating System :: Microsoft :: Windows',
        "Topic :: System :: Systems Administration",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
    keywords=['entropy', 'entropy-analysis', 'malware-analysis', 'file-analysis', 'forensic', 'disk-analysis', 'security', 'cybersecurity'],
    platforms=['Windows', 'Linux', "MacOS"],
    license="GPL-3.0 License",
    entry_points = {
        'console_scripts': [
            'EntropyAnalysis = EntropyAnalysis:main'
        ],
    },
    python_requires='>=3.8',
)