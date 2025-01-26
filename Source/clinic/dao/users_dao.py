import json
import hashlib

class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

class UserDAO:
    def __init__(self, json_file_path="users.json", autosave=False):
        """
        Initialize UserDAO with a path to the JSON file.
        """
        self.json_file_path = json_file_path
        self.autosave =autosave
        self.users = self.load_users()
        
        
        
        
    # Loading users from users.json   
    def load_users(self):
        try:
            with open(self.json_file_path, "r") as file:
                data = json.load(file)
                if "users" in data:
                    return [self.decode_user(user) for user in data["users"]]  ## !!
                else:
                    print("Invalid JSON format.")
                    return []
        except FileNotFoundError:
            print("Users JSON file not found.")
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON file.")
            return []




    def save_users(self):
        """
        Save users to the JSON file.
        """
        with open(self.json_file_path, "w") as file:
            json.dump({"users": [self.encode_user(user) for user in self.users]}, file, indent=4)  ## !! 

    def hash_password(self, password):
        """
        Hash a password using SHA-256.
        """
        return hashlib.sha256(password.encode()).hexdigest()
        
        
        
        
    def encode_user(self, user: User) -> dict:
        """
        Encode a User object to a dictionary.
        """
        return {
            "__type__": "User",
            "username": user.username,
            "password_hash": user.password_hash,
        }
        
        
        
        
    def decode_user(self, data: dict) -> User:
        """
        Decode a dictionary to a User object.
        """
        if "__type__" in data and data["__type__"] == "User":
            return User(data["username"], data["password_hash"])
        return None




    def add_user(self, username, password):
        """
        Add a new user to the database.
        """
        if any(user.username == username for user in self.users):
            print("User already exists.")
            return False
        hashed_password = self.hash_password(password)
        new_user = User(username, hashed_password)
        self.users.append(new_user)
        self.save_users()
        print("User " + str(username) + "added successfully.")
        return True




    def authenticate(self, username, password):
        hashed_password = self.hash_password(password)
        for user in self.users:
            print(f"Checking {user.username.lower()} against {username.lower()}")  # Debugging line
            if user.username.lower() == username.lower():
                print(f"Hashed Password: {hashed_password}, Stored Hash: {user.password_hash}")  # Debugging line
                return user.password_hash == hashed_password
        return False



