
<a href="https://crawlbase.com/signup?utm_source=github&utm_medium=readme&utm_campaign=smart_proxy_banner" target="_blank">
  <img width="1090" height="275" 
       src="https://github.com/user-attachments/assets/6735e89e-3a75-43d8-b613-7a5ae776441d" 
       alt="smart-proxy-cta" 
       style="max-width: 100%; border: 0;">
</a>


# How To Unblock Amazon Proxy

We invite you to explore our [blog](https://crawlbase.com/blog/how-to-unblock-amazon-with-smart-proxy/?utm_source=github&utm_medium=referral&utm_campaign=scraperhub&ref=gh_scraperhub) for more details.

## Setting Up Your Coding Environment

Before building your Amazon proxy unblocker, you'll need to set up a basic Python environment. Here's how to get started:

1. [Install Python 3](https://kinsta.com/knowledgebase/install-python/#how-to-install-python) on your computer
2. Run `pip install -r requirements.txt`

## Obtaining API Credentials

1. Create an account at [Crawlbase](https://crawlbase.com/signup) and log in.
2. After registration, you will receive 5,000 free requests.
3. Locate and copy your Smart Proxy [Private Token](https://crawlbase.com/dashboard/account/docs).

## Running the Example Scripts

Before running the examples, make sure to replace every instance of `<Private token>` with your [Private Token](https://crawlbase.com/dashboard/account/docs).

### Example Scripts

- To run the example from the **"Making Your First Successful Request"** section:

```bash
python making_your_first_successful_request.py
```

- To run the example from the **"Extracting Specific Data"** section:

```bash
python extracting_specific_data.py
```

- To run the example from the **"Compiling Extracted Data into CSV"** section:

```bash
python compiling_extracted_data_into_csv.py
```

### Troubleshooting

Occasionally, you may encounter the following error:

```
An error occurred: HTTPSConnectionPool(host='www.amazon.com', port=443): Max retries exceeded with url: /Apple-iPhone-Silicone-Case-MagSafe/dp/B0CHX2XFLN (Caused by ProxyError('Unable to connect to proxy', OSError('Tunnel connection failed: 500 Internal Server Error')))
```

This is typically a temporary issue. Simply rerun the command, and it should resolve itself.

🛡 Disclaimer
This repository is for educational purposes only. Please make sure you comply with the Terms of Service of any website you scrape. Use this responsibly and only where permitted.

---

Copyright 2025 Crawlbase
