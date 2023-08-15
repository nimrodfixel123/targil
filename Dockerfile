# a. Based on Ubuntu latest image
FROM ubuntu:latest

# b. Define environment variable VERSION=1.2.0
ENV VERSION=1.2.0

# c. Install python
RUN apt-get update && apt-get install -y python3

# d. Install vim
RUN apt-get install -y vim

# e. Install zip
RUN apt-get install -y zip

# f. Install unzip
RUN apt-get install -y unzip

# g. Copy zip_job.py into the image's /tmp folder
COPY zip_job.py /tmp/zip_job.py

# Add proof that /tmp/zip_job.py exists
RUN if [ ! -f /tmp/zip_job.py ]; then echo "ERROR: /tmp/zip_job.py not found"; exit 1; fi

# h. Once docker container is up, run a command which will print OS type and architecture + verify /tmp/zip_job.py exists
CMD echo "os type: $(uname -o)" && echo "arch type: $(uname -m)" && if [ -f /tmp/zip_job.py ]; then echo "file exists: yes"; else echo "file exists: no"; fi
