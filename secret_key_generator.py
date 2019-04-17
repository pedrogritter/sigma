import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

#length = int(input("Insert size for key( must be int ): "))
secret_key = generate_key(length=64)

print(secret_key)
