# **Web Deployment Demo**
_keyword: docker, django, model-view-template (mvt), port mapping_ 

This demo is going to build a docker container with django service as an application host server. (Web server development with **nginx** will be deployed and extended in the future.)

## **Clone this repo** ##

First of all, clone this repo and cd to the folder.

```
git clone https://github.com/harry83017622/django_deploy.git
```

After cd to the folder, let's take a look if docker run correctly by checking docker version. If there is no error raising, you are on the right track so far.
  
``` docker version ```  

Then, we start to build docker image using the dockerfile in the repo by:  

``` docker build -t image_name . ```  

If the image was built successfully, we can build our container and run it as an application server.  
``` docker run -it --name container_name -p 8000:8000 image_name ```

If you are seeing this:  

```
Performing system checks...
System check identified no issues (0 silenced).
December 29, 2020 - 06:00:02
Django version 1.8.19, using settings 'mysite.settings'
Starting development server at http://0:8000/
Quit the server with CONTROL-C.
[29/Dec/2020 06:00:20] "GET / HTTP/1.1" 200 2670 
```

It means you successfully runing a server in the docker. You can check your browser at http://127.0.0.1:8000/ to see the developed web.