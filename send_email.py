import smtplib, ssl


def send_email(message):
    # Mengatur host dan port untuk server SMTP
    # Host "smtp.gmail.com" adalah server SMTP yang digunakan untuk mengirim email dari akun Gmail
    host = "smtp.gmail.com"
    # Port 465 adalah port standar untuk koneksi SSL pada server SMTP
    port = 465

    # Alamat email dan password untuk autentikasi
    # Email pengirim dan juga yang digunakan untuk login
    username = "ikhsansudiramubaroq2910@gmail.com"
    # Password aplikasi (bukan password akun Google) yang digunakan untuk login ke SMTP
    password = "vuis lgyt cvao yetc"

    # Alamat email penerima
    receiver = "ikhsansudiramubaroq2910@gmail.com"
    # Membuat context SSL untuk koneksi yang aman
    context = ssl.create_default_context()

    # Membuka koneksi aman ke server SMTP menggunakan SSL
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # Login ke server SMTP menggunakan username dan password yang diberikan
        server.login(username, password)
        # Mengirim email dari pengirim (username) ke penerima dengan pesan yang diberikan
        server.sendmail(username, receiver, message)
