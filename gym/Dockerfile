FROM mcr.microsoft.com/devcontainers/miniconda:0-3

RUN wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz
RUN tar -xf mujoco210-linux-x86_64.tar.gz 
RUN mkdir ~/.mujoco/
RUN mv mujoco210/ ~/.mujoco/mujoco210
RUN rm mujoco210-linux-x86_64.tar.gz 
# RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mujoco210/bin


COPY conda_env.yml /tmp/environment.yml
RUN /opt/conda/bin/conda env create -f /tmp/conda-tmp/environment.yml
RUN conda init
RUN echo "conda activate decision-transformer-gym" > ~/.bashrc

CMD [ "bash" ]

