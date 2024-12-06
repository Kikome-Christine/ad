class SecureLoginSystem:
    def __init__(self, username, password):
        self._username = username  # Encapsulated attribute for username
        self._password = password  # Encapsulated attribute for password

    def validate_credentials(self):
        """Validate user credentials with abstraction for password validation."""
        return self._is_valid_username() and self._is_valid_password()

    def _is_valid_username(self):
        """Check if the username meets certain criteria."""
        return len(self._username) > 0  # Example: Username must not be empty

    def _is_valid_password(self):
        """Check if the password meets certain security criteria."""
        # Simulating a strong password check
        if len(self._password) >= 8 and any(char.isdigit() for char in self._password):
            return True
        return False

# Example usage
user = SecureLoginSystem("example_user", "secure_password123")
if user.validate_credentials():
    print("Login successful")
else:
    print("Invalid credentials")