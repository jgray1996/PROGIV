from Bio import Entrez
import multiprocessing as mp
import yaml
import ssl
import sys

# Setup SSL to avoid certificate errors
ssl._create_default_https_context = ssl._create_unverified_context

def load_config():
    """
    Load configuration data from a YAML file.

    Returns:
        dict: A dictionary containing configuration data such as email and API key.
    """
    with open("config.yaml") as c_in:
        return yaml.safe_load(c_in)

# Get the number of CPUs available for multiprocessing
cpus = mp.cpu_count()

# Load the configuration data from the YAML file
config = load_config()
Entrez.email = config["email"]
api_key = config["API"]

def entrez_fetch_article_meta_data(id="30049270"):
    """
    Fetch metadata for a given PubMed article.

    Args:
        id (str): The PubMed ID of the article.

    Returns:
        dict: The metadata of the article fetched from Entrez.elink.
    """
    file = Entrez.elink(
        dbfrom="pubmed",
        db="pmc",
        LinkName="pubmed_pmc_refs",
        id=id,
        api_key=api_key,
    )
    return Entrez.read(file)

def extract_article_id_from_metadata(elink_result):
    """
    Extract article IDs from the metadata returned by entrez_fetch_article_meta_data.

    Args:
        elink_result (dict): The metadata returned by Entrez.elink.

    Returns:
        list: A list of article IDs referenced in the metadata.
    """
    return [f'{link["Id"]}' for link in elink_result[0]["LinkSetDb"][0]["Link"]]

def download_article_xml(id):
    """
    Download the full article data for a given PubMed ID and save it as an XML file.

    Args:
        id (str): The PubMed ID of the article to download.
    """
    handle = Entrez.efetch(db="pubmed",
                id=id,
                retmode="xml",
                api_key=api_key)
    
    # Save the XML data to a file named after the article ID
    with open(f"{id}.xml", 'a') as f_out:
        f_out.write(handle.read().decode('utf-8'))


if __name__ == '__main__':
    # Fetch metadata for a specific article
    results = entrez_fetch_article_meta_data(id=input("Enter article id: "))
    # Extract article IDs from the metadata
    article_ids = extract_article_id_from_metadata(results)
    # Use multiprocessing to download articles concurrently
    with mp.Pool(cpus) as p:
        p.map(download_article_xml, article_ids[:10])
    print("Done!")
