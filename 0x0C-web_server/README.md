**Main Role of a Web Server:**
A web server's main role is to respond to incoming requests from clients (typically web browsers) and deliver web content (such as HTML pages, images, and other resources) over the internet. It handles the communication between clients and the hosted websites, ensuring that the requested information is sent back to the user's browser.

**Child Process:**
A child process is a subprocess that is spawned by a parent process. When a program or process creates another process, the newly created process is referred to as the child process, and the original process is the parent process. Child processes inherit certain attributes and resources from their parent but operate independently.

**Parent and Child Processes in Web Servers:**
Web servers often use a parent-child process model for scalability and robustness. The parent process manages and controls the overall server, while multiple child processes handle individual client requests. This design allows the server to handle concurrent connections efficiently. If one child process encounters an issue (e.g., due to a specific request), it does not affect the operation of other child processes, providing better stability.

**Main HTTP Requests:**
The main HTTP requests are:

1. **GET:** Requests data from a specified resource.
2. **POST:** Submits data to be processed to a specified resource.
3. **PUT:** Updates a specified resource.
4. **DELETE:** Deletes a specified resource.
5. **HEAD:** Retrieves the headers of a specified resource without the actual data.
6. **OPTIONS:** Requests information about the communication options available for the target resource.

**DNS:**
**DNS stands for Domain Name System.**

**Main Role of DNS:**
The main role of DNS is to translate human-readable domain names (like www.example.com) into IP addresses that computers use to identify each other on a network. DNS acts as a distributed database, providing a hierarchical naming system for resources connected to the internet.

**DNS Record Types:**

1. **A (Address) Record:** Maps a domain to an IPv4 address.
2. **CNAME (Canonical Name) Record:** Alias of one domain to another, used for domain redirection.
3. **TXT (Text) Record:** Holds text information, often used for descriptive or SPF (Sender Policy Framework) records.
4. **MX (Mail Exchange) Record:** Specifies mail servers responsible for receiving email messages on behalf of a domain.
