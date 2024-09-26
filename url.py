
import urllib.parse
import os
def decode_url(url):
    # Use the unquote function to decode the URL
    return urllib.parse.unquote(url)


def extract_data(url):
    try:
        # Find the start of the target section
        start_index = url.index("#tgWebAppData=") + len("#tgWebAppData=")
        
        # Find the end of the target section
        end_index = url.index("&tgWebAppVersion")
        
        # Extract and return the substring
        return url[start_index:end_index]
    
    except ValueError:
        return "Invalid URL or missing tgWebAppData and tgWebAppVersion"

def main():
    # List to store extracted data
    extracted_data_list = []

    # Read URLs from a file
    with open('urls.txt', 'r') as file:  # Ensure the file name is correct
        for line in file:
            url = line.strip()  # Remove any surrounding whitespace or newline characters
            if url:  # Proceed if the line is not empty
                extracted_data = extract_data(url)
                decoded_url = decode_url(extracted_data)
                extracted_data_list.append(decoded_url)

    # Write all extracted data to data.txt
    with open('data.txt', 'w') as output_file:
        for data in extracted_data_list:
            output_file.write(data + "\n")  # Write each extracted data on a new line

    print("Extracted data has been written to data.txt")
    os.system('clear')
    os.system('python3 bot.py')
if __name__ == "__main__":
    main()