from core.mtg_api import get_card_image_from_each_set

if __name__ == '__main__':
    cards = get_card_image_from_each_set()
    for card_img in cards:
        print(card_img)