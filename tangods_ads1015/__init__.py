from .ADS1015 import ADS1015


def main():
    import sys
    import tango.server

    args = ["ADS1015"] + sys.argv[1:]
    tango.server.run((ADS1015,), args=args)
