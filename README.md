# Baun Digital Library

The **Baun Digital Library** is a core component of the **Baun Eduvault**, an educational media repository designed for seamless access to educational resources. The Digital Library is built on the Django framework and comes integrated with an **AI Tutor** backend, making it a powerful tool for enhancing educational experiences.

## Features

- **AI Tutor Backend**: The Digital Library is powered by an AI-based tutor that assists in providing personalized educational content and guidance.
- **Educational Media Repository**: Stores a variety of educational resources, including textbooks, research papers, videos, and other media types.
- **Django Framework**: The entire system is designed using the Django web framework, ensuring scalability, security, and ease of development.
- **Seamless Integration with Baun Eduvault**: The library is a key part of the Baun Eduvault ecosystem, which is a purpose-built educational device aimed at improving the delivery of educational content.

## Installation

To get started with the Baun Digital Library, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/baun-eduvault/baunlib.git
   cd baunlib


2. **Set up a virtual environment & run**:
```bash
source env/bin/activate  (linux)
env\Scripts\activate (Windows)
pip install -r dev-requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python manage.py runserver
