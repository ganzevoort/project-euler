"""
Each character on a computer is assigned a unique code and the
preferred standard is ASCII (American Standard Code for Information
Interchange). For example, uppercase A = 65, asterisk (*) = 42, and
lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to
ASCII, then XOR each byte with a given value, taken from a secret key. The
advantage with the XOR function is that using the same encryption key
on the cipher text, restores the plain text; for example, 65 XOR 42 =
107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep
the encrypted message and the encryption key in different locations,
and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than
the message, which is likely, the key is repeated cyclically throughout
the message. The balance for this method is using a sufficiently long
password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three
lower case characters. Using cipher.txt (right click and 'Save Link/Target
As...'), a file containing the encrypted ASCII codes, and the knowledge
that the plain text must contain common English words, decrypt the
message and find the sum of the ASCII values in the original text.

"""


import itertools


def decrypt(encrypted, password):
    pw_repetitions = (len(encrypted)-1) // len(password) + 1  # round up
    secret_key = (password * pw_repetitions)[:len(encrypted)]
    decrypted = [(a^b) for (a,b) in zip(encrypted, secret_key)]
    #print 'decrypt',
    #print stringify(encrypted)[:23],
    #print stringify(secret_key)[:23],
    #print stringify(decrypted)[:23]
    return decrypted


def stringify(intlist):
    return ''.join(chr(c) if 32<=c<127 else '*' for c in intlist)


# https://en.wikipedia.org/wiki/Most_common_words_in_English
common_words = """
    the be to of and a in that have I
    it for not on with he as you do at
    this but his by from they we say her she
    """.split()

lowercase = list(map(ord, "abcdefghijklmnopqrstuvwxyz"))
def all_passwords(N):
    cwr = list(itertools.combinations_with_replacement(lowercase, N))
    return cwr


def find_password(N, encrypted):
    found_password = []
    for x in range(N):
        subset = list(itertools.islice(encrypted, x, None, 3))
        for password in all_passwords(1):
            attempt = decrypt(subset, password)
            if not all(32<=c<127 for c in attempt):
                continue
            normal_count = len([c for c in attempt if c==32 or c in lowercase])
            if normal_count > 0.9 * len(attempt):
                #print x, stringify(password), stringify(attempt), \
                #        normal_count
                found_password.extend(password)
                break
        else:
            die  # no password found
    return found_password

def solution(N=3):
    encrypted = list(map(int, open('p059_cipher.txt').read().strip().split(',')))
    password = find_password(N, encrypted)
    decrypted = decrypt(encrypted, password)
    #print stringify(password), stringify(decrypted)
    return sum(decrypted)

if __name__ == '__main__':
    import pdb; pdb.set_trace()
    print(solution())
