import requests

# URL endpoint API Anda
api_url = "https://2djncpz1-8080.asse.devtunnels.ms/savedata"  # Ganti dengan URL yang sesuai

# Data untuk tabel "area"
data_area = {
    "id_area": 1,
    "area": "Area 1"
}

# Data untuk tabel "images"
data_images = {
    "id_images": 1,
    "path_images": "path/to/image1.jpg"
}

# Data untuk tabel "parking"
data_parking = {
    "id_parking": 1,
    "id_area": 1,
    "id_images": 1,
    "hari": "Senin",
    "jam": "08:00",
    "jumlah_spd": 10,
    "jumlah_spdm": 5,
    "jumlah_mobil": 3
}

try:
    # Mengirim data untuk tabel "area"
    response_area = requests.post(api_url, json=data_area)
    if response_area.status_code == 200:
        print("Data area berhasil disimpan ke database.")
    else:
        print(f"Gagal menyimpan data area. Kode status: {response_area.status_code}")

     # Mengirim data untuk tabel "images"
    response_images = requests.post(api_url, json=data_images)
    if response_images.status_code == 200:
         print("Data images berhasil disimpan ke database.")
    else:
         print(f"Gagal menyimpan data images. Kode status: {response_images.status_code}")

     # Mengirim data untuk tabel "jenis_transportasi"
    response_parking = requests.post(api_url, json=data_parking)
    if response_parking.status_code == 200:
         print("Data jenis_parking berhasil disimpan ke database.")
    else:
         print(f"Gagal menyimpan data parking. Kode status: {response_parking.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Gagal melakukan permintaan ke API: {str(e)}")
