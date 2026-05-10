import http.client
import sys

if len(sys.argv) > 1:
    DOMAIN = sys.argv[1]
else:
    DOMAIN = "httpstat.us"


STATUS_CODES = [103, 200, 301, 404, 500]


def fetch_and_process(domain: str, status_code: int):
    print(f">>> Запрашивается https://{domain}/{status_code}")

    conn = http.client.HTTPSConnection(domain, timeout=10)
    try:
        conn.request("GET", f"/{status_code}")
        response = conn.getresponse()
        status = response.status
        body = response.read().decode("utf-8", errors="replace")

        if 100 <= status < 400:
            print(f"Status: {status}")
            print(f"Body: {body}")
        elif 400 <= status < 600:
            raise Exception(f"Получен код статуса ошибки: {status}, Body: {body}")
        else:
            print(f"Необычный статус: {status}, Body: {body}")

    except Exception as e:
        print(f"Возникла ошибка: {e}")
    finally:
        conn.close()


def main():
    print(f"Используется домен: {DOMAIN}\n")
    for code in STATUS_CODES:
        fetch_and_process(DOMAIN, code)


if __name__ == "__main__":
    main()
