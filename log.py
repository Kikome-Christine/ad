class SecureLoginSystem:
    def __init__(self, username, password):
        self._username = username  # Encapsulated attributes
        self._password = password

    def validate_credentials(self):
        # Abstraction for password validation
        if self._is_strong_password():
            return True
        return False

    def _is_strong_password(self):
        # Example of a strong password validation rule
        return len(self._password) >= 8 and any(char.isdigit() for char in self._password)

# Example usage
user = SecureLoginSystem("example_user", "secure_password123")
if user.validate_credentials():
    print("Login successful")
else:
    print("Invalid credentials")
