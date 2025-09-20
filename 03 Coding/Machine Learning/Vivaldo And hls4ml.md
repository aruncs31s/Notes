---
id: Vivaldo And hls4ml
aliases: []
tags:
  - coding
  - machine_learning
dg-publish: true
---
#### Requirements

```bash
sudo apt-get install python3-venv git cmake

```

```bash
git clone https://github.com/fprotopapa/hls4ml-tutorial
cd hls4ml-tutorial/
python3 -m venv venv_hls4ml
source venv_hls4ml/bin/activate
pip install --upgrade pip
pip install notebook
ipython kernel install --user --name=.venv_hls4ml
pip install hls4ml[rolling]

```

^1d13b4

#### onnx install

```bash
sudo apt-get install python3-pip python3-dev libprotobuf-dev protobuf-compiler

git clone https://github.com/onnx/onnx.git
cd onnx
git submodule update --init --recursive
# Optional: prefer lite proto
export CMAKE_ARGS=-DONNX_USE_LITE_PROTO=ON
pip install -e . -v

```

#### For Cent OS

##### Requirements

```bash
sudo yum install epel-release
sudo yum groupinstall 'development tools'
sudo yum install python-pip python3-venv git cmake

```

Then do [[#^1d13b4]]
