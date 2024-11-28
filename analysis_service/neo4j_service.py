
class AnalysisRepository:
    def __init__(self, driver):
        self.driver = driver

    def find_bluetooth_connected(self):
        with self.driver.session() as session:
            query = """
                MATCH (start:Device)
                MATCH (end:Device)
                WHERE start <> end
                MATCH path = shortestPath((start)-[:CONNECTED*]->(end))
                WHERE ALL(r IN relationships(path) WHERE r.method = 'Bluetooth')
                WITH path, length(path) as pathLength
                ORDER BY pathLength DESC
                LIMIT 1
                RETURN length(path) as cycle_length
            """

            result = session.run(query).single()
            if result is None:
                return None
            return result['cycle_length']

    def find_signal_strength(self):
        with self.driver.session() as session:
            query = """
                MATCH (d1:Device)-[r:CONNECTED] - > (d2:Device)
                WHERE r.signal_strength_dbm > -60
                RETURN d1.name as from_name, 
                d2.name as to_name, 
                r.signal_strength_dbm as signal_strength
            """

            result = session.run(query)
            if result is None:
                return None

            calls = [{"from": record['from_name'],
                      "to": record["to_name"],
                      "strength": record['signal_strength']}
                     for record in result]
            print(calls)
            return calls

    def count_connected_devices(self, device_id):
        with self.driver.session() as session:
            query = """
                MATCH (d1:Device{device_id: $device_id })-[r:CONNECTED] -  (d2:Device)
                RETURN COUNT(d2) as count_devices
            """

            result = session.run(query, device_id=device_id).single()
            if result is None:
                return 0
            print(result['count_devices'])
            return result['count_devices']

