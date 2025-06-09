import requests
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url_to_crawl = "https://www.amazon.com/Apple-iPhone-Silicone-Case-MagSafe/dp/B0CHX2XFLN"
crawlbase_private_token = "<Private token>"
crawlbase_crawling_api_parameters = "scraper=amazon-product-details"
crawlbase_smart_proxy_url = (
    f"https://{crawlbase_private_token}:@smartproxy.crawlbase.com:8013"
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

    for review in product_reviews:
        # TODO save the values here in a CSV file
        # but console print for now
        print("--------------------")
        print("Author: ", review["reviewerName"])
        print("Rating: ", review["reviewRating"])
        print("  Date: ", review["reviewDate"])
        print("Review: ", review["reviewText"])

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
