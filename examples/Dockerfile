FROM ubuntu

RUN apt-get update &amp;&amp; apt-get install -y gfortran build-essential make gcc build-essential python python-dev wget libgsl0ldbl gsl-bin libgsl0-dev python-pip git

# blasxxxxxxyyyyy
ADD blas.sh /tmp/blas.sh
RUN chmod 755 /tmp/blas.sh
RUN /tmp/blas.sh
ENV BLAS /usr/local/lib/libfblas.a

# lapack
ADD lapack.sh /tmp/lapack.sh
RUN chmod 755 /tmp/lapack.sh
RUN /tmp/lapack.sh
ENV LAPACK /usr/local/lib/liblapack.a

RUN pip install numpy scipy
RUN easy_install -U ete2

WORKDIR /opt

RUN git clone https://github.com/morrislab/phylowgs.git

RUN cd phylowgs &amp;&amp; g++ -o mh.o  mh.cpp  util.cpp `gsl-config --cflags --libs`
