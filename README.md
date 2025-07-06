
# Portfolio Website

A modern, responsive portfolio website built with Django, showcasing my development projects and skills.

## 🚀 Features

- **Responsive Design**: Optimized for all devices (desktop, tablet, mobile)
- **Modern UI**: Clean, professional design with smooth animations
- **Project Showcase**: Display of various development projects with descriptions
- **Contact Form**: Functional contact form with email integration
- **Demo Videos**: Dedicated section for project demonstrations
- **Deployed Projects**: Links to live project deployments

## 🛠️ Tech Stack

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5, Custom CSS
- **Email**: SMTP integration with Gmail
- **Static Files**: WhiteNoise for static file serving
- **Database**: SQLite (development)

## 📁 Project Structure

```
main/
├── main/                   # Django project settings
│   ├── settings.py        # Main configuration
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI configuration
├── portfolio_app/         # Main application
│   ├── static/           # Static files (CSS, images)
│   ├── templates/        # HTML templates
│   ├── views.py          # View functions
│   └── urls.py           # App URL patterns
├── staticfiles/          # Collected static files
└── manage.py            # Django management script
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Django 5.2.4
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd portfolio-website
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Navigate to project directory**
   ```bash
   cd main
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver 0.0.0.0:5000
   ```

7. **Open your browser**
   Navigate to `http://localhost:5000`

## 📧 Email Configuration

To enable the contact form functionality:

1. **Gmail Setup**:
   - Enable 2-factor authentication on your Gmail account
   - Generate an app-specific password
   - Update `settings.py` with your credentials:

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## 🎨 Customization

### Adding New Projects

1. **Update the home template** (`portfolio_app/templates/portfolio_app/home.html`)
2. **Add project images** to `portfolio_app/static/portfolio_app/images/`
3. **Update project descriptions** in the projects section

### Styling

- **Main styles**: `portfolio_app/static/css/style.css`
- **Bootstrap**: Integrated via CDN
- **Fonts**: Google Fonts (Poppins, Fira Code)

## 📱 Pages & Endpoints

### Available Routes

| Route | Method | Description | Template |
|-------|--------|-------------|----------|
| `/` | GET | Main landing page with hero section, about, skills, and projects | `home.html` |
| `/contact/` | GET, POST | Contact form with email functionality | `contact.html` |
| `/demo-videos/` | GET | Video demonstrations of projects | `demo_videos.html` |
| `/deployed-projects/` | GET | Links to live deployments | `deployed_projects.html` |

### Request/Response Structure

#### Contact Form Submission

**Endpoint:** `POST /contact/`

**Request Headers:**
```
Content-Type: application/x-www-form-urlencoded
X-CSRFToken: [Django CSRF Token]
```

**Request Body:**
```
name=John+Doe&
email=john.doe@example.com&
subject=Project+Inquiry&
message=Hello%2C+I+would+like+to+discuss...&
csrfmiddlewaretoken=[token]
```

**Form Fields:**
- `name` (string, max 100 chars): Sender's full name
- `email` (email): Sender's email address
- `subject` (string, max 200 chars): Email subject
- `message` (text): Message content
- `csrfmiddlewaretoken` (string): Django CSRF protection token

**Response:**
- **Success (302)**: Redirect to `/contact/` with success message
- **Error (200)**: Returns form with validation errors
- **Server Error (500)**: Email sending failure

**Email Template Sent:**
```
Subject: Portfolio Contact: [subject]

New contact form submission:

Name: [name]
Email: [email]
Subject: [subject]

Message:
[message]
```

#### Static File Requests

**CSS Files:**
- `/static/css/style.css` - Main stylesheet
- `/static/admin/css/...` - Django admin styles

**Image Assets:**
- `/static/portfolio_app/images/profile.jpg` - Profile picture
- `/static/portfolio_app/images/[project].jpg` - Project screenshots
- `/static/portfolio_app/images/...` - Other image assets

### Django Views Structure

```python
# Main views in portfolio_app/views.py
def home(request):          # GET /
def contact(request):       # GET, POST /contact/
def demo_videos(request):   # GET /demo-videos/
def deployed_projects(request): # GET /deployed-projects/
```

### Form Validation

**ContactForm Fields:**
```python
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
```

**Validation Rules:**
- Name: Required, max 100 characters
- Email: Required, valid email format
- Subject: Required, max 200 characters
- Message: Required, textarea input

## 🔧 Configuration

### Environment Variables

For production deployment, consider using environment variables for sensitive data:

```python
import os
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD', 'your-email-password')
```

### Debug Mode

- **Development**: `DEBUG = True`
- **Production**: `DEBUG = False`

## 📦 Dependencies

Key packages used in this project:

```
Django==5.2.4
whitenoise==6.5.0
gunicorn==21.2.0
```

## 🚀 Deployment

This project is configured for deployment on Replit:

1. **Automatic deployment** via `.replit` configuration
2. **Static files** served with WhiteNoise
3. **Database migrations** run automatically
4. **Production server** using Gunicorn

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

- **Email**: anishde0950@gmail.com
- **Portfolio**: [Your Portfolio URL]
- **GitHub**: [Your GitHub Profile]

## 🎯 Future Enhancements

- [ ] Add blog functionality
- [ ] Implement user authentication
- [ ] Add project filtering and search
- [ ] Integrate with CMS for dynamic content
- [ ] Add analytics and tracking
- [ ] Implement dark/light theme toggle

---

⭐ **Star this repository if you found it helpful!**
