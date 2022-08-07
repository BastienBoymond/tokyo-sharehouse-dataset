from region import Region

class TokyoShareHouse:
    url = 'https://tokyosharehouse.com/eng/'
    allregions = []

    def __init__(self):
        region = Region();
        self.allregions = region.get_regions();