-- Buat database jika belum ada
CREATE DATABASE IF NOT EXISTS parking;
USE parking;


-- Table Area
CREATE TABLE IF NOT EXISTS area (
    id_area INTEGER PRIMARY KEY AUTO_INCREMENT,
    area VARCHAR(20)
);

-- Table Gambar
CREATE TABLE IF NOT EXISTS images (
    id_images INTEGER PRIMARY KEY AUTO_INCREMENT,
    path_images VARCHAR(255)
);

-- Table Parking
CREATE TABLE IF NOT EXISTS parking (
    id_parking INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_area INTEGER,
    id_images INTEGER,
    hari TEXT,
    jam TIMESTAMP(6),
    jumlah_spd INTEGER,
    jumlah_spdm INTEGER,
    jumlah_mobil INTEGER,
    FOREIGN KEY (id_area) REFERENCES area (id_area),
    FOREIGN KEY (id_images) REFERENCES images (id_images),
    UNIQUE(jam)
);