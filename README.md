# Kubernetes-Update-Apps-The-Hard-Way
Exercise in manually updating applications running on Kubernetes

### Deployment Strategies

* Recreate - Deleting old pods and replacing them with new ones
* blue-green - Switching from old to new at once
* Rolling - Replacing one pod at a time with a new version while the old is running in parallel

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

### Recreate

1. Edit ReplicationController or ReplicaSet
2. Update Pod template (image, etc...)
3. Delete all running pods
4. Replication Controller creates new pods from updated template


### Rolling update with kubectl

```
#start curl loop to watch versions change
while true; do curl http://localhost:81;echo \n;sleep 2; done

#use kubeclt rollout to perform upgrade
kubectl rollout archetype-v1 archetype-v2 --image=duffney/archetype:v2
```
