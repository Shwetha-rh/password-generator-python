# password_generator.py
import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    pools = []
    if use_upper:   pools.append(string.ascii_uppercase)
    if use_lower:   pools.append(string.ascii_lowercase)
    if use_digits:  pools.append(string.digits)
    if use_symbols: pools.append(string.punctuation)

    if not pools:
        raise ValueError("Select at least one character type.")

    # ensure at least one from each selected pool
    password_chars = [random.choice(pool) for pool in pools]

    # fill the rest
    all_chars = "".join(pools)
    remaining = max(0, length - len(password_chars))
    password_chars += [random.choice(all_chars) for _ in range(remaining)]

    # shuffle for randomness
    random.shuffle(password_chars)
    return "".join(password_chars)

if __name__ == "__main__":
    print("🔐 Password Generator")
    try:
        length = int(input("Enter password length (e.g., 12): "))
        password = generate_password(length=length)
        print("\n✅ Your password:", password)
    except Exception as e:
        print("Error:", e)