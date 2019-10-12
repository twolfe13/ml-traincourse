import datetime
import requests

def download_data(verbose=True):

    """
    Pull the data down from the public servers

    Parameters 
    ----------
    verbose: boolean

    Return
    ------
    trips: list of dicts showing departure and arrival times
    Each dict has a 'dep' and 'arr' field.
    Indicateding the departure and arrival datetime objects 
    for each trip.

    """
    # Harvard Square. Red line stop, outbound
    harvard_stop_id = '70068'

    # JFK / UMass. Red line stop, inbound
    jfk_stop_id = '70086'
    
    # Define time range that we're interested in 
    # Gather trip date from a time window from each day
    start_time = datetime.time(7,0)
    end_time = datetime.time(10,0)
    start_date = datetime.date(2015, 5, 1)
    end_date = datetime.date(2018, 5, 1)
    
    TTravelURL = "http://realtime.mbta.com/developer/api/v2.1/traveltimes"
    TKey = "?api_key=wX9NwuHnZU2ToO7GmGR9uw"
    TFormat = "&format=json"
    from_stop = "&from_stop" + str(jfk_stop_id)
    to_stop = "&to_stop" + str(harvard_stop_id)
    
    # Cycle through all the days 
    #initilize a counter for the day
    i_day = 0 
    #initialize empty list of the trips to collect
    trips = []
    #create a while loop to iterate, day-by-day, through dates of interest
    while True:
        #using .timedelta, after each day we increment the # of days
        check_date = start_date + datetime.timedelta(days=i_day)
        #once we reach a date that's later than our end date, we end loop
        if check_date > end_date: 
            break
        # Formulate the query, specify the time window we are interested
        #for that day
        from_time = datetime.datetime.combine(check_date, start_time)
        to_time = datetime.datetime.combine(check_date, end_time)
        # Convert both into a unix epic timestamp
        TFrom_time = '&from_datetime' + str(int(from_time.timestamp()))
        TTo_time = '&to_datetime' + str(int(to_time.timestamp()))
    
        SRequest = "".join([
            TTravelURL,
            TKey,
            TFormat,
            from_stop,to_stop,
            TFrom_time, TTo_time
    ])
    s = requests.get(SRequest)
    # Convert to nested dicts, a nice format
    s_json = s.json()
    #pull indiv trips out of the response
    for trip in s_json['travel_times']:
        trips.append({
            'dep': datetime.datetime.fromtimestamp(
                float(trip['dep_dt'])),
            'arr': datetime.datetime.fromtimestamp(
                float(trip['arr_dt']))})
    if verbose: 
        print(check_date, ":", len(s_json['travel_times']))
    
    i_day += 1
    return trips

if __name__ == '__main__':
    trips = download_data()
    
