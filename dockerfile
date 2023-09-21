# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE config.settings
ENV DEBUG false
ENV EMAIL_HOST_USER sotoramirezaaron@gmail.com
ENV EMAIL_HOST_PASSWORD='tzfd kjfd igjs uasj'

# ENV DB_PORT 5432
# ENV DB_NAME appdb
# ENV DB_USER postgres
# ENV DB_PASSWORD akjln45bu4b5

# Create and set the working directory
WORKDIR /app/src/
COPY . .

# Copy the Pipfile and Pipfile.lock and install dependencies
RUN pip install -r requirements.txt

# Expose the port the application will run on
EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate

RUN python manage.py createsuperuser

# Command to run the application
CMD ["python", "manage.py", "runserver"]

