# SMTP to Resend API requests converter

## Installation and running

1. Clone the repository
2. Create a .env file with the following variables:
   - SECRET_KEY: The secret key for the application
   - RESEND_API_KEY: The Resend API key
3. Run the application using Docker

```bash
docker build -t stmp-to-resend-api .
docker run -p 8000:8000 stmp-to-resend-api
```