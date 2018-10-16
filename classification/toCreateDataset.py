''' 
this code does an important task to the project...
I load all the frames and make a cut with a specific size (width and length)
Based on the size I show the max windows extracted from the frame and classify that
Y if the window has a part of Darwin body and N if not has a part of him body.
The Y files are storage with a Y at the end of name and N files with N at the end of name.

Attention to the trade-off here: Large windows = less data to classify, more time running algorithms and more bias
Small windows = more data to classify, less time running algorithms and less bias
Be careful!
'''
# to navigation in folders
import os
# to read images
import cv2

width = 300
height = 300

def classifyImagesFromPath(path = ''):
    if not os.path.exists(path):
        print('folder not found - aborted!')

    if not os.path.exists('dataset'):
        os.mkdir('dataset')
    
    filesInPath = os.listdir(path)
    onlyImagesFilenames= [filename for filename in filesInPath if filename.endswith('.jpg') ]

    for filename in onlyImagesFilenames:
        pathfile = '%s/%s' % (path, filename)
        print(filename)
        img = cv2.imread(pathfile)
        i = 0
        j = 0
        count = 1

        global width
        global height
        while(i < img.shape[0]):
            while(j < img.shape[1]):
                window = img[i:(i+width),j:(j+height),:]

                cv2.imshow('Window', window)
                key = cv2.waitKey()

                if(key == ord('y')):
                    print('Yes')
                    cv2.imwrite('dataset/%s-%s-y.jpg' % (filename, count.6+
                    ), window)
                    cv2.destroyAllWindows()

                elif(key == ord('n')):
                    print('No')
                    cv2.imwrite('dataset/%s-%s-n.jpg' % (filename, count), window)
                    cv2.destroyAllWindows()

                count += 1

                j += height

            i += width

        os.remove(pathfile)

classifyImagesFromPath('/home/renan/whereIsDarwin/classification/frames')




