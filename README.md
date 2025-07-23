
# CodeBlog1

**CodeBlog1** is a simple Django-based blog website. It includes a home page with a card and image, along with static pages like About and Contact. The blog section is structured to display blog posts, with templates ready for listing and detail views.

The project is built using Django’s template system and extends a base layout (`base.html`) for consistency. It uses Bootstrap for responsive styling, and static assets like images are served from the `static/images/` directory using Django's `{% static %}` template tag.

## Features

- Home page with a card and welcome image
- Static About and Contact pages
- Blog structure with placeholder views and templates
- Template inheritance using `base.html`
- Responsive design with Bootstrap
- Static file handling with Django’s `{% static %}`

## Tech Stack

- Django (Python)
- HTML5, CSS3, Bootstrap
- Django Templates

## Project Structure

```
CodeBlog1/
├── blog/
├── home/
│   └── templates/home/
│       ├── home.html
│       ├── about.html
│       └── contact.html
├── static/
│   └── images/
│       └── codeimage.jpg
└── templates/
    └── base.html
```

## Getting Started

1. Clone the repository
2. Set up a virtual environment
3. Run `python manage.py runserver`
4. Visit `http://localhost:8000/` to view the site

---
