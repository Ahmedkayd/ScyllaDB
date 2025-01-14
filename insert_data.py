from cassandra.cluster import Cluster
from cassandra.query import ConsistencyLevel
import random

class CallDrop:
    def __init__(self):
        try:
            self.cluster = Cluster(['127.0.0.1'], port=9042)
            self.session = self.cluster.connect()
            self.session.set_keyspace('calldrop')
            self.session.default_consistency_level = ConsistencyLevel.QUORUM
            print("Connected to ScyllaDB and set keyspace 'calldrop'!")
        except Exception as e:
            print(f"Error connecting to ScyllaDB: {e}")
            self.session = None

    def generate_call_records(self):
        """Generate random call records."""
        users = [random.randint(1000000000, 9999999999) for _ in range(15)] 
        towers = [f'Tower-{i}' for i in range(1, 11)]  # 10 cell tower IDs
        records = []

        for user in users:
            for _ in range(random.randint(20, 25)):  # 20-25 calls per user
                destination = random.randint(1000000000, 9999999999)  # Random destination phone number
                record = {
                    'phone': user,
                    'destination': destination,
                    'duration_seconds': random.randint(1, 3600),  # Call duration between 1 second to 1 hour
                    'src_cell_tower_id': random.choice(towers),
                    'destination_cell_tower_id': random.choice(towers),
                    'call_completed': random.choice([True, False]),
                    'phone_imei': str(random.randint(10**14, 10**15 - 1)),  # Random 15-digit number
                }
                records.append(record)
        return records

    def insert_call_records(self, records):
        """Insert the generated records into the CallDrop_tbl1 table."""
        if not self.session:
            print("No active session. Cannot insert records.")
            return
        
        query = """
        INSERT INTO CallDrop_tbl1 (
            phone,
            destination,
            duration_seconds,
            src_cell_tower_id,
            destination_cell_tower_id,
            call_completed,
            phone_imei
        ) VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        try:
            for record in records:
                self.session.execute(query, (
                    record['phone'],
                    record['destination'],
                    record['duration_seconds'],
                    record['src_cell_tower_id'],
                    record['destination_cell_tower_id'],
                    record['call_completed'],
                    record['phone_imei'],
                ))
            print("Sample data inserted successfully!")
        except Exception as e:
            print(f"Data insertion failed: {e}")

    def close(self):
        """Close the session and cluster connection."""
        if self.session:
            self.session.shutdown()
        if self.cluster:
            self.cluster.shutdown()
        print("Cluster and session closed.")

# Instantiate and run the app
if __name__ == "__main__":
    app = CallDrop()
    try:
        records = app.generate_call_records()
        app.insert_call_records(records)
    finally:
        app.close()
