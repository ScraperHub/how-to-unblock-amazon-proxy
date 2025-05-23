import requests
import json
import csv
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url_to_crawl = "https://www.amazon.com/Apple-iPhone-Silicone-Case-MagSafe/dp/B0CHX2XFLN"
crawlbase_normal_token = "<Normal requests token>"
crawlbase_crawling_api_parameters = "scraper=amazon-product-details"
crawlbase_smart_proxy_url = (
    f"https://{crawlbase_normal_token}:@smartproxy.crawlbase.com:8013"
)

try:
    response = requests.get(
        url=url_to_crawl,
        headers={"CrawlbaseAPI-Parameters": crawlbase_crawling_api_parameters},
        proxies={"http": crawlbase_smart_proxy_url, "https": crawlbase_smart_proxy_url},
        verify=False,
        timeout=30,
    )
    response.raise_for_status()

    json_data = json.loads(response.text)
    product_reviews = json_data["body"]["reviews"]

    with open("product_reviews.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Author", "Rating", "Date", "Review"])  # Header
        for review in product_reviews:
            writer.writerow(
                [
                    review["reviewerName"],
                    review["reviewRating"],
                    review["reviewDate"],
                    review["reviewText"],
                ]
            )

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
