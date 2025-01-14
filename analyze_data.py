from cassandra.cluster import Cluster
from cassandra.query import ConsistencyLevel

class callDrop:
    def __init__(self):
        self.cluster = Cluster(contact_points=["127.0.0.1"], port=9042)
        self.session = self.cluster.connect(keyspace="calldrop")  # Update with your keyspace name
        self.session.default_consistency_level = ConsistencyLevel.QUORUM

    def get_success_percentage(self, start_time, end_time, phone_number=None):
        print("Call Records for the Given Time Range".center(50, "="))
        
        # Prepare the base query for the call data
        query = """
        SELECT * FROM calldrop_tbl1
        WHERE duration_seconds >= %s AND duration_seconds <= %s 
        """
        
        # Add phone_number if provided
        if phone_number:
            query += " AND phone = %s ALLOW FILTERING"
            params = (start_time, end_time, phone_number)
        else:
            query += "ALLOW FILTERING"
            params = (start_time, end_time)
        
        try:
            # Execute the query
            result = self.session.execute(query, params)
            
            # Initialize counters
            total_calls = 0
            successful_calls = 0

            # Loop through the result and process each row
            for row in result:
                total_calls += 1
                # Check if call_completed is True
                if row.call_completed:
                    successful_calls += 1
            
            if total_calls == 0:
                print("No calls found in the given time range.")
                return 0  # Avoid division by zero if no calls are found

            print(f"Total Calls: {total_calls}, Successful Calls: {successful_calls}")
            success_percentage = (successful_calls / total_calls) * 100
            print(f"Percentage of successful calls: {success_percentage:.2f}%")
            return success_percentage

        except Exception as e:
            print(f"Query execution failed: {e}")
            return 0

# Main function to run the script
if __name__ == "__main__":
    app = callDrop()
    start_time = int(input("Enter start time in seconds): "))
    end_time = int(input("Enter end time in seconds: "))
    phone_number = int(input("Enter phone number (Optional): "))
    app.get_success_percentage(start_time, end_time, phone_number)
