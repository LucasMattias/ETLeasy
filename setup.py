from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ETLeasy",
    version="0.0.1",
    author="Lucas Mattias",
    author_email="lucasmattias@outlook.com.br",
    description="Pacote com ferramentas para facilitar o processo de ETL de dados",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LucasMattias/ETLeasy",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)
