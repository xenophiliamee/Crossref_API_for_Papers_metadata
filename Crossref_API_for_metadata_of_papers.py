import requests

# List of DOIs
dois = [
    "10.1016/0305-1978(94)90114-7",
    "10.1016/j.quascirev.2017.01.023",
    # Add more DOIs here
]

# Loop through each DOI
for doi in dois:
    # Construct API request URL
    url = f'https://api.crossref.org/works/{doi}'

    try:
        # Send API request
        response = requests.get(url)
        data = response.json()

        # Print the full API response for debugging
        print(f"API response for {doi}:")
        print(data)

        # Extract PDF download URL from API response
        pdf_url = None
        if 'message' in data and 'link' in data['message']:
            for link in data['message']['link']:
                if link.get('content-type') == 'application/pdf':
                    pdf_url = link['URL']
                    break

        if pdf_url:
            # Download the PDF
            pdf_response = requests.get(pdf_url)
            if pdf_response.status_code == 200:
                # Save the PDF to a file
                with open(f'{doi.replace("/", "_")}.pdf', 'wb') as f:
                    f.write(pdf_response.content)
                print(f"Downloaded: {doi}")
            else:
                print(f"Error downloading {doi}: HTTP status {pdf_response.status_code}")

        else:
            print(f"Error downloading {doi}: PDF download URL not found")

    except Exception as e:
        print(f"Error downloading {doi}: {e}")
