from models.store import Store
from models.user_store import UserStore


def update(storeId):
    """
    Update Store instance with id=storeId from database.
    If UserStore has object with store_ref_id=storeId, update it.
    """
    store = Store.objects.get_or_404(id=storeId)
    try:
        user_store = UserStore.objects.get(store_ref_id=storeId)
        user_store.update()
    except Exception as e:
        pass

    store.update()

    return {"status": "OK"}, 200
