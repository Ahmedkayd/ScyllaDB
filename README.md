# ScyllaDB Cluster on EC2 Nodes
## Quick Guide: Running the CallDrop Scripts

This guide explains how to set up and run the two Python scripts for ScyllaDB: 

1. [Data Insertion Script](#Run-Data-Insertion-Script-First)
2. [Success Percentage Calculation Script](#Success-Percentage-Calculation-Script)

---

## Prerequisites

1. **Python Installed**: Ensure Python 3.7 or later is installed.
2. **clone this repo**:
   ```bash
   git clone https://github.com/Ahmedkayd/ScyllaDB.git
   ```
3. **Required Libraries**: Install the necessary Python packages using pip:
   ```bash
   pip install cassandra-driver
   ```
4. Make sure the client server you are using is able to reach the ScyllaDB Cluster hosts.


### ScyllaDB Setup and  run the scripts
- ScyllaDB cluster should be running.
- Ensure the keyspace calldrop and table calldrop_tbl1 exist with the right datatypes.

2. ### Run Data Insertion Script First
    ```bash
    python3 insert_data.py
    ```
    ```bash
    =====================================OUTPUT SAMPLE=======================================
    ubuntu@ip-172-31-40-194:~/scylla$ python3 test.py 
    /home/ubuntu/scylla/test.py:13: DeprecationWarning: Setting the consistency level at the session level will be removed in 4.0. Consider using execution profiles and setting the desired consistency level to the EXEC_PROFILE_DEFAULT profile.
    self.session.default_consistency_level = ConsistencyLevel.QUORUM
    Connected to ScyllaDB and set keyspace 'calldrop'!
    Sample data inserted successfully!
    Cluster and session closed.
    ```
2. ### Success Percentage Calculation Script
    ```bash
    success_percentage.py
    ```
    ```bash
    =====================================OUTPUT SAMPLE=======================================
    ubuntu@ip-172-31-40-194:~/scylla$ python3 success_percentage.py
    /home/ubuntu/scylla/success_percentage.py:12: DeprecationWarning: Setting the consistency level at the session level will be removed in 4.0. Consider using execution profiles and setting the desired consistency level to the EXEC_PROFILE_DEFAULT profile.
    self.session.default_consistency_level = ConsistencyLevel.QUORUM
    Connected to ScyllaDB and set keyspace 'calldrop'!
    Enter start time in seconds: 1
    Enter end time in seconds: 3600
    Enter phone number (Optional): 6187600354
    ======Call Records for the Given Time Range=======
    Total Calls: 21, Successful Calls: 17
    Percentage of successful calls: 80.95%
    ```