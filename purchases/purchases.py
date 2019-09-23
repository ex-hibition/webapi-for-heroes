import logging

logging.basicConfig(level=logging.DEBUG)


class Purchases:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.purchases = [
            {
                "11": [
                    {
                        "201909": [
                            {
                                "goods": "00001",
                                "price": 1500,
                            },
                            {
                                "goods": "00002",
                                "price": 2000,
                            }
                        ]
                    },
                    {
                        "201908": [
                            {
                                "goods": "00001",
                                "price": 1500,
                            },
                            {
                                "goods": "00003",
                                "price": 500,
                            }
                        ]
                    },
                ]
            },
            {
                "12": [
                    {
                        "201909": [
                            {
                                "goods": "00001",
                                "price": 150,
                            },
                            {
                                "goods": "00002",
                                "price": 200,
                            }
                        ]
                    },
                    {
                        "201908": [
                            {
                                "goods": "00001",
                                "price": 150,
                            },
                            {
                                "goods": "00003",
                                "price": 50,
                            }
                        ]
                    },
                ]
            }
        ]

    def get_purchases(self):
        """全データを返す"""
        return self.purchases

    def get_user_purchases(self, target_id):
        """指定idのデータを返す"""
        return [x.get(target_id) for x in self.purchases if x.get(target_id)][0]
