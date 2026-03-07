import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = "3e5540e751686aef108afe88c65097810bf864d2f685b98d1acea134df426a92"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price_usd = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price from API")
    except KeyError:
        sys.exit("Unexpected API response structure")

    total_cost = n_bitcoins * price_usd
    formatted_cost = f"${total_cost:,.4f}"
    print(formatted_cost)


if __name__ == "__main__":
    main()
