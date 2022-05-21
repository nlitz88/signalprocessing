import time
import speedtest
from csv import writer
from os.path import exists


# Set up speedtest parameters.
servers = [34840]
st = speedtest.Speedtest()
st.get_servers(servers)         # I think this command grabs the actual IP of the servers whose ID we provide.

# Set up logging file if not already existing.
file_exists = exists('speedtest_results.csv')
if not file_exists:
    with open('speedtest_results.csv', 'a', newline='') as csv_file:
        # Set up the first row as the row of headers.
        writer_object = writer(csv_file)
        header_list = st.results.csv_header().split(',')
        writer_object.writerow(header_list)
        csv_file.close()

# Main recording loop. Perform a speedtest every <interval> minutes
start_time = time.time()
interval_m = 30
interval_s = interval_m * 60.0

while True:

    # Perform the speedtest and extract the results as csv.
    print("Running a new Speedtest")
    st.download()
    st.upload()
    st_results_csv_header = st.results.csv_header()
    st_results_csv = st.results.csv()
    result_list = st_results_csv.split(',')

    # Then, write the latest speedtest results as a new row to the csv.
    # https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/
    with open('speedtest_results.csv', 'a', newline='') as csv_file:
        # Get a writer object to write the results csv list as a new row.
        writer_object = writer(csv_file)
        # Write the new speedtest result list as a new row.
        writer_object.writerow(result_list)
        # Then, close the file.
        csv_file.close()

    # Then, wait for whatever amount of time is left until the next desired iteration.
    time.sleep(interval_s - ((time.time() - start_time) % interval_s))