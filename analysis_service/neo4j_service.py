
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

            # patterns = []
            # for record in result:
            #     """
            #     לבחון את התוצאות, לראות אם זה נגיש להבין מי העביר מה וכמה
            #     אם לא - לנסות למצוא פיתרון איך לעצב את מה שחוזר כדי שיהיה לאנליסט נוח
            #     """
            #     pattern = {
            #
            #         'accounts': [node['id'] for node in record['accounts']],
            #         'transactions': [
            #             {
            #                 'amount': tx['amount'],
            #                 'currency': tx['currency'],
            #                 'timestamp': f"{tx['timestamp']}"
            #             } for tx in record['transactions']
            #         ],
            #         'cycle_length': record['cycle_length']
            #     }
            #     patterns.append(pattern)
            #
            # return patterns