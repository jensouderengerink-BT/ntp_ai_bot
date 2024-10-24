import bcrypt

# Function to hash passwords
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to check if the password matches the stored hash
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Example user dictionary with hashed passwords
users = {
    "j.hek@ntp.nl": hash_password("i38Llf^^&ckCy4&S5U"),
    "jens@bluetree.nl": hash_password("5V$Ew!7Y@4J^wAQ3u8"),
}
