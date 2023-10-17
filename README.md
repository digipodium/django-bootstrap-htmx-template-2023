# Django Website Template 2023


[![Team digipodium](https://img.shields.io/badge/-digipodium-red?style=for-the-badge)](https://digipodium.com/)

<iframe src="https://ghbtns.com/github-btn.html?user=twbs&repo=bootstrap&type=star&count=true&size=large" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<iframe src="https://ghbtns.com/github-btn.html?user=mdo&type=follow&count=true&size=large" frameborder="0" scrolling="0" width="230" height="30" title="GitHub"></iframe>
<iframe src="https://ghbtns.com/github-btn.html?user=twbs&repo=bootstrap&type=fork&count=true&size=large" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>

![Django Logo](https://www.djangoproject.com/s/img/logos/django-logo-negative.png)

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Setup Virtual Environment](#setup-virtual-environment)
    - [Install Dependencies](#install-dependencies)
3. [Usage](#usage)
    - [Running the Development Server](#running-the-development-server)
    - [Creating Django Apps](#creating-django-apps)
4. [Contributing](#contributing)
5. [License](#license)

---

## Introduction

Django Website Template 2023 is a ready-to-use template for building websites using Django, Bootstrap 5, and Htmx. It provides a solid foundation with a preconfigured project structure and integrated frontend tools to accelerate web development.

This template saves you time by eliminating the need to set up the basic configurations, allowing you to focus on building your website's unique features.

---

## Installation

### Prerequisites

Before getting started, make sure you have the following dependencies installed:

- Python >= 3.10 (miniconda recommended for python)
- Basic knowledge of Python
- Basic knowledge of Django, Bootstrap, and Htmx


### Clone the Repository

Clone the repository or download the source code to your local machine.

```shell
git clone https://github.com/digipodium/django-bootstrap-htmx-template-2023.git
```

### Setup Virtual Environment

It is recommended to set up a virtual environment before installing the template's dependencies. Navigate to the project directory and create a new virtual environment.

```shell
cd django-bootstrap-htmx-template
```

### Install Dependencies

Activate the virtual environment and install the required dependencies.

```shell
pip install -r requirements.txt
```

---

## Usage

### Running the Development Server

To run the development server, execute the following command in your terminal:

```shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

By default, the server runs on `http://localhost:8000/`. Open this URL in your browser to access your Django website.

### Creating Django Apps

To create a new Django app within your project, use the following command:

```shell
python manage.py startapp app_name
```

Replace `app_name` with the desired name for your app. This command will create a new directory with the specified name, containing the necessary files and folders for a Django app.

---

## Contributing

Contributions are welcome! If you find any issues or have improvements to suggest, please feel free to submit a pull request or open an issue in this repository.

When contributing, please adhere to the following guidelines:
- Fork the repository and create a new branch for your changes.
- Write clear commit messages.
- Test your changes thoroughly.

---

## License

This Django website template is licensed under the [MIT License](https://opensource.org/licenses/MIT). Please refer to the `LICENSE` file for more details.