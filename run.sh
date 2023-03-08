# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/yeoju/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/yeoju/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/yeoju/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/yeoju/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

eval "$(conda shell.bash hook)"
conda activate counter &
cd /home/yeoju/projects/vehicle_counter_pyqt_app
pwd
sleep 3
/home/yeoju/anaconda3/envs/counter/bin/python3 App.py
sleep 2