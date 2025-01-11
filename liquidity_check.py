import requests
def liquidity(contract_address):
    """Fetch liquidity & market cap from DEX Screener API."""
    url = requests.get(
        f"https://api.dexscreener.com/latest/dex/tokens/{contract_address}",
        headers={},
    )
    response = url.json()
    if "pairs" in response:
        pair = response["pairs"][0]
        liquidity = pair.get("liquidity", {})
        market_cap = pair.get("fdv", "N/A")

        # Extract liquidity in USD
        usd_liquidity = liquidity.get("usd", 0)

        print(f" Liquidity: ${usd_liquidity} |  Market Cap: {market_cap}")
        return usd_liquidity, market_cap

    else:
        print(" Token not found on DEX Screener")
        return 0, None