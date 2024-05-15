# SMTP to Resend API requests converter

## Installation and running

1. Clone the repository
2. Create a .env file according to .env.sample with the following variables:
   - SECRET_KEY: The secret key for the application
   - RESEND_API_KEY: The Resend API key
   - SENDER: The sender's email address
3. Run the application using Docker

```bash
docker build -t stmp-to-resend-api .
docker run -p 8000:8000 stmp-to-resend-api
```

## Usage

The application is a FastAPI application. It listens for POST requests on the /forward-email endpoint. The request body should be a JSON object with the following fields:

- to: The recipient's email address
- subject: The email subject
- text: The email text
- html: The email HTML
- headers: Custom headers to add to the email

The application will forward the email to Resend using the Resend API key specified in the .env file.

Each request should bear Authorization header with a value in the format of `Bearer <SECRET_KEY>`.
