import itertools
import random
import string
import timeit

import numpy as np

allowed_chars = string.ascii_lowercase
max_len = 32  #set the password lenght
max_len = max_len + 1
lenn = random.randint(2, max_len)
password = ''.join(random.choice(allowed_chars) for _ in range(lenn - 1))
def password_check(user_input):
    if len(user_input) == len(password):
        for idx, element in enumerate(password):
            if user_input[idx] != element:
                return False
    else:
        return False
    return True


def random_str(size):
    return ''.join(random.choices(allowed_chars, k=size))


def get_length() -> int:
    trials = 2000
    times = np.empty(max_len)
    for i in range(max_len):
        i_time = timeit.repeat(stmt='password_check(x)',
                               setup=f'x=random_str({i!r})',
                               globals=globals(),
                               number=trials,
                               repeat=10)
        times[i] = min(i_time)
    most_likely = int(np.argmax(times))
    return most_likely


def get_correct_password(length):
    guess = random_str(length)
    counter = itertools.count()
    trials = 1000
    while True:
        i = next(counter) % length
        for c in allowed_chars:
            alt = guess[:i] + c + guess[i + 1:]

            alt_time = timeit.repeat(stmt='password_check(x)',
                                     setup=f'x={alt!r}',
                                     globals=globals(),
                                     number=trials,
                                     repeat=10)
            guess_time = timeit.repeat(stmt='password_check(x)',
                                       setup=f'x={guess!r}',
                                       globals=globals(),
                                       number=trials,
                                       repeat=10)

            if password_check(alt):
                return alt

            if min(alt_time) > min(guess_time):
                guess = alt

            print(guess)


def main():
    length = get_length()
    print(f"Password has most likely length: ", length)
    input("ENTER TO CONTINUE")
    print("Wait...")
    password_cracked = get_correct_password(length)
    print(f"Cracked password: ", password_cracked)
    print(f"Generated password: ", password)


if __name__ == '__main__':
    main()
