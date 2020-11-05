"""Photoshop program"""
import cv2
import imutils

path = 'C:\\Users\\yashw\\OneDrive\\Desktop\\RDSK6021.jpg'
image = cv2.imread(path)
height, width = image.shape[:2]
 
def is_angle_valid_or_not(angle):
	if angle.isdigit() == False:
		print("PLEASE GIVE A VALID ANGLE.")
		exit()

def get_angle_to_rotate_image():
	angle = input("Enter an angle to rotate an image: ")
	return angle

def view_original_image():
	cv2.imshow("Original", image)
	cv2.waitKey(0)

def view_gray_scale_image():
	gray_colour_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imshow("Grayscale", gray_colour_image)
	cv2.waitKey(0)

def view_rotated_image():
	angle = get_angle_to_rotate_image()
	is_angle_valid_or_not(angle)
	angle = int(angle)
	rotated_image = imutils.rotate_bound(image, angle)
	image_name = "Image rotated by " + str(angle) + " degrees"
	cv2.imshow(image_name, rotated_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def view_cropped_image():
	start_row, start_column = int(height * 0.15), int(width * 0.15)
	end_row, end_column = int(height * 0.85), int(width * 0.85)
	cropped_image = image[start_row:end_row, start_column:end_column]
	cv2.imshow("Cropped Image", cropped_image)
	cv2.waitKey(0)

def confirm_to_exit():
	print("Do you want to leave? ")
	user_choice = input("Press Y or N: ")
	if user_choice == 'Y':
		exit()

functions_list = [view_original_image, view_gray_scale_image, view_rotated_image, view_cropped_image, confirm_to_exit]

while True:
	print("1. Original image\n2. Convert colour image into gray scale\n3. Rotate an image\n4. Crop an image\n5. Confirm to exit")
	user_choice = int(input("Enter a number: "))
	if user_choice > 0 and user_choice <=5:
		functions_list[user_choice - 1]()
	else:
		print("ENTER A VALID NUMBER.")