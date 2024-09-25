# CloudVault


This project was created with the purpose of providing storage for files, specifically images and videos in certain formats. It complements a script I created to convert .HEIC files to .JPG and .MOV files to .MP4, as these are not conventional types and are just for iOS devices, I wanted to migrate them and convert them easily but storing the entire memory of my iPhone was a challenge. The goal is to offer a simple service for file storage without unnecessary requirements or the need for payments on other platforms. It is a straightforward solution for anyone in need of efficient file storage without difficulties. This project was made for educational purposes so it might no be as polished as other APIs.


## 1. Features

- RESTful API built with Django REST Framework.
- User authentication with Django Allauth.
- Upload and management of multimedia files.
- Documentation with CoreAPI.
- Seeding with Django-seed.
- Tests using Django's TestCase. (Covering serializers, views, models, URLs)
- CRUD Operations: Complete Create, Read, Update, Delete functionality for managing multimedia files.


## 2. Stack

- Django.
- Django REST Framework.
- Docker.
- PostgreSQL.
- CoreAPI.

## 3. Installation

### Clone the repository:

   ```bash
   git clone https://github.com/antyep/cloudvault_api.git
   cd cloudvault_api
  ```

### Create a virtual environment and activate it using the following commands:

This is not a must if you are considering using Docker.

For Linux:

   ```bash
    python3 -m venv venv
    source venv/bin/activate    
  ```
For Windows:

   ```PowerShell
    python3 -m venv venv
    source venv/Scripts/activate  
  ```

To deactivate the virtual environment type this command in your terminal:

   ```bash
    deactivate  
  ```

### Install the dependencies:

   ```bash
    pip install -r requirements.txt
  ```

### Build the image and run Docker container:

Make sure Docker Desktop is running.

   ```bash
   docker-compose up --build
  ```

Once Docker is running, the API is accessible on port 8000. It is not necessary to execute the "runserver" command, but you must create the superuser first.

### Create superuser:

  ```bash
    docker-compose exec web python manage.py createsuperuser
  ```

You will be prompted to enter username, email, and password, here is how you should see it:

  ```bash
    username: your_username
    email: example@example.com
    password: password
    password(again): invisible password # You will not be able to see it.
  ```

Make sure to replace the placeholders with your own information.

Once the superuser is created you could access to the admin site by the following URL:

http://localhost:8000/admin/

## 4. Usage

### Endpoints (Admin)

#### List All Media

- __Request:__
  - __Method:__ GET
  - __URL:__ `http://localhost:8000/admin/api/media/`
 
#### Get Media by ID

- __Request:__
  - __Method:__ GET
  - __URL:__ `http://localhost:8000/admin/api/media/{id}/`

- __Response:__
  - Returns a list of all media files in JSON format.

#### List all users

- __Request:__
  - __Method:__ GET
  - __URL:__ `http://localhost:8000/admin/api/customuser/`

#### Delete Media

- __Request:__
  - __Method:__ DELETE
  - __URL:__ `http://localhost:8000/admin/api/media/{id}/delete`
  - 

#### Create Media

- __Request:__
  - __Method:__ POST
  - __URL:__ `http://localhost:8000/api/media/`
  - __Body:__ (example)
    ```json
    {
      "title": "Sample Image",
      "description": "A sample image file.",
      "media_file": "image.jpg",
      "file_type": "jpg/mp4",
      "user": "id"
      "is_public": false,
      "is_deleted": false
    }
   

## 5. Future Improvements

File Search Functionality: Implementing search capabilities to easily find stored files.
User Profile Management: Allowing users to manage their profiles and profile pictures.
Enhanced File Format Support: Supporting additional file formats for upload and conversion.
Integration with Cloud Storage Services: Providing options for users to directly upload files to Cloud Storage providers.
Social Login and Registration: Implementing various methods to log in or sign up using Gmail, GitHub, or other services.
Frontend Interface: Developing a user-friendly frontend interface to interact with the API for a better user experience.
Token Verification: Implementing robust token verification to ensure secure access to the API. This process involves validating the authenticity of tokens on each request, preventing unauthorized access, and protecting sensitive data. Users will be required to provide a valid token in the authorization header for all requests to ensure that only authenticated users can interact with the API.


## Contact

Feel free to contact me through: antyep6@gmail.com.


