from APIS import woocommerce_api as woo
import utilities as ut


def one_day(status, after):
    """ Fetches all orders for that product on that day

       Parameters:
       status (str): pending, processing, on-hold, completed, cancelled or refunded
       after (str): datetimeformat as '1979-11-09T00:00:00'
       before (str): datetimeformat as '1979-11-09T00:00:00', default datetime.now()

       Returns:
       list:Returning a list of all orders

      """
    return woo.fetch_all_orders(status, after)


def first_order_date():
    """ Gets the fist completed order placed from the host and returns that date as an datetime object
       Returns: datetime object
    """
    all_completed_orders = woo.fetch_all_orders('completed')
    order_date = all_completed_orders[0]['date_created'].replace('T', ' ')
    first_order_datetime_object = ut.datetime.strptime(order_date, '%Y-%m-%d %H:%M:%S')
    print('First completed order:', first_order_datetime_object, 'is of type', type(first_order_datetime_object))
    return first_order_datetime_object


def last_order_date():
    """ Gets the last completed order placed from the host and returns that date as an datetime object
       Returns: datetime object
    """
    last_order = woo.fetch_last_order('completed')
    order_date = last_order[0]['date_created'].replace('T', ' ')
    order_datetime_object = ut.datetime.strptime(order_date, '%Y-%m-%d %H:%M:%S')
    print('Last completed order:', order_datetime_object, 'is of type', type(order_datetime_object))
    return order_datetime_object


def fetch_product_categories():
    """ Fetches product information and their assigned categories
       Returns: list of product information as dicts
    """
    product_dicts = []
    for product in woo.products():
        categories = []
        #product variations not showing.... fix needed.
        for item in product['categories']:
            categories.append(item['name'])
        p = {
            'id': product['id'],
            'name': product['name'],
            'sku': product['sku'],
            'stock_quantity': product['stock_quantity'],
            'categories': categories
        }
        product_dicts.append(p)
    return product_dicts


def main():
    # status = 'completed'
    # after = '2021-01-04T00:00:00'
    # orders = one_day(status, after)
    #
    # for order in orders:
    #     ut.print_dict(order)
    #     ut.divider()

    products = fetch_product_categories()
    for p in products:
        print(p)

    sequence = ut.date_sequence(first_order_date(), last_order_date())
    for date_range in sequence:
        print(date_range)


if __name__ == '__main__':
    main()
