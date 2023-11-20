from setuptools import setup, find_packages

setup(
    name='llm-linux-lib-explainer',
    version='0.1.0',
    url='https://github.com/yourusername/llm-linux-lib-explainer',
    author='Author Name',
    author_email='author@gmail.com',
    description='A project to explain specific Linux shared libraries using LLM API',
    packages=find_packages(),    
    install_requires=['openai', 'ctypes'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)