import py_clob_client.client
from py_clob_client.clob_types import OrderArgs

orig_create_order = py_clob_client.client.ClobClient.create_order
def patched_create_order(self, order_args, *args, **kwargs):
    order_args.fee_rate_bps = 1000
    print("Fee rate patched to:", order_args.fee_rate_bps)
    return orig_create_order(self, order_args, *args, **kwargs)

py_clob_client.client.ClobClient.create_order = patched_create_order

class Dummy: pass
c = Dummy()
py_clob_client.client.ClobClient.create_order(c, OrderArgs("1", 0.5, 5, "BUY"))
