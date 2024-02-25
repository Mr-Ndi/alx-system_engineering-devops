Explanation of Each Element and Related Concepts:

1.--> Load Balancer (HAproxy):

Why: Added for load distribution, improving performance, and ensuring high availability by distributing incoming traffic across multiple servers.
Distribution Algorithm (Round Robin):

Why: Chosen for simplicity. Distributes incoming requests equally among servers. Alternatives like Least Connections or IP Hash may be chosen based on specific needs.
Active-Active Setup:

Why: Both servers actively handle incoming requests, increasing overall system performance and providing redundancy.
-------------------------------> Active-Active vs. Active-Passive:
Active-Active: Both servers are actively serving traffic. More efficient resource utilization but requires proper load balancing and synchronization.
Active-Passive: One server actively serves traffic while the other is on standby. Simpler setup but may lead to underutilization of resources.
Database Primary-Replica Cluster:

Why: Added for high availability and fault tolerance. Allows for read and write operations to be distributed across nodes.
How it Works:
Write Operations (Primary): Handled by the Primary node. Ensures data consistency.
Read Operations (Replica): Replicas can be used to distribute read traffic, improving overall database performance.
---------------------------------> Difference between Primary and Replica in Application:

Why: The application interacts with both nodes for different purposes.
Difference:
Primary Node: Handles write operations, ensuring data consistency and integrity.
Replica Node: Used for read operations, reducing the load on the Primary node and improving overall system performance.
Issues with the Infrastructure:
--------------------------------------------------> Single Points of Failure (SPOFs):

--> Load Balancer: If the load balancer fails, traffic distribution is disrupted.
Individual Servers: If a single server fails, it impacts the availability of the entire application.
Database Primary Node: If the primary node fails, write operations are impacted.
Security Issues:

--> No Firewall: Without a firewall, the infrastructure is vulnerable to unauthorized access and potential attacks.
--> No HTTPS: Lack of HTTPS encryption exposes user data to potential eavesdropping and man-in-the-middle attacks.
--> No Monitoring:

--> Without monitoring:
--> Detection: Issues like performance degradation, downtime, or security threats may go undetected.
--> Proactive Management: Lack of insights into system health makes it challenging to proactively manage and optimize the infrastructure.
