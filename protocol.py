#Handle how messages are sent and received over TCP
"""
This file should:
- turn a Python dictionary into JSON
- encode JSON into bytes
- put the 4-byte length header in front
- send the full message
- receive exactly 4 bytes for the header
- determine how long the message is
- receive exactly that many bytes
- turn the bytes back into JSON/Python data
"""

