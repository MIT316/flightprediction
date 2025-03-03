import mysql.connector

class DB:
    def __init__(self):
        # Connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='9033170512',
                database='flight'  # Correct database name
            )
            self.mycursor = self.conn.cursor()
            print('Connection established')
        except mysql.connector.Error as err:
            print(f'Connection error: {err}')

    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
        SELECT DISTINCT(Destination) FROM `flights_cleaned - flights_cleaned`
        UNION
        SELECT DISTINCT(Source) FROM `flights_cleaned - flights_cleaned`
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self, source, destination):
        self.mycursor.execute("""
             SELECT Airline, Route, Dep_Time, Duration, Price 
             FROM `flights_cleaned - flights_cleaned`
             WHERE Source = %s AND Destination = %s
        """, (source, destination))

        data = self.mycursor.fetchall()

        return data

    def fetch_airline_frequency(self):
        airline = []
        frequency = []

        self.mycursor.execute("""
        SELECT Airline, COUNT(*) 
        FROM `flights_cleaned - flights_cleaned`
        GROUP BY Airline
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):
        city = []
        frequency = []

        self.mycursor.execute("""
        SELECT Source, COUNT(*) 
        FROM (
            SELECT Source FROM `flights_cleaned - flights_cleaned`
            UNION ALL
            SELECT Destination FROM `flights_cleaned - flights_cleaned`
        ) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def daily_frequency(self):
        date = []
        frequency = []

        self.mycursor.execute("""
        SELECT Date_of_Journey, COUNT(*) 
        FROM `flights_cleaned - flights_cleaned`
        GROUP BY Date_of_Journey
        """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency
