from sys import _current_frames


class Portforlio:
    def __init__(self):
        self.number_of_shares = 0
        self.share_list = []

    def is_empty(self):
        return self.number_of_shares == 0

    def unique_share(self):
        return len(self.share_list)

    def purchase_share(self, share_name, buy_count):
        self.number_of_shares += buy_count
        if (len(self.share_list) == 0):
            self.share_list.append(Share(share_name, buy_count))
        else:
            for share in self.share_list:
                if share.name == share_name:
                    share.hold_count += buy_count
                    return
            self.share_list.append(Share(share_name, buy_count))

    def sell_share(self, share_name, sell_count):
        for share in self.share_list:
            if share.name == share_name:
                if sell_count > share.hold_count:
                    raise ShareSaleException
                else:
                    share.sell(sell_count)
                    self.number_of_shares -= sell_count
                    if share.hold_count == 0:
                        self.share_list.remove(share)
    
    def share_num_by_name(self, share_name):
        if (len(self.share_list) == 0):
            return
        else:
            for share in self.share_list:
                if share.name == share_name:
                    return share.hold_count


class Share:
    def __init__(self, name, hold_count):
        self.name = name
        self.hold_count = hold_count

    def sell(self, sell_amount):
        self.hold_count = self.hold_count - sell_amount

class ShareSaleException(Exception):
    pass