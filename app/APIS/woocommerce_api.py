from APIS.config import *
from datetime import datetime
from woocommerce import API

# DOCS: https://woocommerce.github.io/woocommerce-rest-api-docs/?python#introduction

wcapi = API(
    url=URL,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    version=VERSION
)


# Fetch all orders from server
# status options: pending, processing, on-hold, completed, cancelled, refunded, failed and trash. Default is pending.
def fetch_all_orders(status, after = '1979-11-09T00:00:00', before = datetime.now()):
    """ Fetches all orders

    Parameters:
    status (str): pending, processing, on-hold, completed, cancelled or refunded
    after (str): datetimeformat as '1979-11-09T00:00:00'
    before (str): datetimeformat as '1979-11-09T00:00:00', default datetime.now()

    Returns:
    list:Returning a list of all orders

   """
    ''' Fetches orders based on status; ending, processing, on-hold, completed, cancelled, refunded, failed and trash '''
    print(f"Fetching all {status} orders between {after} and {before}")
    all_orders = []
    fetching = True
    data = {
        "after": after,
        "before": before,
        "page": 1,
        "per_page": 100,
        "status": status

    }

    while fetching:
        if len(wcapi.get("orders/", params=data).json()) == 0:
            print(f'Fetching complete: {len(all_orders)} {status} orders acquired')
            all_orders_sorted = sorted(all_orders, key=lambda k: k['id'])
            return all_orders_sorted
        else:
            for order in wcapi.get("orders/", params=data).json():
                all_orders.append(order)

            print(f'Page @ {data["page"]} | {len(all_orders)}')
            data['page'] += 1


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f'{key}: {value}')


def main():

    for item in fetch_all_orders('completed'):
        print_dict(item)


if __name__ == '__main__':
    main()
