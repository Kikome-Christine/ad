class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role.lower()  # Normalize role to lowercase for consistency

    def can_access_sensitive_data(self):
        # Enforce least privilege by explicitly allowing only 'admin' access
        allowed_roles = ['admin']
        if self.role in allowed_roles:
            return True
        return False

    def __str__(self):
        # Provide a meaningful string representation for the user
        return f"User(username={self.username}, role={self.role})"


# Example Usage
if __name__ == "__main__":
    user1 = User('Alice', 'Admin')  # Admin user
    user2 = User('Bob', 'User')    # Regular user
    user3 = User('Eve', 'guest')   # Guest user

    # Check access for each user
    print(f"{user1}: Access Sensitive Data: {user1.can_access_sensitive_data()}")
    print(f"{user2}: Access Sensitive Data: {user2.can_access_sensitive_data()}")
    print(f"{user3}: Access Sensitive Data: {user3.can_access_sensitive_data()}")
