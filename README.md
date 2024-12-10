# User Management System Documentation

## Overview
This is a Polish user management system written in Python. It supports operations like adding, removing, and editing users with validation checks for NIP, PESEL and REGON and ensures secure passwords.

## Installation

```
 git clone https://github.com/KubaloPL/user_management
 cd user_management
```

## Dependencies
- `json`: For JSON file handling
- `random`: For password generation
- `string`: For character set manipulations

## Configuration
- `DATA_PATH`: Directory for storing user data
- `USER_DATABASE_PATH`: Path to the users JSON database file

## Main Functions

### User Management

#### `add_user(user_data: dict)`
Adds a new user to the system after validating their information.

**User Data Template:**
```python
{ # Incremental
    "name": "Jan Kowalski",
    "nip": "1234567890",
    "pesel": "44051401458",
    "regon": "123456789",
    "password": "ZflaP2-0z<afVMZ,
    "status": "Registered"  # Can be "Registered" or "Removed", as string for further scalability
}
```

**Validation Checks:**
- PESEL number validation
- NIP number validation
- REGON number validation
- Password strength validation

**Returns:** 
- `True` if user is successfully added
- `False` if validation fails

#### `remove_user(user_id)`
Removes a user by:
- Clearing PESEL
- Clearing password
- Changing status to "Removed"

#### `edit_user(user_id: int, updated_data: dict)`
Edits user information for a specific user ID.

### Validation Functions

#### `validate_nip(nip: str)`
Validates the Polish Tax Identification Number (NIP)
- Checks length (10 digits)
- Performs checksum validation
- Returns `True` if valid, `False` otherwise

#### `validate_pesel(pesel)`
Validates the Polish Personal Identity Number (PESEL)
- Checks length (11 digits)
- Performs checksum validation
- Returns `True` if valid, `False` otherwise

#### `validate_regon(regon)`
Validates the Polish Business Registration Number (REGON)
- Supports 9 and 14-digit formats
- Performs checksum validation
- Returns `True` if valid, `False` otherwise

#### `validate_password(password, dontprint=None)`
Validates password strength
**Requirements:**
- Minimum 12 characters
- At least 1 digit
- At least 1 uppercase letter
- At least 1 lowercase letter
- At least 1 special character

### Password Generation

#### `generate_password()`
Generates a strong random password
- Uses a combination of ASCII letters, digits, and punctuation
- Ensures the generated password meets all validation criteria

## File Handling

### `save_users_to_file(users)`
Saves the current list of users to a JSON file

### `load_users_from_file()`
Loads users from the JSON file into the global `users` list

## Error Handling
The script provides detailed error messages in Polish for various validation failures, including:
- Invalid NIP
- Invalid PESEL
- Invalid REGON
- Weak password

## Usage Example
```python
# Adding a new user
new_user = {
    "name": "Jan Kowalski",
    "nip": "1234567890",
    "pesel": "44051401458",
    "regon": "123456789",
    "password": generate_password(),
    "status": "Registered"
}
add_user(new_user)

# Removing a user
remove_user(0)

# Editing a user
edit_user(1, {"name": "New Name"})
```

## Notes
- Ensure the `data/` directory exists before running the script
- The script uses a global `users` list for managing user data
- All operations require loading users from the file first

## Security Considerations
- Passwords are generated with strong randomness
- Multiple validation checks prevent invalid data entry
- User removal is soft-delete (status changed to "Removed")