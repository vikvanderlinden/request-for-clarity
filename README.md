# RFC: Request For Clarity

Small tool to probe the dependencies of RFC's (obsoletes, obsoleted by, updates, updated by) and automatically download them.

## Run

Just `python3 ./src/main.py` from repo root.

### Listing dependencies

To show the dependencies for a certain RFC, enter the number:

```
RFC to search: 793

| - RFC761 - DoD standard Transmission Control Protocol
> RFC793 - Transmission Control Protocol
| + RFC1122 - Requirements for Internet Hosts - Communication Layers
| | + RFC1349 - Type of Service in the Internet Protocol Suite

... (other output) ...

| + [P] RFC3168 - The Addition of Explicit Congestion Notification (ECN) to IP
| + [P] RFC6093 - On the Implementation of the TCP Urgent Mechanism
| + RFC6528 - Defending against Sequence Number Attacks
```

The line with '>' is the RFC requested. Before this line is the history, after it the future (relative to the requested RFC). A '-' in front of an RFC means it was obsoleted by (history) or obsoletes (future) the RFC. A '+' means it was updated by (history) or updates (future) the RFC.

For some lines, a '[P]' will be shown at the beginning. This means the children of that RFC have been shown previously in the output and they are not repeated.

So in the example above:

* RFC793 obsoletes RFC761
* RFC793 is updated by RFCs 1122, 3168, 6093, 6528
* RFC1122 is on its turn updated by RFC1349 (and others, not shown)
* RFCs 3168 and 6093 have already been processed before ('[P]'; this means somewhere in the 'other output' part, so they have multiple dependencies in the full tree) and therefore their children are not repeated

### Downloading

To download an RFC, add a '+' or '*' in front of the RFC number:

```
RFC to search: +793

File downloaded as 793_transmission-control-protocol.pdf
```

A '+' downloads a file if it is available (not all RFCs have PDFs) and '*' combines the listing and downloading (it does both).

### Limiting search depth

To limit the depth of dependencies, add the maximum depth after a colon to the number:

```
RFC to search: 793:1

| - RFC761 - DoD standard Transmission Control Protocol
> RFC793 - Transmission Control Protocol
| + RFC1122 - Requirements for Internet Hosts - Communication Layers
| + RFC3168 - The Addition of Explicit Congestion Notification (ECN) to IP
| + RFC6093 - On the Implementation of the TCP Urgent Mechanism
| + RFC6528 - Defending against Sequence Number Attacks

RFC to search: 793:2

| - RFC761 - DoD standard Transmission Control Protocol
> RFC793 - Transmission Control Protocol
| + RFC1122 - Requirements for Internet Hosts - Communication Layers
| | + RFC1349 - Type of Service in the Internet Protocol Suite
| | + RFC4379 - Detecting Multi-Protocol Label Switched (MPLS) Data Plane Failures
| | + RFC5884 - Bidirectional Forwarding Detection (BFD) for MPLS Label Switched Paths (LSPs)
| | + RFC6093 - On the Implementation of the TCP Urgent Mechanism
| | + RFC6298 - Computing TCP's Retransmission Timer
| | + RFC6633 - Deprecation of ICMP Source Quench Messages
| | + RFC6864 - Updated Specification of the IPv4 ID Field
| | + RFC8029 - Detecting Multiprotocol Label Switched (MPLS) Data-Plane Failures
| + RFC3168 - The Addition of Explicit Congestion Notification (ECN) to IP
| | + RFC4301 - Security Architecture for the Internet Protocol
| | + RFC6040 - Tunnelling of Explicit Congestion Notification
| | + RFC8311 - Relaxing Restrictions on Explicit Congestion Notification (ECN) Experimentation
| + [P] RFC6093 - On the Implementation of the TCP Urgent Mechanism
| + RFC6528 - Defending against Sequence Number Attacks
```

### Exiting

To exit just enter on a blank line
