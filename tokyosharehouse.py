from region import Region

class TokyoShareHouse:
    url = 'https://tokyosharehouse.com/eng/'
    region = []

    def __init__(self):
        region = Region();
        self.region = region.get_regions();