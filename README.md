# BookStore-API

Advanced Bookstore API with User Authentication and ReviewsObjective: Create a RESTful API for managing a bookstore with user authentication and review functionality.

Architecture Design: Use the Model-View-Serializer (MVS) architecture with Django's built-in authentication system.
## Functionality:
### Models:
- Book (title, author, genre, published date, ISBN).
- UserProfile (user, bio, profile picture).
- Review (book, user, rating, content).
### Features:
- Implement user registration and login using JWT authentication.
- Create viewsets for books and reviews.
- Allow users to create reviews for books they have read, including a rating system (1-5 stars).
- Implement permissions so that only authenticated users can create or edit reviews.
- Add filtering capabilities to retrieve books by genre or autho
