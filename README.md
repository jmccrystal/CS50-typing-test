# Typing Test Application

## Overview

This application is a simple typing test game with a client-server architecture. Users can test their typing speed, save their scores, and view leaderboards. The application consists of a client-side GUI built with PySimpleGUI and a server-side Flask application for managing scores and banned initials.

## Features

- Typing test with randomized words
- Real-time timer and WPM (Words Per Minute) calculation
- Local and online leaderboards
- User initials validation
- Server-side score management

## Screenshots

Here are some screenshots of the application in action:

<img width="735" alt="Screenshot 2024-10-09 at 8 57 31 PM" src="https://github.com/user-attachments/assets/f870cfb8-0f00-4351-b286-dbfff7ef7335">

<img width="343" alt="Screenshot 2024-10-09 at 9 00 13 PM" src="https://github.com/user-attachments/assets/b2530d81-1ea3-466b-b5ef-efbf8ac94cda"> <img width="347" alt="Screenshot 2024-10-09 at 9 03 47 PM" src="https://github.com/user-attachments/assets/74209160-156b-43e9-bf7e-949e2687f897"> 

## Components

### Client-side

1. `main.py`: The main script that runs the client-side application.
2. `layouts.py`: Contains the GUI layouts for different windows.
3. `other_stuff.py`: Includes utility functions and variables.
4. `icons.py`: Stores icon data for GUI buttons.

### Server-side

1. `server.py`: Flask application for managing scores and banned initials.
2. `banned_initials.py`: List of banned initials.

## Setup and Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required packages:
   ```
   pip install PySimpleGUI requests Flask
   ```
3. Create a file named `server_ip.txt` in the same directory as `main.py` and add the IP address of your server.

## Running the Application

1. Start the server:
   ```
   python server.py
   ```
2. Run the client application:
   ```
   python main.py
   ```

## How to Play

1. Launch the application.
2. Type the displayed words as quickly and accurately as possible.
3. Press Enter or click the OK button when finished.
4. Enter your initials (2 or 3 letters) when prompted.
5. View your scores and the top 10 leaderboard.

## Technical Details

### Client-side

- The typing test uses PySimpleGUI for the graphical interface.
- Words are randomly selected from a predefined list stored in `words.pkl`.
- The application calculates WPM based on the time taken to complete the test.
- Scores are sent to the server and stored locally.

### Server-side

- The Flask server manages the online leaderboard and banned initials list.
- Scores are stored in `online_leaderboard.pkl` on the server.
- The server provides endpoints for adding scores, retrieving scores, and getting banned initials.

## File Descriptions

- `main.py`: Main client application script
- `layouts.py`: GUI layout definitions
- `other_stuff.py`: Utility functions and variables
- `icons.py`: Icon data for GUI buttons
- `server.py`: Flask server application
- `banned_initials.py`: List of banned initials
- `words.pkl`: Pickle file containing the word list for typing tests
- `online_leaderboard.pkl`: Pickle file storing the online leaderboard data
- `server_ip.txt`: Text file containing the server IP address

## Future Improvements
