# Kubernetes-Update-Apps-The-Hard-Way
Exercise in manually updating applications running on Kubernetes

## Deployment Strategies

* Recreate - Deleting old pods and replacing them with new ones
* blue-green - Switching from old to new at once
* Rolling - Replacing one pod at a time with a new version while the old is running in parallel

### Manual Recreate

![Deployment strategy Recreate](https://github.com/Duffney/Kubernetes-Update-Apps-The-Hard-Way/blob/master/doc-images/deploymentStrategyRecreate.jpg "Kubernetes Recreate Deployment strategy")


1. Edit ReplicationController or ReplicaSet
2. Update Pod template (image, etc...)
3. Delete all running pods
4. Replication Controller creates new pods from updated template

### Lab

1. Deploy app v1
    ```
    kubectl apply -f archetype-rc-and-service-v1.yaml
    ```
2. Start version check loop
    ```
    while true; do curl http://localhost:81;sleep 2; done
    ```
3. Edit RepliaSet & updated template.spec.image to v2
    ```
    kubectl edit ~
    ```
4. Delete v1 pods
    ```
    kubectl delete pod label -eq something
    ```
Insert Gif here

### blue-green

1. Deploy new ReplicationController or ReplicaSet with update pod template
2. Change service's label selector to reference new pods
3. Delete old ReplicationController or ReplicaSet


### Rolling update with kubectl

1. Deploy new ReplicationController or Replicate set with updated template
2. Delete v1 pods one by one to be replaced with v2 pods using a single service

_application must support running old and new versions along side one another_


```
#start curl loop to watch versions change
while true; do curl http://localhost:81;echo \n;sleep 2; done

#use kubeclt rollout to perform upgrade
kubectl rollout archetype-v1 archetype-v2 --image=duffney/archetype:v2
```
### Kubernetes Deployment Strategies

* RollingUpdate [Default]
* Recreate
  * Use when your application does not support running multiple versions at once
*  


### Build and Deploy App v1

1. Build and upload images to docker hub with tags

```
cd v1; docker build -t duffney/archetype:v1 .
cd ../v2; docker build -t duffney/archetype:v2 .
docker push duffney/archetype
```

2. Deploy v1 to Kubernetes

```
kubectl apply -f v1/archetype-rc-and-service-v1.yaml
```