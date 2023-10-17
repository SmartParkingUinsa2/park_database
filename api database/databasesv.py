import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="parking"
        )
        self.cursor = self.conn.cursor(buffered=True)

    def insert_area(self, area_name):
        # Insert data into the "area" table
        sql = "INSERT INTO area (area) VALUES (%s)"
        values = (area_name,)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def insert_images(self, path):
        # Insert data into the "images" table
        sql = "INSERT INTO images (path_images) VALUES (%s)"
        values = (path,)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def insert_parking_data(self, id_area, id_images, hari, jam, jumlah_spd, jumlah_spdm, jumlah_mobil):
        # Insert data into the "parking" table
        sql = "INSERT INTO parking (id_area, id_images, hari, jam, jumlah_spd, jumlah_spdm, jumlah_mobil) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (id_area, id_images, hari, jam, jumlah_spd, jumlah_spdm, jumlah_mobil)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def get_area_by_id(self, area_id):
        # Mengambil data area berdasarkan ID
        sql = "SELECT * FROM area WHERE id_area = %s"
        values = (area_id,)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()

    def get_images_by_id(self, image_id):
        # Mengambil data images berdasarkan ID
        sql = "SELECT * FROM images WHERE id_images = %s"
        values = (image_id,)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()

    def get_parking_data_by_id(self, parking_id):
        # Mengambil data parkir berdasarkan ID
        sql = "SELECT * FROM parking WHERE id_parking = %s"
        values = (parking_id,)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()
    
    def get_area_all(self):
        # Mengambil data area berdasarkan ID
        sql = "SELECT * FROM area"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_parking_data_all(self, parking_id):
        # Mengambil data parkir berdasarkan ID
        sql = "SELECT * FROM parking"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()