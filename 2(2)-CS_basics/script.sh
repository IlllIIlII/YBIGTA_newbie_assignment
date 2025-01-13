#!/bin/bash

if ! command -v conda &> /dev/null; then
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh -b -p $HOME/miniconda
    rm miniconda.sh
fi

source ~/miniconda/etc/profile.d/conda.sh

if ! conda env list | grep -q "myenv"; then
    conda create -n myenv python=3.9 -y
fi

conda activate myenv
if [[ $? -ne 0 ]]; then
    exit 1
fi

# ## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "가상환경 활성화: 성공"
else
    echo "가상환경 활성화: 실패"
    exit 1 
fi

pip install mypy

if [ ! -d "submission" ]; then
    exit 1
fi
cd submission || { echo "submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    problem_name=$(basename "$file" .py)
    input_file="../input/${problem_name}_input"
    output_file="../output/${problem_name}_output"

    if [ ! -f "$input_file" ]; then
        continue
    fi

    python "$file" < "$input_file" > "$output_file"
done

mypy --strict .

conda deactivate