import time
import speedtest
from csv import DictWriter, writer
from os.path import exists

# Would be nice to have a main() function and then a check for "if __name__ == __main__" --> main()

# Set up speedtest parameters and run initial test.
servers = []
st = speedtest.Speedtest()

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
interval_m = 15
interval_s = interval_m * 60.0

while True:

    # Perform the speedtest and extract the results as csv.
    print("Running a new Speedtest")
    # Set up a new speedtest instance so all of the speedtest attributes are refreshed.
    st = speedtest.Speedtest()
    st.get_servers(servers)
    st.download()
    st.upload()
    st_header_list = st.results.csv_header().split(',')
    st_results_dict = st.results.dict()
    # Now, parse the dict for the results we want.
    st_results_list = []
    st_results_list.append(st_results_dict["server"]["id"])
    st_results_list.append(st_results_dict["server"]["sponsor"])
    st_results_list.append(st_results_dict["server"]["name"])
    st_results_list.append(st_results_dict["timestamp"])
    st_results_list.append(st_results_dict["server"]["d"])
    st_results_list.append(st_results_dict["ping"])
    st_results_list.append(st_results_dict["download"])
    st_results_list.append(st_results_dict["upload"])
    st_results_list.append(st_results_dict["share"])
    st_results_list.append(st_results_dict["client"]["ip"])

    # Then, write the latest speedtest results as a new row to the csv.
    # https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/
    with open('speedtest_results.csv', 'a', newline='') as csv_file:
        # Get a writer object to write the results csv list as a new row.
        writer_object = writer(csv_file)
        # Write the new speedtest result list as a new row.
        writer_object.writerow(st_results_list)
        # Then, close the file.
        csv_file.close()

    # Then, wait for whatever amount of time is left until the next desired iteration.
    time.sleep(interval_s - ((time.time() - start_time) % interval_s))