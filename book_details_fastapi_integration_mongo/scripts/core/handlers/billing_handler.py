from scripts.core.db.mongo import read_item, create_item, update_item, delete_item, Item


class ItemHandler:

    def read_data(self):
        return read_item()

    def create_data(self, item: Item):
        return create_item(item)

    def update_data(self, item_id: int, item: Item):
        return update_item(item_id, item)

    def delete_data(self, item_id: int):
        return delete_item(item_id)
