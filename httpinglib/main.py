"""
"""
# Imports
import random
import string

# Other script imports
import post
import get
import redirect
import flood

# Variables
url = input("Enter URL: ")
mode = input("Enter mode: ")

print(
    """
    Welcome to httping

    a) post
    b) get
    c) redirect test
    d) flood

    """
)
print(mode)
print(url)

if mode == 'a':
    post.postSend(url)
elif mode == 'b':
    get.getSend(url)
elif mode == 'c':
    redirect.postRedirect(url)
elif mode == 'd':
    flood.test(url)
else:
    print('Invalid Statement')
    exit(127)


def dataGen(size, type=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation):
    return ''.join(random.choice(type) for _ in range(size))

