import functools
# calculating the total cost after applying a discount for certain flavors.
ice_cream_price_list = [('vanilla', 40),('strawberry', 50),('mango', 60),('butterscotch', 70),('chocolate', 100),('cookies_n_creme', 120),('blueberry_muffin', 140),('watermelon',  160)]

# map to apply a discount of 10% to the prices of watermelon, mango, blueberry_muffin and butterscotch

discounted_flavors = [
    'watermelon',
    'mango',
    'blueberry_muffin',
    'butterscotch'
]
    
def add(sum_so_far, num):
    return sum_so_far + num

def discount_applier(ice_list):
    filtered_ice_list = list(filter(discount_checker, ice_list))
    unfiltered_ice_list = list(filter(no_discount_checker, ice_list))
    print(f"Filtered Ice List: {filtered_ice_list}")
    print(f"Filtered Ice List: {list(map(price_calculator, filtered_ice_list))}")
    discounted_prices = list(map(price_calculator, filtered_ice_list))
    unchanged_prices = list(map(unchanged_price_calculator, unfiltered_ice_list))
    final_price_list = discounted_prices + unchanged_prices
    print(f"Total Cost: {functools.reduce(add, final_price_list)}")
    return functools.reduce(add, final_price_list)

def price_calculator(x):
    return int(x[1] - x[1] * 0.1)

def unchanged_price_calculator(y):
    return int(y[1])

def discount_checker(item):
    print(f"Item: {item[0] in discounted_flavors}")
    return item[0] in discounted_flavors

def no_discount_checker(price):
    return price[0] not in discounted_flavors

discount_applier(ice_cream_price_list)


