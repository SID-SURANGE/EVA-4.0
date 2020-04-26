<h2><i><b> Assignment B - Train Custom Dataset Using YoloV3 </B><I></H2>
<HR>

<H4> Follow below steps to train YOLOV3 on custom DATASET</H4>
<H6> All the below steps have been referred from repo https://github.com/theschoolofai/YoloV3. Visit here for full implemenation details and model weights</H6>


```
For custom dataset:

1) Clone this repo: https://github.com/miki998/YoloV3_Annotation_Tool
2) Follow the installation steps as mentioned in the repo.
3) For the assignment, download 500 images of your unique object.
4) Annotate the images using the Annotation tool.
5) This is how data looks -
data
  --customdata
    --images/
      --img001.jpg
      --img002.jpg
      --...
    --labels/
      --img001.txt
      --img002.txt
      --...
    custom.data #data file
    custom.names #your class names
    custom.txt #list of name of the images you want your network to be trained on. Currently we are using same file for test/train

6) As you can see above you need to create custom.data file. For 1 class example, your file will look like this:
   classes=1
    train=data/customdata/custom.txt
    test=data/customdata/custom.txt 
    names=data/customdata/custom.names
7) As you it a poor idea to keep test and train data same, but the point of this repo is to get you up and running with YoloV3 asap.  You'll probably do a mistake in writing to custom.txt file. This is how our file looks like (please note the .s and /s):
   ./data/customdata/images/img001.jpg
   ./data/customdata/images/img002.jpg
   ./data/customdata/images/img003.jpg
   ...

8) You need to add custom.names file as you can see above. For our example, we downloaded images of Walle. Our custom.names file look like this:
    Groot
    Groot above will have a class index of 0.

9) For COCO's 80 classes, VOLOv3's output vector has 255 dimensions ( (4+1+80)*3). Now we have 1 class, so we would need to change it's architecture.
10) Copy the contents of 'yolov3-spp.cfg' file to a new file called 'yolov3-custom.cfg' file in the data/cfg folder.
    Search for 'filters=255' (you should get entries entries). Change 255 to 18 = (4+1+1)*3
    Search for 'classes=80' and change all three entries to 'classes=1'
11) Since you are lazy (probably), you'll be working with very few samples. In such a case it is a good idea to change:
    burn_in to 100
    max_batches to 5000
   steps to 4000,4500
12) Run this command python train.py --data data/customdata/custom.data --batch 10 --cache --cfg cfg/yolov3-custom.cfg --epochs 3 --nosave

```

Author - Siddharth Surange
