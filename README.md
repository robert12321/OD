# Konfiguracja rozwiązania SECOND na danych Udacity

## Instalacja oprogramowania
### 1. Instalacja CUDA 9.0 oraz CUDNN 7.3
Pobrać plik instalatora i cztery pakiety ze strony https://developer.nvidia.com/cuda-90-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=deblocal
Razem powinno być pięć pobranych plików .deb
Przejść do katalogu z pobranymi plikami i wykonać następujące polecenia.
```bash
sudo dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64.deb
for dir in /var/cuda-repo-*/
do
  sudo apt-key add $dir/7fa2af80.pub
done
sudo apt-get update
sudo apt-get install cuda
```

Następnie trzeba dodać następujący kod na początek pliku ~/.bashrc
```bash
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

Aby sprawdzić poprawność instalacji należy wykonać:
```bash
cuda-install-samples-9.0.sh ~/
cd ~/NVIDIA_CUDA-9.0_Samples
make
cd bin/x86_64/linux/release/
./deviceQuery
./bandwidthTest
```
Wykonanie programów deviceQuery oraz bandwidthTest powinno wyświetlić na końcu "Result = PASS"

Więcej informacji o CUDA 9.0 znajduje się na stronie https://docs.nvidia.com/cuda/archive/9.0/cuda-installation-guide-linux/

Aby zainstalować CUDNN należy wejść na stronę https://developer.nvidia.com/rdp/cudnn-archive i pobrać trzy zaznaczone na ilustracji pliki
W razie konieczności trzeba założyć konto i zalogować się na stronie https://developer.nvidia.com

Po pobraniu plików należy wejść do katalogu z pobranymi plikami i wykonać:
```bash
sudo dpkg -i libcudnn7*
```

W celu weryfikacji poprawności instalacji należy wykonać:
```bash
cp -r /usr/src/cudnn_samples_v7/ $HOME
cd  $HOME/cudnn_samples_v7/mnistCUDNN
make clean && make
./mnistCUDNN
```
Po wykonaniu powinien pojawić się napis "Test passed!"

Więcej informacji o CUDNN znajduje się na https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installlinux

### 2. Instalacja Docker CE

```bash
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce
```

W celu sprawdzenia poprawności instalacji należy uruchomić:
```bash
sudo docker run hello-world
```

Więcej informacji o Docker CE znajduje się na https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce


### 3. Instalacja ROS Kinetic

W celu instalacji ROS Kinetic należy wykonać:
```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
sudo rosdep init
rosdep update
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

Następnie należy zainstalować przydatne pakiety
```bash
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt-get install ros-kinetic-velodyne
```

Więcej informacji o ROS Kinetic na http://wiki.ros.org/kinetic/Installation/Ubuntu
Poradnik na temat wizualizacji danych Udacity w oprogramowaniu ROS znajduje się na https://github.com/udacity/didi-competition/blob/master/docs/GettingStarted.md

### 4. Instalacja Anaconda 3 i utworzenie środowiska secondEnv 

Należy pobrać instalator Anaconda3 dla systemu Linux ze strony https://www.anaconda.com/download/#linux
Po pobraniu należy go uruchomić i zainstalować Anaconda3 w folderze domyślnym, czyli w ~/.
Aktywacja środowiska Anaconda 3 odbywa się po wykonaniu:
```bash
source ~/anaconda/bin/activate/
```

Po instalacji Anaconda3 należy utworzyć środowisko secondEnv
```bash
conda create -n secondEnv python=3.6.7
```

Aktywowanie środowiska odbywa się po wykonaniu:
```bash
conda activate secondEnv
```

## Konfiguracja rozwiązania
### 1. Pobranie repozytorium 

```bash
git clone https://github.com/robert12321/OD.git
cd ./OD/second.pytorchUdacity/
source ~/anaconda3/bin/activate
conda activate secondEnv
pip install numba
pip install shapely fire pybind11 pyqtgraph tensorboardX protobuf
sudo apt-get install libboost-all-dev
./install.sh
```

Należy dodać do na początek pliku ~/.bashrc linie:
```bash
export NUMBAPRO_CUDA_DRIVER=/usr/lib/x86_64-linux-gnu/libcuda.so
export NUMBAPRO_NVVM=/usr/local/cuda/nvvm/lib64/libnvvm.so
export NUMBAPRO_LIBDEVICE=/usr/local/cuda/nvvm/libdevice
```


### 2. Instalacja SparseConvNet

```bash
source 
conda install pytorch-nightly -c pytorch 
conda install google-sparsehash -c bioconda
conda install -c anaconda pillow
cd second.pytorchUdacity/
git clone https://github.com/facebookresearch/SparseConvNet.git
cd SparseConvNet/
bash build.sh
```

## Konwersja danych Udacity na KITTI
### 1. Konwersja danych Didi-Release-2

Pobierz plik torrent ze strony http://academictorrents.com/details/18d7f6be647eb6d581f5ff61819a11b9c21769c7
Pobierz dane za pomocą programu obsługującego pliki torrent np. Free Download Manager
Rozpakować archiwum Didi-Release-2.tar.gz
Skopiować pliki .bag z katalogów /1/, /2/ i /3/ znajdujących się w /Didi-Release-2/Data/ do odpowiadających im katalogów w OD/Didi-Release-2/Data/
Wejść do katalogu OD/ i uruchomić:
```bash
./create_tracklets_for_Didi-Release-2.sh
./convert_Didi-Release-2.sh
```

### 2. Konwersja danych Didi-Training-Release-1

Pobierz plik torrent ze strony http://academictorrents.com/details/76352487923a31d47a6029ddebf40d9265e770b5
Pobierz dane za pomocą programu obsługującego pliki torrent np. Free Download Manager
Rozpakować archiwum Didi-Training-Release-1.tar.gz do katalogu OD/Didi-Training-Release-1/
Usunąć z rozpakowanych danych katalog Noisy/ oraz plik NOISY_spin_2.bag
Przejść do katalogu OD/ i wykonać:
```bash
./create_tracklets_for_Didi-Training-Release-1.sh
./convert_Didi-Training-Release-1.sh
```

## Uruchomienie rozwiązania
Przejść do katalogu OD/second.pytorchUdacity/ i uruchomić:
```bash
./run.sh
```
