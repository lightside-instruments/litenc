# litenc

A lightweight NETCONF session framer for Python. The API provides `connect`,
`send`, `receive`, `close`, and a convenience `rpc` operation. It gives callers
control over NETCONF messages without validating the protocol data units.

## Installation

```sh
python -m pip install litenc
```

Requires Python 3.7 or newer. Paramiko and lxml are installed automatically.
The distribution includes the `litenc` and `litenc_lxml` Python packages and
the `ncget` command.

## Usage

```python
from litenc.litenc import litenc

session = litenc()
if session.connect(server="router.example.com", user="admin", password="secret") == 0:
    try:
        session.send('<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">'
                     '<capabilities><capability>urn:ietf:params:netconf:base:1.0</capability>'
                     '</capabilities></hello>')
        status, hello = session.receive()
    finally:
        session.close()
```

Use `ncget --verbose-session` to log all sent and received NETCONF messages
to stderr while keeping the result on stdout. For command options, run
`ncget --help`. Network-wide tools are available in
the separate `tntapi` distribution.

[Source and issue tracker](https://github.com/vlvassilev/litenc)

## License

BSD-3-Clause. See LICENSE and COPYRIGHT for the license and copyright notices.
