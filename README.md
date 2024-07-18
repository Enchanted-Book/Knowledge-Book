<div align="center">
	<picture>
		<source media="(prefers-color-scheme: dark)" alt="Bookshelf" srcset="./docs/_imgs/banner.svg" width="600px">
		<img alt="Bookshelf" src="./docs/_imgs/	banner-light.png" width="600px">
	</picture>
</div>

<div align="center">
	<a href="https://enchanted-book.readthedocs.io/projects/fr/"><img alt="Static Badge" src="https://img.shields.io/badge/website-fr-ED2939?style=for-the-badge&labelColor=363a4f"></a>
	<a href="https://enchanted-book.readthedocs.io/projects/en/"><img alt="Static Badge" src="https://img.shields.io/badge/website-en-0052CC?style=for-the-badge&labelColor=363a4f"></a>
</div>

<br/>

<div align="center">
Greetings, curious friends, budding map makers, and apprentice data packers! Welcome to the Enchanted Book repository.
</div>

<br/>
<br/>

# 🧙‍♂️ Enchanted Book

Enchanted-Book is a repository aimed at providing resources and documentation for data pack enthusiasts. Whether you're new to Minecraft map making or looking to enhance your skills, this repository offers tools and guides to help you create magical experiences with data packs.

# 🛠️ Building the Documentation

To build the documentation locally, follow these steps:

## ⚙️ Install the required tools

Ensure Python (version 3.12 or higher) is installed:

1. Download Python from [Python's official website](https://www.python.org/downloads/).
2. After installing Python, navigate to the docs directory of your cloned Enchanted-Book repository.
3. Open a terminal (or PowerShell on Windows) and execute the following command:

```bash
pip install -r requirements.txt -U
```

This command installs necessary dependencies such as [Sphinx](https://www.sphinx-doc.org/en/master/) and [Myst Parser](https://myst-parser.readthedocs.io/en/latest/intro.html), which are essential for generating the documentation website from Markdown files.

## 🔨 Build the documentation

By default, the build language for make is set to French (fr). Adjust the LANGUAGE variable as needed.

- **On Unix-based systems (Linux/MacOS):**

```bash
make html LANGUAGE=<fr|en>
```

- **On Windows:**

```cmd
set LANGUAGE=<fr|en>
make.bat html
```

# 🤝 Contribution

We welcome contributions from anyone interested in improving Enchanted-Book! Please feel free to:

- Report issues for unexpected findings.
- Submit pull requests for improvements or new content.

Your contributions help enrich our repository and enhance learning opportunities for data pack enthusiasts.
