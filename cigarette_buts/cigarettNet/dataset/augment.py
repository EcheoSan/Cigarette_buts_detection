

class Augment():
    def __init__(self):
        pass


    def generate_img_over_bg(image_path , mask_path , bg_image_path):
    '''
    project a segmented objects over background image
    Args: image_path(str) , mask_path(str) , bg_image_path(str)
    '''
    img = plt.imread(image_path)
    mask = np.load(mask_path)
    bg_img = plt.imread(bg_image_path)

    positions = np.where(mask > 0)
    merged = np.zeros((config.IMG_HEIGHT , config.IMG_WIDTH , 3))
    merged = bg_img.copy()
    for pos_x , pos_y in zip(positions[0] , positions[1]):
        merged[pos_x , pos_y] = img[pos_x , pos_y]

    plt.imsave('../out/image/buts/merged_4.jpg' , merged)