
from models.store import Store
from models.user_store import UserStore


def delete(storeId):
    """
    Remove Store instance with id=storeId from database.
    if UserStore has object with store_ref_id=storeId remove it.
    """
    store = Store.objects.get_or_404(_id=storeId)
    try:
        user_store = UserStore.objects.get(store_ref_id=storeId)
        user_store.delete()
    except Exception as e:
        pass

    store.delete()

    return {"status": "OK"}, 200
