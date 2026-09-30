#Should run the actual server
"""
- create TCP socket
- bind to 0.0.0.0:9090
- listen for clinets and accept connections
- use ThreadPoolExecutor and recieve requrests using protocol file
- determine what client wants and call appropriate storage function
- send response back with protocol file. (client sends Json style stuff)
"""
