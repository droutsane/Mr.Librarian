# MRLibrarian

MRLibrarian is a Telegram-based bot designed to make the process of issuing, managing, and tracking books in a library hassle-free. With this bot, users can:

- Issue books without visiting the library
- Search for book availability
- Track the books they have issued
- Get reminders for returning books
- Issue books peer-to-peer (P2P) with others in the same hostel

## Features

### 1. **Make Issuing Books Hassle-Free**
All books in the library have a unique code associated with them. Users can issue books by sending a message to the bot with the book code. The bot verifies the availability of the book and issues it to the user, eliminating the need to wait in long queues.

#### Key Points:
- Users can issue books by sending book codes to the bot.
- Each user is identified by their unique Telegram username to avoid fraudulent book issuance.

### 2. **Peer-to-Peer Book Issuing**
Users can issue books directly from peers (other users in the same hostel) without having to visit the library. The system maintains a record of who has the book, and users can find out which book is available through the bot.

#### Key Points:
- Users can search for the availability of books in a peer-to-peer system.
- The person issuing the book provides their Name, Scholar ID, and Hostel Room number.
- No need to visit the library to pick up or return books.

### 3. **Search for Book Availability**
The bot allows users to search for a book in the library database. It shows whether the book is available and, if not, who currently holds the book and for how long.

#### Key Points:
- Users can query the database for the availability of books.
- The bot provides the name of the person holding the book and the due date.

### 4. **Track Issued Books and Get Return Reminders**
The bot keeps a record of the books a user has issued, including the due date for returning them. A reminder will be sent a day before the due date to help users return books on time.

#### Key Points:
- Users can query to see the books they have issued.
- The bot provides the return date and an option to reissue or return the book.
- Reminders are sent a day before the return date.

## Backend Logic

- **Registration:** The bot registers users by asking them to provide their Telegram username, Name, Library ID, Scholar ID, and Hostel Room number. This information is stored securely in a database.
  
- **Database Management:** Each book has a unique code, and the bot keeps a record of who has issued each book and when it is due for return. The database is updated whenever a new book is issued or returned.

- **Telegram Integration:** Telegram usernames are used to ensure that each transaction is associated with the correct individual. The bot verifies users based on their Telegram username to avoid misuse.

- **Default Return Date:** Each issued book comes with a default return date, which can be adjusted based on user requests or system requirements. Users can only perform peer-to-peer (P2P) book transactions after the book’s return date has passed, unless the book is marked for submission earlier.

## Future Development

- **Python-Based:** The bot is written in Python 3, which is lightweight, easy to scale, and doesn't require any heavy frameworks. It can run locally on a terminal or be deployed on a Virtual Private Server (VPS) for 24/7 availability.
  
- **Scalable Architecture:** The backend is designed to be scalable. In the future, the same code can be reused to build a web or mobile application. The bot commands can be replaced with user interface elements (forms, buttons, etc.), with minimal changes required in the backend logic.

- **New Features:** Additional features can be added in the future, such as advanced searching, better user management, or integration with external systems like SMS notifications or email alerts.

## How to Use

1. **Register with the bot** by sending your Telegram username, Name, Library ID, Scholar ID, and Hostel Room number.
2. **Issue books** by sending the unique book code to the bot.
3. **Search for books** by querying the bot for availability.
4. **Track issued books** and get reminders about the return dates.

## Technologies Used

- Python 3
- Telegram Bot API
- SQLite (or another database solution) for storing book and user information
- VPS for hosting the bot (optional for larger-scale usage)

## Setup

1. Clone the repository: git clone <repository-url>
2. Install required Python packages: pip install -r requirements.txt
3. Set up your Telegram Bot via [BotFather](https://core.telegram.org/bots#botfather).
4. Configure the bot with your Telegram API token and database settings.
5. Run the bot: python bot.py


## Conclusion

MRLibrarian is an efficient and user-friendly solution for managing books in a library. By using Telegram as a platform, it offers a seamless experience without requiring additional apps or software. With its scalable design, it’s easy to extend or migrate to other platforms in the future.
For any issues or feature requests, please feel free to open an issue in the repository or contact the bot administrators.



