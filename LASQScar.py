import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import torch 
import kornia




def make_edges(image,three):
    
    three = np.stack((three,)*3, axis=2)
    three = torch.tensor(three)
    three = np.transpose(three, (2,0,1))  ## to bring channel first 
    three= torch.unsqueeze(three,axis = 0)
    three = three.float()
    magnitude, edges=kornia.filters.canny(three, low_threshold=0.05, high_threshold=0.15, kernel_size=(9, 9), sigma=(5, 5), hysteresis=True, eps=1e-06)
    print(edges.shape)
    edges = np.array(edges)
    image[np.where(edges[0,0,:,:]!=0)] = 1
    return image


def norm(img_slice):
    # Assuming 'img_slice' is your 2D image slice
    img_min = np.min(img_slice)
    img_max = np.max(img_slice)
    
    # Normalize the image
    img_normalized = (img_slice - img_min) / (img_max - img_min)
    
    return img_normalized



def center_crop(image, crop_size=(450, 450)):
    """
    Center crops an RGB image.
    
    Args:
        image (numpy.ndarray): Input image (H, W, C).
        crop_size (tuple): Desired crop size (crop_h, crop_w).
    
    Returns:
        numpy.ndarray: Center-cropped image.
    """
    h, w, _ = image.shape
    crop_h, crop_w = crop_size

    start_x = (w - crop_w) // 2
    start_y = (h - crop_h) // 2

    return image[start_y:start_y + crop_h, start_x:start_x + crop_w]




image = sitk.ReadImage(r"C:\Users\Abbas Khan\Downloads\task1_val_data_gold\val_data_notforpublic\test_3\enhanced.nii.gz")
image_array_3d = sitk.GetArrayFromImage(image)  # Shape: (Depth, Height, Width)

image = sitk.ReadImage(r"C:\Users\Abbas Khan\Downloads\task1_val_data_gold\val_data_notforpublic\test_3\atriumSegImgMO.nii.gz")
atrium_array_3d = sitk.GetArrayFromImage(image)  # Shape: (Depth, Height, Width)

image = sitk.ReadImage(r"C:\Users\Abbas Khan\Downloads\task1_val_data_gold\val_data_notforpublic\test_3\scarSegImgM.nii.gz")
scar_array_3d = sitk.GetArrayFromImage(image)  # Shape: (Depth, Height, Width)



for k in range(60,64):
    image_array = image_array_3d[k,:]
    image_array = np.stack((image_array, image_array,image_array), axis=-1)
    atrium_array = atrium_array_3d[k,:]
    scar_array = scar_array_3d[k,:]
    
    image_array = norm(image_array)
    
    gray = image_array.copy()
    gray = center_crop(gray)
    
    #plt.figure()
    #plt.imshow(gray)
    
    
    atrium_array =atrium_array/255
    image_array[np.where(atrium_array==1)] = [1,1,0]
    image_array[np.where(scar_array==1)] = [1,1,0]
    
    edges = make_edges(image_array,atrium_array)
    
    # plt.figure()
    # plt.imshow(edges)
    
    
    edges = center_crop(edges)
    
    plt.imsave(r'C:\Users\Abbas Khan\Downloads\task1_val_data_gold\viz/' +  str(k)  + '.png', edges)
    plt.imsave(r'C:\Users\Abbas Khan\Downloads\task1_val_data_gold\viz/' +  str(k)+'_img'  + '.png', gray)


