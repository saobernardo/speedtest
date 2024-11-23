import speedtest
from verify_connection import check_internet_connection

def run():
  st = speedtest.Speedtest()

  st.get_best_server()

  print("Aguarde...")

  download_speed = st.download() / 1_000_000
  print(f"Download Speed: {download_speed:.2f} Mpbs")

  upload_speed = st.upload() / 1_000_000
  print(f"Upload Speed: {upload_speed:.2f} Mbps")

  ping = st.results.ping
  print(f"Ping: {ping:.2f} ms")

if __name__ == "__main__":
  if check_internet_connection():
    run()
  else:
    print('There is no internet connection to test')