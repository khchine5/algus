from setuptools import setup
filename = 'lino_algus/setup_info.py'
exec(compile(open(filename, "rb").read(), filename, 'exec'))

if __name__ == '__main__':
    setup(**SETUP_INFO)
