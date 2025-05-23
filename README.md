
---

## Cervical Spine Home Therapy App

### Core Principles:

1.  **User-Centric Design:** Easy navigation, large readable text, clear instructions.
2.  **Soothing Aesthetics:** Colors, shapes, and font chosen to create a calm, supportive environment.
3.  **Workflow-Driven:** Guiding the user step-by-step through their chosen therapy.
4.  **Accessibility:** High contrast, good font size, semantic HTML.

---

### Technology Stack:

*   **Backend:** Python 3 with Flask
*   **Database:** SQLite (for simplicity in development, easily upgradable to PostgreSQL/MySQL)
*   **Frontend:** HTML5, CSS3, Vanilla JavaScript
*   **ORM:** SQLAlchemy (integrated with Flask-SQLAlchemy)

---

### Project Structure:

```
cervical-therapy-app/
├── app.py                  # Main Flask application
├── config.py               # Configuration settings
├── models.py               # Database models
├── routes.py               # Defines application routes
├── static/
│   ├── css/
│   │   └── style.css       # All custom CSS
│   ├── js/
│   │   └── main.js         # Frontend JavaScript
│   └── images/             # Placeholder for organic shapes, icons, etc.
│       └── organic-shape-1.svg
│       └── organic-shape-2.svg
├── templates/
│   ├── base.html           # Base layout for all pages
│   ├── index.html          # Welcome/Home page
│   ├── signup.html         # Signup form
│   ├── therapy_selection.html # Choose therapy area
│   ├── therapy_intro.html  # Intro to a specific therapy workflow
│   ├── exercise_detail.html # Displays one exercise
│   ├── therapy_complete.html # Session completion
│   └── disclaimer.html     # Medical disclaimer page
└── venv/                   # Python Virtual Environment
├── requirements.txt        # Project dependencies
```

---
