from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()
flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

ORIGIN_IATA_CODE = "GRU"
tomorrow = datetime.now() + timedelta(days=1)
future = datetime.now() + timedelta(days=6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_IATA_CODE,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=future
    )
    if flight is None:
        continue
    list_emails = [all_your_clients_emails]
    if flight.price <= destination["lowestPrice"]:
        notification_manager.send_emails(
            emails=list_emails,
            message=f"We found a lower price! Only £{flight.price} to book a flight from [{flight.city}-{flight.airport}] to [{flight.destination_city}-{flight.destination_airport}], from {flight.date} to {flight.return_date}.",
            flight_link=f'https://www.google.co.uk/flights?hl=en#flt={flight.airport}.{flight.destination_airport}.{flight.date}*{flight.destination_airport}.{flight.airport}.{flight.return_date}'
        )
