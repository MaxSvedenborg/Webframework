from APIS import woocommerce_api as wapi


def one_day(status, after):
    """ Fetches all orders for that product on that day

       Parameters:
       status (str): pending, processing, on-hold, completed, cancelled or refunded
       after (str): datetimeformat as '1979-11-09T00:00:00'
       before (str): datetimeformat as '1979-11-09T00:00:00', default datetime.now()

       Returns:
       list:Returning a list of all orders

      """
    return wapi.fetch_all_orders(status, after)


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f'{key}: {value}')

def divider():
    print('-' * 150)

def main():
    status = 'completed'
    after = '2021-01-04T00:00:00'
    orders = one_day(status, after)

    for order in orders:
        print_dict(order)
        divider()


if __name__ == '__main__':
    main()
