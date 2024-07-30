from setuptools import setup, find_packages

setup(
    name='ArtexTTS',
    version='0.0.5',
    author='Artex AI',
    description='A python text to speech library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JunaidParkar/Python-TTS',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'mtranslate==1.8',
        "pyttsx3==2.90"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://github.com/JunaidParkar/Python-TTS',
        'Source': 'https://github.com/JunaidParkar/Python-TTS',
        'Tracker': 'https://github.com/JunaidParkar/Python-TTS',
    },
)
