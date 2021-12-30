"""
* Assignment: File Read Passwd
* Required: no
* Complexity: hard
* Lines of code: 100 lines
* Time: 55 min

English:
    1. Save listings content to files:
        a. `etc_passwd.txt`
        b. `etc_shadow.txt`
        c. `etc_group.txt`
    2. Copy also comments and empty lines
    3. Parse files and convert it to `result: list[dict]`
    4. Return list of users with `UID` greater than 1000
    5. User dict should contains data collected from all files
    6. Run doctests - all must succeed

Polish:
    1. Zapisz treści listingów do plików:
        a. `etc_passwd.txt`
        b. `etc_shadow.txt`
        c. `etc_group.txt`
    2. Skopiuj również komentarze i puste linie
    3. Sparsuj plik i przedstaw go w formacie `result: list[dict]`
    4. Zwróć listę użytkowników, których `UID` jest większy niż 1000
    5. Dict użytkownika powinien zawierać dane z wszystkich plików
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `from datetime import date`
    * `date.fromtimestamp(timestamp: int)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'username': 'watney',
      'uid': 1000,
      'gid': 1000,
      'home': '/home/watney',
      'shell': '/bin/bash',
      'algorithm': None,
      'password': None,
      'groups': ['astronauts', 'mars'],
      'last_changed': datetime.date(2015, 4, 25),
      'locked': True},
     {'username': 'lewis',
      'uid': 1001,
      'gid': 1001,
      'home': '/home/lewis',
      'shell': '/bin/bash',
      'algorithm': 'SHA-512',
      'password': 'tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50',
      'groups': ['astronauts', 'sysadmin', 'moon'],
      'last_changed': datetime.date(2015, 7, 16),
      'locked': False},
     {'username': 'martinez',
      'uid': 1002,
      'gid': 1002,
      'home': '/home/martinez',
      'shell': '/bin/bash',
      'algorithm': 'MD5',
      'password': 'SWlkjRWexrXYgc98F.',
      'groups': ['astronauts', 'sysadmin'],
      'last_changed': datetime.date(2005, 2, 11),
      'locked': False}]

      >>> from os import remove
      >>> remove(FILE_GROUP)
      >>> remove(FILE_SHADOW)
      >>> remove(FILE_PASSWD)
"""

from datetime import date
from os.path import dirname, join


BASE_DIR = dirname(__file__)
FILE_GROUP = join(BASE_DIR, 'etc-group.txt')
FILE_SHADOW = join(BASE_DIR, 'etc-shadow.txt')
FILE_PASSWD = join(BASE_DIR, 'etc-passwd.txt')


CONTENT_GROUP = """##
# `/etc/group` structure
#   - Group Name: from `/etc/passwd`
#   - Group Password: `x` indicates that shadow passwords are used)
#   - GID: Group ID
#   - Members: usernames from `/etc/passwd`
##

root::0:root
other::1:
bin::2:root,bin,daemon
sys::3:root,bin,sys,adm
adm::4:root,adm,daemon
mail::6:root
astronauts::10:watney,lewis,martinez
daemon::12:root,daemon
sysadmin::14:martinez,lewis
mars::1000:watney
moon::1001:lewis
nobody::60001:
noaccess::60002:
nogroup::65534:"""


CONTENT_PASSWD = """##
# `/etc/passwd` structure:
#   - Username
#   - Password: `x` indicates that shadow passwords are used
#   - UID: User ID number
#   - GID: User's group ID number
#   - GECOS: Full name of the user
#   - Home directory
#   - Login shell
##

root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
lewis:x:1001:1001:Melissa Lewis:/home/lewis:/bin/bash
martinez:x:1002:1002:Rick Martinez:/home/martinez:/bin/bash"""


CONTENT_SHADOW = """##
# `/etc/shadow` structure
#   - Username: from `/etc/passwd`
#   - Password
#   - Last Password Change: Days since 1970-01-01
#   - Minimum days between password changes: 0 - changed at any time
#   - Password validity: Days after which password must be changed, 99999 - many, many years
#   - Warning threshold: Days to warn user of an expiring password, 7 - full week
#   - Account inactive: Days after password expires and account is disabled
#   - Time since account is disabled: Days since 1970-01-01
#   - A reserved field for possible future use
#
# Password field (split by `$`):
#   - algorithm
#   - salt
#   - password hash
#
# Password algorithms:
#   - `1` - MD5
#   - `2a` - Blowfish
#   - `2y` - Blowfish
#   - `5` - SHA-256
#   - `6` - SHA-512
#
# Password special chars:
#   - ` ` (blank entry) - password is not required to log in
#   - `*` (asterisk) - account is disabled, cannot be unlocked, no password has ever been set
#   - `!` (exclamation mark) - account is locked, can be unlocked, no password has ever been set
#   - `!<password_hash>` - account is locked, can be unlocked, but password is set
#   - `!!` (two exclamation marks) - account created, waiting for initial password to be set by admin
##

root:$6$Ke02nYgo.9v0SF4p$hjztYvo/M4buqO4oBX8KZTftjCn6fE4cV5o/I95QPekeQpITwFTRbDUBYBLIUx2mhorQoj9bLN8v.w6btE9xy1:16431:0:99999:7:::
adm:$6$5H0QpwprRiJQR19Y$bXGOh7dIfOWpUb/Tuqr7yQVCqL3UkrJns9.7msfvMg4ZO/PsFC5Tbt32PXAw9qRFEBs1254aLimFeNM8YsYOv.:16431:0:99999:7:::
watney:!!:16550::::::
lewis:$6$P9zn0KwR$tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50:16632:0:99999:7:::
martinez:$1$.QKDPc5E$SWlkjRWexrXYgc98F.:12825:0:90:5:30:13096:"""

with open(FILE_GROUP, mode='w') as file:
    file.write(CONTENT_GROUP)

with open(FILE_PASSWD, mode='w') as file:
    file.write(CONTENT_PASSWD)

with open(FILE_SHADOW, mode='w') as file:
    file.write(CONTENT_SHADOW)

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

ALGORITHMS = {
    '1': 'MD5',
    '2a': 'Blowfish',
    '2y': 'Blowfish',
    '5': 'SHA-256',
    '6': 'SHA-512',
}

# list[dict]: joined data from all files for users with `UID` greater than 1000
result = ...
