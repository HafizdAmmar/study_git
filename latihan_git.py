data_panen = {
    'lokasi1':{
        'nama lokasi':'Kebun A',
        'hasil panen':{
            'padi':1200,
            'jagung':800,
            'kedelai':500
        }
    },
    'lokasi2':{
        'nama lokasi':'Kebun B',
        'hasil panen':{
            'padi':1500,
            'jagung':900,
            'kedelai':450
        }
    },
    'lokasi3':{
        'nama lokasi':'Kebun C',
        'hasil panen':{
            'padi':1100,
            'jagung':750,
            'kedelai':600
        }
    },
    'lokasi4':{
        'nama lokasi':'Kebun D',
        'hasil panen':{
            'padi':1300,
            'jagung':850,
            'kedelai':550
        }
    },
    'lokasi5':{
        'nama lokasi':'Kebun E',
        'hasil panen':{
            'padi':1400,
            'jagung':950,
            'kedelai':480
        }
    }
}

# soal1
print(data_panen)

# soal2
jagung_2 = data_panen['lokasi2']['hasil panen']['jagung']
print(F"Jumlah hasil panen jagung dari lokasi ke 2 adalah {jagung_2}")

# soal3
nama_3 = data_panen['lokasi3']['nama lokasi']
print(f"Nama Lokasi dari Lokasi ke 3 adalah {nama_3}")

# soal4 & 5
hasil_padi = {lokasi: data['hasil panen']['padi'] for lokasi, data in data_panen.items()}
hasil_kedelai = {lokasi: data['hasil panen']['kedelai'] for lokasi, data in data_panen.items()}
print(f"Jumlah hasil panen padi dari setiap lokasi adalah: {hasil_padi}")
print(f"Jumlah hasil panen kedelai dari setiap lokasi adalah: {hasil_kedelai}")

# soal6
for lokasi, data in data_panen.items():
    lokasi = data['nama lokasi']
    padi = data['hasil panen']['padi']
    jagung = data['hasil panen']['jagung']

    if padi > 1300 or jagung > 800:
        print(f"{lokasi} memerlukan perhatian khusus")
    else:
        print(f"{lokasi} dalam kondisi normal")