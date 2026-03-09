import imageio.v3 as iio
import os

os.chdir(r'C:\Users\Lenovo\moonberlyy')

filenames = [
    r'C:\Users\Lenovo\moonberlyy\pic1.jpg',
    r'C:\Users\Lenovo\moonberlyy\pic2.jpg'
]
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))
  

iio.imwrite('frog.gif', images, duration = 500, loop = 0)