class User:
    def __init__(self, username, password, email=None):
        # Preconditions and encapsulation
        if not username or not isinstance(username, str):
            raise ValueError("Username must be a non-empty string.")
        if not password or not isinstance(password, str):
            raise ValueError("Password must be a non-empty string.")
        if email is not None and ('@' not in email or not isinstance(email, str)):
            raise ValueError("Email must contain '@' if provided.")

        self.__username = username
        self.__password = password
        self.email = email

    def authenticate(self, password):
        """Check if the password matches (encapsulated)."""
        return self.__password == password

    @property
    def username(self):
        return self.__username

# User storage
users = {}

def register(username, password, email=None):
    # Exception for duplicate usernames
    if username in users:
        raise Exception("Username '{}' already exists.".format(username))
    user = User(username, password, email)
    users[username] = user
    print(f"User '{username}' registered successfully.")

def login(username):
    max_attempts = 3
    if username not in users:
        print("User '{}' not found.".format(username))
        return
    user = users[username]
    for attempt in range(1, max_attempts + 1):
        pwd = input(f"Enter password for '{username}': ")
        if user.authenticate(pwd):
            print(f"Login attempt {attempt} for '{username}': Login successful! Welcome {username}.")
            break
        else:
            if attempt < max_attempts:
                print("Login attempt {} for '{}': Incorrect password, try again.".format(attempt, username))
                continue
            else:
                print(f"Login attempt {attempt} for '{username}': Login failed. Maximum attempts reached.")

# --- Sample Usage ---

# Registration
try:
    register(username="alice", password="pass123")
    register(username="bob", password="bobpass", email="bob@example.com")
except Exception as e:
    print(e)

print()

# Simulate login attempts for 'alice'
# For demonstration, we'll simulate input using a list instead of input()
login_attempts = iter(["wrongpass", "pass123"])

def mock_input(prompt):
    print(prompt, end='')  # Show the prompt
    return next(login_attempts)

# Patch input function for this demonstration
import builtins
original_input = builtins.input
builtins.input = mock_input

login("alice")

# Restore original input
builtins.input = original_input