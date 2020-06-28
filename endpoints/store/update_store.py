from models.store import Store
from models.user_store import UserStore

def update(storeId):
    store = Store.objects.get_or_404(id=storeId)

    try:
        user_store = UserStore.objects.get(store_ref_id=storeId)
        session.add(user_store)
        session.commit()
    except Exception as e:
        return jsonify({'error_msg':str(e)})
    return jsonify({'status': 'OK'), 200