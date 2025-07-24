# Data Project Starter Kit

## About the Project

This is a repository to reinforce how to build a basic project structure in Data Engineering, including folder classifications, best practices, and some interesting libraries to use.

### Workshop Objectives:

* **Understand standard project structure**: This includes organizing directories such as source code, tests, documentation, and more.

* **Standard structures in data projects**: We will refactor the project using classes, modules, and best practices in an ETL pipeline.

* **Get familiar with development tools**: We will cover the use of virtual environments and discuss tools like PIP, CONDA, and POETRY.

* **Testing with Pytest**: Ensure your code works as expected by creating unit and integration tests.

* **Version control with Git and GitHub**: Learn how to version your project and use GitHub for collaboration and publishing.

* **Documentation with MKDocs**: You'll learn how to document your project with MKDocs and publish it on [GitHub Pages](https://lvgalvao.github.io/DataProjectStarterKit/)

* **Automation and CI/CD**: Set up continuous integration and delivery routines to maintain project quality.

---

## Getting Started

### Prerequisites

* **VSCode**: This is the code editor we’ll use during the workshop. [VSCode installation instructions here](https://code.visualstudio.com/download).

* **Git and GitHub**:

1. You must have Git installed on your machine. [Git installation instructions here](https://git-scm.com/book/en/v2).
2. You also need a GitHub account. [GitHub account setup instructions here](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account).
3. For Windows users, we recommend this video: [YouTube](https://www.youtube.com/watch?v=_hZf1teRFNg).
4. Basic Git and GitHub tutorial [Ebook](https://www.linkedin.com/feed/update/urn:li:activity:7093915148351864832/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7093915148351864832%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=4GUdvXH4TK%2BtZtlNHmiqJA%3D%3D).
5. If you're already familiar with Git, check out this video by Akita: [YouTube](https://www.youtube.com/watch?v=6Czd1Yetaac).

* **Pyenv**: Used to manage different Python versions. [Pyenv installation instructions here](https://github.com/pyenv/pyenv#installation). We'll use Python 3.11.3 for this project. For Windows users, this tutorial is recommended: [YouTube](https://www.youtube.com/watch?v=TkcqjLu1dgA).

* **Poetry**: This project uses Poetry for dependency management. [Poetry installation instructions here](https://python-poetry.org/docs/#installation). For Windows users, this video is helpful: [YouTube](https://www.youtube.com/watch?v=BuepZYn1xT8). It covers Python, Poetry, and VSCode setup. But a simple `pip install poetry` also works.

**Suggested reading:**  
[Ebook 1 - Testing](https://www.linkedin.com/feed/update/urn:li:activity:7099722252144848896/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7099722252144848896%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=hg1%2BufBeTLClrS%2BJixGEoA%3D%3D)  
[Ebook 2 - GitHub Actions](https://www.linkedin.com/feed/update/urn:li:activity:7098264928553201665/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7098264928553201665%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=%2BFcdPRcDT62iNieFV3Yc%2Fg%3D%3D)  
[Ebook 3 - "It works on my machine"](https://www.linkedin.com/feed/update/urn:li:activity:7095419109449814017/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7095419109449814017%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=7ShpQeNCQuCDErI%2BAzEBXw%3D%3D)

---

### Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/lvgalvao/dataprojectstarterkit.git
cd dataprojectstarterkit
```

2. Set the correct Python version with pyenv:

```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

3. Configure Poetry to use Python 3.11.5 and activate the virtual environment:

```bash
poetry env use 3.11.5
poetry shell
```

4. Install the project dependencies:

```bash
poetry install
```

5. Run the tests to make sure everything is working properly:

```bash
task test
```

6. Run the command to view the project documentation:

```bash
task doc
```

7. Run the ETL pipeline:

```bash
task run
```

8. Check the data/output folder to confirm that the file was generated correctly.