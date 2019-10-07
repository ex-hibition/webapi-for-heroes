import logging

logging.basicConfig(level=logging.DEBUG)


class Billing:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.purchases = [
            {
                "11": [
                    {
                        "201909": [
                            {
                                "method": "credit card",
                                "price": 3500,
                            },
                        ]
                    },
                    {
                        "201908": [
                            {
                                "method": "bill",
                                "price": 2000,
                            },
                        ]
                    },
                ]
            },
            {
                "12": [
                    {
                        "201909": [
                            {
                                "method": "credit card",
                                "price": 350,
                            },
                        ]
                    },
                    {
                        "201908": [
                            {
                                "method": "credit card",
                                "price": 200,
                            },
                        ]
                    },
                ]
            }
        ]

    def get_billing(self):
        """全データを返す"""
        return self.purchases

    def get_user_billing(self, target_id):
        """指定idのデータを返す"""
        try:
            return [x.get(target_id) for x in self.purchases if x.get(target_id)][0]
        except IndexError as e:
            self.logger.info(f"IndexError: ${e}")
            return []
