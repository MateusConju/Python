from app.models import Item

def test_create_item_persist(db_session):
    item = Item(name="Item Sujo", description="Um item que deve 'sumir' em breve!")
    db_session.add(item)
    db_session.commit()

    assert db_session.query(Item).count() == 1
    assert db_session.query(Item).first().name == "Item Sujo"

def test_read_item_is_empty(db_session):
    items = db_session.query(Item).all()

    assert len(items) == 0