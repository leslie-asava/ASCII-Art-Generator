import cv2
import numpy as np

#ascii_set = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,^`'."
#ascii_set = "N@#W$9876543210?!abc;:+=-,.            "
ascii_set = " " * 10 + ".:-i|=+%O#@"
#ascii_set = ascii_set[::-1]

print(len(ascii_set)) #29

def resize(img, size, padColor=0):

    h, w = img.shape[:2]
    sh, sw = size

    # interpolation method
    if h > sh or w > sw: # shrinking image
        interp = cv2.INTER_AREA
    else: # stretching image
        interp = cv2.INTER_CUBIC

    # aspect ratio of image
    aspect = w/h  # if on Python 2, you might need to cast as a float: float(w)/h

    # compute scaling and pad sizing
    if aspect > 1: # horizontal image
        new_w = sw
        new_h = np.round(new_w/aspect).astype(int)
        pad_vert = (sh-new_h)/2
    elif aspect < 1: # vertical image
        new_h = sh
        new_w = np.round(new_h*aspect).astype(int)
    else: # square image
        new_h, new_w = sh, sw

	# set pad color
    if len(img.shape) == 3 and not isinstance(padColor, (list, tuple, np.ndarray)): # color image but only one color provided
        padColor = [padColor]*3

    # scale and pad
    scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)
    #scaled_img = cv2.copyMakeBorder(scaled_img, pad_top, pad_bot, pad_left, pad_right, borderType=cv2.BORDER_CONSTANT, value=padColor)

    return scaled_img


def generate_ascii_art(image_array):

	image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

	MAX_SIZE = 110

	resized_image = resize(image_array, (MAX_SIZE, MAX_SIZE), 10)

	ascii_array = []

	for row in resized_image:
		current_row = ""
		for column in row:
			
			char = ascii_set[int((column/255) * len(ascii_set) -1 )]

			#print(char, end = "")
			current_row += ascii_set[int((column/255) * len(ascii_set) -1 )]
		#print("\n")
		current_row += "\n"
		ascii_array.append(current_row)

	# with open("output.txt", "w") as output_file:
	# 	for row in ascii_array:
	# 		output_file.write(row)

	return ascii_array

if __name__ == "__main__":

    image_filepath = r"C:\Users\lesli\OneDrive\Desktop\Hack Everything\Image-to-ASCII\ASAVA LESLIE.jpeg"
    image_array = cv2.imread(image_filepath)

    generate_ascii_art(image_array)




# show image
# cv2.imshow('image',resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()