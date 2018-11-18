# ETL-lambda
ETL Processes for OpenOil Web App (AWS Lambda)


## ND Web Scrape Final

Web scraping algorithm to receive well information from https://www.dmr.nd.gov website.

The NorthDakotaOAGPull class takes a username, password, and file number (well number). All of the wells that are requested should have main information about the well, but some of them will not have available production data.

The main information will come back in a dictionary form, while the production data will come back in a pandas dataframe.

Here is an example of how to call the 30216 well:


file_30216 = NorthDakotaOAGPull('username','password','30216')


main_info, prod_data = file_30216.get_main_info()
