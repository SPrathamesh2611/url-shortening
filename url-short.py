import pyshorteners  # Import the pyshorteners library for URL shortening

url = input("ENTER URL FOR SHORTENING \n")s#Prompt the user to enter the URL for shortening

# Shorten the URL using the pyshorteners library and the TinyURL service
shortened_url = pyshorteners.Shortener().tinyurl.short(url)

print("URL AFTER SHORTENING :- ", shortened_url)  # Print the shortened URL

