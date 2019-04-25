from mtgsdk import Set, Card


def get_card_image_from_each_set(up_to_sets=50):
    """
    Get a card from each set
    :param up_to_sets: There are 450 sets this takes a long time to get everycard indicate how many sets you want.
    :return:
    """
    cards = []
    sets = Set.all()[:up_to_sets]
    for set in sets:
        try:
            card = Card.where(set=set.code).iter().__next__()
            cards.append(card.image_url)
        except StopIteration as si:
            pass
    return cards
