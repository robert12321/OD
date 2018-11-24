cd Didi-Training-Release-1

echo "Creating .bin pointcloud files from .bag files"
python2 pcl_from_bag.py
python2 interp.py ./TRACKLETS/


echo "Creating .txt labels from .xml tracklets"
python2 xml_to_label.py ./TRACKLETS/

echo "Copying labels to second.pytorchUdacity/data/KITTI/training/label_2/"
for dir in label-*
do
  cd $dir
  for file in *
  do
    cp $file ../../second.pytorchUdacity/data/KITTI/training/label_2/"$file"-1-"$dir"-.txt
  done
  cd ..
done

echo "Copying .bin files to second.pytorchUdacity/data/KITTI/training/velodyne/"
for dir in pc-*-proc
do
  cp ./$dir/* ../second.pytorchUdacity/data/KITTI/training/velodyne/
done

echo "Copying images to second.pytorchUdacity/data/KITTI/training/image_2/"
cd ./TRACKLETS/
for dir in *
do
  sudo cp ./$dir/camera/* ../../second.pytorchUdacity/data/KITTI/training/image_2/
done

echo "Copying xml files"
for dir in *
do
  sudo cp ./$dir/*.xml ../
done

echo "Moving to second.pytorchUdacity/data/KITTI/testing/"
cd ../../second.pytorchUdacity/data/KITTI/testing/

echo "Creating calibration files"
python2 create_calib.py 

echo "Renaming files to KITTI indices"
python2 KITTI_Udacity_inds.py
python2 trans_inds_to_KITTI.py
python2 test_inds.py



echo "Moving to second.pytorchUdacity/data/KITTI/training/"
cd ../training/

echo "Creating calibration files"
python2 create_calib.py 

echo "Renaming files to KITTI indices"
python2 KITTI_Udacity_inds.py
python2 trans_inds_to_KITTI.py

