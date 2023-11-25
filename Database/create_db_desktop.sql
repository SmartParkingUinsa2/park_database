CREATE DATABASE IF NOT EXISTS db_desktop;
USE db_desktop;

-- Table pengguna
CREATE TABLE IF NOT EXISTS pengguna (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    nama VARCHAR(50),
    pass VARCHAR(20),
    level_pengguna VARCHAR(15)
);

-- Table data parkir
CREATE TABLE IF NOT EXISTS parkir (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tahun INTEGER,
    bulan INTEGER,
    tanggal INTEGER,
    hari VARCHAR(6),
    jam INTEGER,
    area VARCHAR(5),
    jenis_kendaraan VARCHAR(12),
    jumlah_kendaraan INTEGER

);