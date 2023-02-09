import tkinter as tk
import requests
from bs4 import BeautifulSoup

def track_prices():
    # Get the list of URLs for dog food items
    URLs = entry.get().split("\n")

    # Keep track of the results
    results = []
    cheapest_price = float('inf')
    cheapest_title = ""

    # Loop through each URL
    for URL in URLs:
        # Make a request to the website
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }
        page = requests.get(URL, headers=headers)

        # Parse the HTML of the page
        soup = BeautifulSoup(page.content, "html.parser")

        # Find the title and price of the product
        title = soup.find(id="productTitle").get_text().strip()
        price = float(soup.find(id="priceblock_ourprice").get_text().strip()[1:].replace(',',''))

        # Add the result to the list
        results.append(f"{title} - ${price:.2f}")

        # Check if this is the cheapest price so far
        if price < cheapest_price:
            cheapest_price = price
            cheapest_title = title

    # Update the result label with all the results
    result_label.config(text="\n".join(results) + f"\n\nCheapest: {cheapest_title} - ${cheapest_price:.2f}")

# Create the Tkinter GUI
root = tk.Tk()
root.title("Amazon Price Tracker")

# Add a label to prompt the user for the URLs
url_label = tk.Label(root, text="Enter the URLs of the dog food items (separated by new lines):")
url_label.pack()

# Add an entry for the URLs
entry = tk.Text(root, height=10, width=50)
entry.pack()

# Add a button to trigger the price tracking
track_button = tk.Button(root, text="Track Prices", command=track_prices)
track_button.pack()

# Add a label to show the results
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI
root.mainloop()