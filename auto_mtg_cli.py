from core.mtg_api import get_all_cards_in_set, get_set_image_each_set

if __name__ == '__main__':
    # sets call saves to png_set_images and svg_set_images
    sets = get_set_image_each_set()
    card_tuples = get_all_cards_in_set('rna')
    print(card_tuples)