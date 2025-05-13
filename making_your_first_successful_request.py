import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url_to_crawl = "https://www.amazon.com/Apple-iPhone-Silicone-Case-MagSafe/dp/B0CHX2XFLN"
crawlbase_normal_token = "<Normal requests token>"
crawlbase_smart_proxy_url = (
    f"https://{crawlbase_normal_token}:@smartproxy.crawlbase.com:8013"
)

try:
    response = requests.get(
        url=url_to_crawl,
        proxies={"http": crawlbase_smart_proxy_url, "https": crawlbase_smart_proxy_url},
        verify=False,
        timeout=30,
    )
    response.raise_for_status()  # Raise an exception for bad status codes

    print("Response Code:", response.status_code)
    print("Response Body:", response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
