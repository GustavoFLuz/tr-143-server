# Use the official CentOS image from the Docker Hub
FROM centos:latest

# Change to the yum repository directory
WORKDIR /etc/yum.repos.d/

# Disable mirrorlist in yum repository files
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

# Update the CentOS image
RUN yum -y update

WORKDIR /

# Install necessary packages
RUN yum -y install \
#    vim \
#    git \
    curl

# Install Apache HTTP Server
RUN yum -y install httpd

# Copy custom configuration file to Apache directory
COPY httpd.conf /etc/httpd/conf/httpd.conf

COPY 00-dav.conf /etc/httpd/conf.modules.d/00-dav.conf

# Enable Apache HTTP Server to start on boot
#RUN systemctl enable httpd

# Expose port 80
EXPOSE 80

# Start Apache HTTP Server in the foreground
#CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
