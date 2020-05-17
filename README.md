#Usage guide:

assuming one has git and docker installed the example can be run using
```bash
git clone https://github.com/Bijaelo/docker_test.git 
cd docker_test/python_test
docker build -t mydockertest:1.0.0 .
docker run --rm -d --name mydockertest mydockertest:1.0.0
```
One might want to remove using `docker image rm [image]` afterwards to save space.
