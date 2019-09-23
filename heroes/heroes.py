import logging
import re

logging.basicConfig(level=logging.DEBUG)


class Heroes:
    # _unique_instance = None
    #
    # @classmethod
    # def get_instance(cls) -> object:
    #     if not cls._unique_instance:
    #         cls._unique_instance = cls()
    #     return cls._unique_instance

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.heroes = [
            {"id": 11, "name": 'Dr Nice'},
            {"id": 12, "name": 'Narco'},
            {"id": 13, "name": 'Bombasto'},
            {"id": 14, "name": 'Celeritas'},
            {"id": 15, "name": 'Magneta'},
            {"id": 16, "name": 'RubberMan'},
            {"id": 17, "name": 'Dynama'},
            {"id": 18, "name": 'Dr IQ'},
            {"id": 19, "name": 'Magma'},
            {"id": 20, "name": 'Tornado'},
        ]

    def get_heroes(self):
        return self.heroes

    def update_hero(self, hero):
        for num, rec in enumerate(self.heroes):
            self.logger.info(f"num={num}, rec={rec}")

            if rec.get('id') == int(hero.get('id')):
                # 指定されたidのデータを配列から削除
                self.heroes.pop(num)
                # 更新後データを配列に追加
                self.heroes.append(hero)
                break

        self.logger.info(f"heroes={self.heroes}")

    def add_hero(self, hero: dict):
        # heroes.idの最大値を取得
        max_id = 0
        for rec in self.heroes:
            if rec.get('id') > max_id:
                max_id = rec.get('id')

        # heroes.idの最大値+1をセット
        hero.update(id=max_id + 1)

        # 新規データを配列に追加
        self.heroes.append(hero)

        self.logger.info(f"new hero={hero}")
        self.logger.info(f"heroes={self.heroes}")

        return hero

    def delete_hero(self, target_id: int):
        for num, rec in enumerate(self.heroes):
            if rec.get('id') == target_id:
                self.heroes.pop(num)
                self.logger.info(f"deleted hero id={target_id}")

        self.logger.info(f"heroes={self.heroes}")

    def search_hero(self, name: str):
        result_list = []
        for num, rec in enumerate(self.heroes):
            if re.match(name, rec.get('name')):
                result_list.append(rec)

        return result_list
