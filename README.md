# Python Socket Programming: TCP and UDP

Minimal client/server examples written while studying Computer Networks in the seventh semester of my B.Sc. in Computer Engineering. Author: Farzan Rahmani.

Both examples send a text message to a server, convert it to uppercase, and return the result. They illustrate the difference between TCP connections and UDP datagrams using Python's standard-library `socket` module.

## Programs

| Protocol | Server | Client | Port |
| --- | --- | --- | --- |
| TCP | `TCP/TCPServer.py` | `TCP/TCPClient.py` | 65432 |
| UDP | `UDP/UDPServer.py` | `UDP/UDPClient.py` | 12000 |

## Requirements and Address Configuration

Use Python 3; no third-party packages are required. The clients currently use the original development address, `172.25.96.1`. Before running them locally, set `serverName` in the selected client to `127.0.0.1`, or to the reachable address of the machine running the server. Server and client port values must match.

The servers bind to all local IPv4 interfaces. For a cross-machine test, ensure the selected address is reachable and the appropriate TCP/UDP port is allowed by the host firewall.

## Run an Example

From the repository root, start the TCP server in one terminal:

```sh
python TCP/TCPServer.py
```

After configuring the client address, run the client in a second terminal:

```sh
python TCP/TCPClient.py
```

Enter `hello world` when prompted; the expected response is `HELLO WORLD`. For UDP, run `UDP/UDPServer.py` and `UDP/UDPClient.py` in the same way. Stop either server with `Ctrl+C`.

## Implementation Notes

The TCP server handles one accepted connection at a time and performs one read of up to 1024 bytes. UDP uses datagrams of up to 2048 bytes. These are introductory examples: the clients have no timeout, and the TCP implementation does not add message framing, concurrent handling, or complete-send/read loops. Keep demonstration inputs short.

## License

See [LICENSE](LICENSE) for license terms.
