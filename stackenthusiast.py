"""
StackEnthusiast

@author: Wiktor Wednesday 7 Feb 2018
"""
import mechanize
import credentialsSO

SO_cred = credentialsSO.credentials()


def open_stack(email, password):

    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Safari')]
    br.open("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
    br.select_form(nr = 1)
    br.form['email'] = email
    br.form['password'] = password
    sub = br.submit()

    print(sub.read())


def main():
    email = SO_cred.email
    password = SO_cred.password

    return open_stack(email, password)


if __name__ == '__main__':
    main()
