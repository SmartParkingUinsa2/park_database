import requests

# URL server Flask
server_url = "http://localhost:5000"  # Ganti dengan URL server yang sesuai

# Contoh data yang akan dikirim
area_data = {"area_name": "Nama Area"}
image_data = {"image": ("1.jpeg", open("1.jpeg", "rb"))}
parking_data = {
    "id_area": 112,
    "id_images": 223,
    "hari": "Senin",
    "jam": "2023-10-04 07:00:00",
    "jumlah_spd": 10,
    "jumlah_spdm": 5,
    "jumlah_mobil": 3
}

# Mengirim data area
response = requests.post(f"{server_url}/insert_area", json=area_data)
print("Response from /insert_area:", response.json())

# Mengirim data gambar
response = requests.post(f"{server_url}/insert_images", files=image_data)
print("Response from /insert_images:", response.json())

# Mengirim data parking
response = requests.post(f"{server_url}/insert_parking_data", json=parking_data)
print("Response from /insert_parking_data:", response.json())
