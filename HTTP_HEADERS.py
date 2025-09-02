# HTTP_HEADERS.py

HEADER_PROFILES = [
    # 1. Android Motorola (Chrome)
    {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; moto g(8) power) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7"
    },
    # firefox pi5
    {
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0"
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        "Accept-Language: en-US,en;q=0.5"
        "Accept-Encoding: gzip, deflate, br, zstd"
        "DNT: 1"
        "Connection: keep-alive"
        "Upgrade-Insecure-Requests: 1"
        "Sec-Fetch-Dest: document"
        "Sec-Fetch-Mode: navigate"
        "Sec-Fetch-Site: none"
        "Sec-Fetch-User: ?1"
        "Priority: u=0, i"
    }
]
