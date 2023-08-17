import unittest
from io import StringIO
from contextlib import redirect_stdout
from ipaddress import IPv4Address
from one_ring import parse_cli_args, eight_bit_passwd, twelve_bit_passwd, create_table


class IPyPassTests(unittest.TestCase):

    def test_parse_cli_args(self):
        # Test with valid IP address
        args = ['--ip', '192.168.0.1']
        ip = parse_cli_args()
        self.assertIsInstance(ip, IPv4Address)
        self.assertEqual(str(ip), '192.168.0.1')

        # Test without IP address
        args = []
        with self.assertRaises(SystemExit):
            with self.assertRaises(argparse.ArgumentTypeError):
                parse_cli_args()

        # Test without IP address
        args = []
        ip = parse_cli_args()

def parse_cli_args():
    """
    Command line parser for IPv4 address of interest, with validation.

    Returns:
        IPv4 address as an instance of ipaddress.IPv4Address, or None if no IP address is provided.

    Raises:
        argparse.ArgumentTypeError: If the IP address is invalid.
    """

    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", action="store", type=ipaddress.IPv4Address,
                        required=False,
                        help="IP address of interest, e.g. 0.0.0.0")
    args = parser.parse_args()

    return args.ip if hasattr(args, 'ip') else None

self.assertIsNone(ip)

    def test_eight_bit_passwd(self):
        split_address = ['192', '168', '0', '1']
        password = eight_bit_passwd(split_address)
        self.assertEqual(password, '0*9*****')

    def test_twelve_bit_passwd(self):
        split_address = ['192', '168', '0', '1']
        password = twelve_bit_passwd(split_address)
        self.assertEqual(password, '0*13*168****')

    def test_create_table(self):
        ip_address = IPv4Address('192.168.0.1')
        expected_output = '8-bit    12-bit     \n-------- ------------\n0*9***** 0*13*168****\n'
        with redirect_stdout(StringIO()) as output:
            create_table(ip_address)
            self.assertEqual(output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
