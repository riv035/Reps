import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload_file(self, load_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": f"/{load_file}", "overwrite": "true"}
        headers = {"Content-Type": "application/json", "Accept": "application/json",
                   "Authorization": f"OAuth {token}"}
        response = requests.get(upload_url, params=params, headers=headers)
        href = response.json().get("href")
        if not href:
            print(f"Невозможно получить ссылку для загрузки. Код ошибки: {response.status_code}")
            return
        with open(load_file, "rb") as file:
            requests.put(href, data=file)
        print("Файл успешно загружен в облако")


if __name__ == "__main__":
    file_path = "Test.jpg"
    token = "***"
    uploader = YaUploader(token)
    result = uploader.upload_file(file_path)